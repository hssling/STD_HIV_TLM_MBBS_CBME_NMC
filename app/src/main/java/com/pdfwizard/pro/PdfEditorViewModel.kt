package com.pdfwizard.pro

import android.app.Application
import android.content.ContentResolver
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Canvas
import android.graphics.Matrix
import android.graphics.Paint
import android.graphics.pdf.PdfDocument
import android.graphics.pdf.PdfRenderer
import android.net.Uri
import android.os.Environment
import android.provider.DocumentsContract
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.core.content.FileProvider
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.pdfwizard.pro.R
import com.tom_roush.pdfbox.android.PdfBoxResourceLoader
import com.tom_roush.pdfbox.pdmodel.PDDocument
import com.tom_roush.pdfbox.pdmodel.PDDocumentInformation
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.text.SimpleDateFormat
import java.util.Calendar
import java.util.Collections
import java.util.Date
import java.util.Locale
import kotlin.math.min
import kotlin.math.roundToInt

class PdfEditorViewModel(application: Application) : AndroidViewModel(application) {

    private val appContext = getApplication<Application>()

    init {
        PdfBoxResourceLoader.init(appContext)
    }

    private val _state = MutableStateFlow(PdfEditorState())
    val state: StateFlow<PdfEditorState> = _state

    fun clearNotifications() {
        _state.update { it.copy(message = null, error = null) }
    }

    fun setCurrentPage(index: Int) {
        _state.update { current ->
            if (!current.hasDocument) {
                current
            } else {
                current.copy(currentPageIndex = index.coerceIn(0, current.pageCount - 1))
            }
        }
    }

    fun loadPdf(uri: Uri) {
        viewModelScope.launch {
            _state.update {
                it.copy(
                    isProcessing = true,
                    error = null,
                    message = null,
                    pages = emptyList(),
                    currentPageIndex = 0
                )
            }
            try {
                val pages = withContext(Dispatchers.IO) { renderPdf(appContext.contentResolver, uri) }
                if (pages.isEmpty()) {
                    _state.update { it.copy(isProcessing = false, error = appContext.getString(R.string.export_error)) }
                } else {
                    val displayName = resolveDisplayName(appContext.contentResolver, uri)
                    val baseName = displayName.substringBeforeLast('.')
                    _state.update {
                        it.copy(
                            documentName = displayName,
                            pages = pages,
                            currentPageIndex = 0,
                            isProcessing = false,
                            metadata = PdfMetadata(title = baseName.ifBlank { displayName }),
                            lastSavedFilePath = null,
                            message = appContext.getString(R.string.pdf_loaded, pages.size)
                        )
                    }
                }
            } catch (ex: Exception) {
                if (ex is CancellationException) throw ex
                _state.update { it.copy(isProcessing = false, error = ex.localizedMessage ?: appContext.getString(R.string.generic_error)) }
            }
        }
    }

    fun deleteCurrentPage() {
        _state.update { current ->
            if (!current.hasDocument) return@update current
            val updated = current.pages.toMutableList().also { list ->
                if (current.currentPageIndex in list.indices) {
                    list.removeAt(current.currentPageIndex)
                }
            }
            if (updated.isEmpty()) {
                current.copy(
                    pages = emptyList(),
                    currentPageIndex = 0,
                    message = appContext.getString(R.string.all_pages_removed)
                )
            } else {
                current.copy(
                    pages = updated.mapIndexed { index, page -> page.copy(index = index) },
                    currentPageIndex = current.currentPageIndex.coerceIn(0, updated.lastIndex),
                    message = appContext.getString(R.string.page_deleted)
                )
            }
        }
    }

    fun rotateCurrentPage() {
        _state.update { current ->
            if (!current.hasDocument) return@update current
            val index = current.currentPageIndex
            if (index !in current.pages.indices) return@update current
            val pages = current.pages.toMutableList()
            val page = pages[index]
            val rotatedBitmap = rotateBitmap(page.bitmap)
            pages[index] = page.copy(
                rotationDegrees = (page.rotationDegrees + 90) % 360,
                width = rotatedBitmap.width,
                height = rotatedBitmap.height,
                bitmap = rotatedBitmap,
                annotations = page.annotations.map { rotateAnnotation(it, page.height) },
                images = page.images.map { rotateImageStamp(it, page.height) }
            )
            current.copy(pages = pages, message = appContext.getString(R.string.page_rotated))
        }
    }

    fun moveCurrentPageLeft() = movePageBy(-1)

    fun moveCurrentPageRight() = movePageBy(1)

    fun duplicateCurrentPage() {
        _state.update { current ->
            if (!current.hasDocument) return@update current
            val index = current.currentPageIndex
            if (index !in current.pages.indices) return@update current
            val page = current.pages[index]
            val duplicatedBitmap = page.bitmap.copy(page.bitmap.config ?: Bitmap.Config.ARGB_8888, true)
            val timestamp = System.currentTimeMillis()
            val duplicatedAnnotations = page.annotations.mapIndexed { idx, annotation ->
                annotation.copy(id = timestamp + idx)
            }
            val duplicatedImages = page.images.mapIndexed { idx, image ->
                image.copy(
                    id = timestamp + duplicatedAnnotations.size + idx,
                    bitmap = image.bitmap.copy(image.bitmap.config ?: Bitmap.Config.ARGB_8888, true)
                )
            }
            val pages = current.pages.toMutableList()
            val insertIndex = (index + 1).coerceAtMost(pages.size)
            pages.add(
                insertIndex,
                page.copy(
                    index = insertIndex,
                    bitmap = duplicatedBitmap,
                    annotations = duplicatedAnnotations,
                    images = duplicatedImages
                )
            )
            current.copy(
                pages = pages.mapIndexed { idx, item -> item.copy(index = idx) },
                currentPageIndex = insertIndex,
                message = appContext.getString(R.string.page_duplicated)
            )
        }
    }

    fun insertBlankPage() {
        _state.update { current ->
            val reference = current.pages.getOrNull(current.currentPageIndex)
            val width = reference?.width ?: 1240
            val height = reference?.height ?: 1754
            val blankBitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888).apply {
                eraseColor(android.graphics.Color.WHITE)
            }
            val pages = current.pages.toMutableList()
            val insertIndex = if (current.hasDocument) {
                (current.currentPageIndex + 1).coerceAtMost(pages.size)
            } else {
                0
            }
            pages.add(
                insertIndex,
                PdfPageState(
                    index = insertIndex,
                    width = width,
                    height = height,
                    rotationDegrees = 0,
                    bitmap = blankBitmap
                )
            )
            val defaultName = appContext.getString(R.string.default_document_name)
            val defaultTitle = appContext.getString(R.string.default_document_title)
            val newDocumentName = if (current.documentName.isBlank()) defaultName else current.documentName
            val newMetadata = if (current.metadata.title.isBlank()) current.metadata.copy(title = defaultTitle) else current.metadata
            current.copy(
                pages = pages.mapIndexed { idx, page -> page.copy(index = idx) },
                currentPageIndex = insertIndex,
                documentName = newDocumentName,
                metadata = newMetadata,
                message = appContext.getString(R.string.blank_page_inserted)
            )
        }
    }

    fun toggleMetadataEditor(show: Boolean) {
        _state.update { it.copy(showMetadataEditor = show, message = null, error = null) }
    }

    fun updateMetadata(metadata: PdfMetadata) {
        _state.update {
            it.copy(
                metadata = metadata,
                showMetadataEditor = false,
                message = appContext.getString(R.string.metadata_updated)
            )
        }
    }

    fun addAnnotation(pageIndex: Int, annotation: PdfAnnotation) {
        _state.update { current ->
            if (!current.hasDocument || pageIndex !in current.pages.indices) return@update current
            val pages = current.pages.toMutableList()
            val page = pages[pageIndex]
            pages[pageIndex] = page.copy(annotations = page.annotations + annotation)
            current.copy(pages = pages)
        }
    }

    fun addImageStamp(pageIndex: Int, stamp: PdfImageStamp) {
        _state.update { current ->
            if (!current.hasDocument || pageIndex !in current.pages.indices) return@update current
            val pages = current.pages.toMutableList()
            val page = pages[pageIndex]
            pages[pageIndex] = page.copy(images = page.images + stamp)
            current.copy(pages = pages)
        }
    }

    fun addImageFromUri(uri: Uri) {
        viewModelScope.launch {
            val snapshot = _state.value
            val pageIndex = snapshot.currentPageIndex
            if (!snapshot.hasDocument || pageIndex !in snapshot.pages.indices) {
                return@launch
            }
            val bitmap = withContext(Dispatchers.IO) {
                appContext.contentResolver.openInputStream(uri)?.use { inputStream ->
                    BitmapFactory.decodeStream(inputStream)
                }
            } ?: return@launch

            val page = snapshot.pages[pageIndex]
            val maxScale = min(
                page.width.toFloat() / bitmap.width.toFloat(),
                page.height.toFloat() / bitmap.height.toFloat()
            ).coerceAtMost(1f)
            val desiredScale = (maxScale * 0.6f).coerceAtLeast(0.2f)
            val scaledBitmap = Bitmap.createScaledBitmap(
                bitmap,
                (bitmap.width * desiredScale).roundToInt().coerceAtLeast(1),
                (bitmap.height * desiredScale).roundToInt().coerceAtLeast(1),
                true
            )
            val position = Offset(
                (page.width - scaledBitmap.width) / 2f,
                (page.height - scaledBitmap.height) / 2f
            )
            addImageStamp(
                pageIndex,
                PdfImageStamp(
                    id = System.currentTimeMillis(),
                    pageIndex = pageIndex,
                    bitmap = scaledBitmap,
                    position = position,
                    scale = 1f
                )
            )
            _state.update {
                it.copy(message = appContext.getString(R.string.image_added))
            }
        }
    }

    fun exportPdf(onResult: (Uri?) -> Unit) {
        val snapshot = _state.value
        if (!snapshot.hasDocument) {
            onResult(null)
            return
        }
        viewModelScope.launch {
            _state.update { it.copy(isProcessing = true, message = appContext.getString(R.string.saving_pdf), error = null) }
            val metadata = snapshot.metadata.touch()
            val outputFile = withContext(Dispatchers.IO) {
                try {
                    val file = createExportFile(snapshot.documentName)
                    PdfDocument().use { document ->
                        snapshot.pages.forEachIndexed { pageIndex, page ->
                            val pageInfo = PdfDocument.PageInfo.Builder(page.width, page.height, pageIndex + 1).create()
                            val pdfPage = document.startPage(pageInfo)
                            val canvas = pdfPage.canvas
                            canvas.drawBitmap(page.bitmap, 0f, 0f, null)
                            drawAnnotations(canvas, page)
                            drawImages(canvas, page)
                            document.finishPage(pdfPage)
                        }
                        FileOutputStream(file).use { stream ->
                            document.writeTo(stream)
                        }
                    }
                    applyMetadata(file, metadata)
                    file
                } catch (io: IOException) {
                    null
                }
            }
            if (outputFile != null) {
                val shareUri = FileProvider.getUriForFile(
                    appContext,
                    "${appContext.packageName}.fileprovider",
                    outputFile
                )
                _state.update {
                    it.copy(
                        isProcessing = false,
                        lastSavedFilePath = outputFile.absolutePath,
                        metadata = metadata,
                        message = appContext.getString(R.string.export_success)
                    )
                }
                onResult(shareUri)
            } else {
                _state.update { it.copy(isProcessing = false, error = appContext.getString(R.string.export_error)) }
                onResult(null)
            }
        }
    }

    private fun movePageBy(offset: Int) {
        _state.update { current ->
            if (!current.hasDocument) return@update current
            val fromIndex = current.currentPageIndex
            val toIndex = (fromIndex + offset).coerceIn(0, current.pageCount - 1)
            if (fromIndex == toIndex) return@update current
            val pages = current.pages.toMutableList()
            Collections.swap(pages, fromIndex, toIndex)
            current.copy(
                pages = pages.mapIndexed { idx, page -> page.copy(index = idx) },
                currentPageIndex = toIndex,
                message = appContext.getString(R.string.page_reordered)
            )
        }
    }

    private fun drawAnnotations(canvas: Canvas, page: PdfPageState) {
        if (page.annotations.isEmpty()) return
        val paint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
            style = Paint.Style.FILL
        }
        page.annotations.forEach { annotation ->
            paint.color = annotation.color.toArgb()
            paint.textSize = annotation.fontSize * canvas.scaleFactor
            canvas.drawText(annotation.text, annotation.position.x, annotation.position.y, paint)
        }
    }

    private fun drawImages(canvas: Canvas, page: PdfPageState) {
        page.images.forEach { stamp ->
            val matrix = Matrix().apply {
                setScale(stamp.scale, stamp.scale)
                postTranslate(stamp.position.x, stamp.position.y)
            }
            canvas.drawBitmap(stamp.bitmap, matrix, null)
        }
    }

    private fun rotateAnnotation(annotation: PdfAnnotation, pageHeight: Int): PdfAnnotation {
        val newPosition = Offset(
            pageHeight - annotation.position.y,
            annotation.position.x
        )
        return annotation.copy(position = newPosition)
    }

    private fun rotateImageStamp(stamp: PdfImageStamp, pageHeight: Int): PdfImageStamp {
        val rotatedBitmap = rotateBitmap(stamp.bitmap)
        val newPosition = Offset(
            pageHeight - stamp.position.y - rotatedBitmap.height,
            stamp.position.x
        )
        return stamp.copy(bitmap = rotatedBitmap, position = newPosition)
    }

    private suspend fun renderPdf(contentResolver: ContentResolver, uri: Uri): List<PdfPageState> = withContext(Dispatchers.IO) {
        val descriptor = contentResolver.openFileDescriptor(uri, "r") ?: return@withContext emptyList()
        val renderer = PdfRenderer(descriptor)
        val pages = mutableListOf<PdfPageState>()
        try {
            for (index in 0 until renderer.pageCount) {
                renderer.openPage(index).use { page ->
                    val bitmap = Bitmap.createBitmap(page.width, page.height, Bitmap.Config.ARGB_8888)
                    page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
                    pages += PdfPageState(
                        index = index,
                        width = bitmap.width,
                        height = bitmap.height,
                        rotationDegrees = 0,
                        bitmap = bitmap
                    )
                }
            }
        } finally {
            renderer.close()
            descriptor.close()
        }
        pages
    }

    private fun resolveDisplayName(contentResolver: ContentResolver, uri: Uri): String {
        return runCatching {
            contentResolver.query(
                uri,
                arrayOf(DocumentsContract.Document.COLUMN_DISPLAY_NAME),
                null,
                null,
                null
            )?.use { cursor ->
                val column = cursor.getColumnIndex(DocumentsContract.Document.COLUMN_DISPLAY_NAME)
                if (cursor.moveToFirst() && column != -1) cursor.getString(column) else null
            }
        }.getOrNull() ?: uri.lastPathSegment ?: "EditedDocument.pdf"
    }

    private fun createExportFile(documentName: String): File {
        val baseName = documentName.substringBeforeLast('.')
            .ifBlank { "PDF_Wizard_Export" }
        val timestamp = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.US).format(Date())
        val exportDir = File(appContext.getExternalFilesDir(Environment.DIRECTORY_DOCUMENTS), "exports").apply {
            mkdirs()
        }
        return File(exportDir, "${baseName}_$timestamp.pdf")
    }

    private fun applyMetadata(file: File, metadata: PdfMetadata) {
        runCatching {
            PDDocument.load(file).use { document ->
                val info = document.documentInformation ?: PDDocumentInformation().also { document.documentInformation = it }
                info.title = metadata.title
                info.author = metadata.author
                info.subject = metadata.subject
                info.keywords = metadata.keywords
                info.creator = metadata.creator
                info.producer = metadata.producer
                val calendar = Calendar.getInstance().apply { timeInMillis = metadata.modifiedAt }
                info.modificationDate = calendar
                if (info.creationDate == null) {
                    info.creationDate = calendar
                }
                document.save(file)
            }
        }
    }

    private fun Color.toArgb(): Int = android.graphics.Color.argb(
        (alpha * 255).toInt().coerceIn(0, 255),
        (red * 255).toInt().coerceIn(0, 255),
        (green * 255).toInt().coerceIn(0, 255),
        (blue * 255).toInt().coerceIn(0, 255)
    )

    private val Canvas.scaleFactor: Float
        get() = runCatching {
            val field = Canvas::class.java.getDeclaredField("mDensity")
            field.isAccessible = true
            val density = field.getInt(this)
            if (density <= 0) 1f else density / 72f
        }.getOrDefault(1f)

    private fun rotateBitmap(source: Bitmap): Bitmap {
        val matrix = Matrix().apply { postRotate(90f) }
        return Bitmap.createBitmap(source, 0, 0, source.width, source.height, matrix, true)
    }
}
