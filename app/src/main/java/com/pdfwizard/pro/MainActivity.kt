package com.pdfwizard.pro

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.contract.ActivityResultContracts
import androidx.activity.viewModels
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.compose.material3.SnackbarDuration
import androidx.compose.material3.SnackbarHostState
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.ui.platform.LocalContext
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.pdfwizard.pro.ui.theme.PdfWizardTheme
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {

    private val viewModel: PdfEditorViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        handleIntent(intent)
        setContent {
            val state by viewModel.state.collectAsStateWithLifecycle()
            val context = LocalContext.current
            val snackbarHostState = remember { SnackbarHostState() }
            val coroutineScope = rememberCoroutineScope()
            val isDarkTheme = isSystemInDarkTheme()

            val pdfPickerLauncher = rememberLauncherForActivityResult(ActivityResultContracts.OpenDocument()) { uri ->
                if (uri != null) {
                    grantUriPermission(uri)
                    viewModel.loadPdf(uri)
                }
            }

            val imagePickerLauncher = rememberLauncherForActivityResult(ActivityResultContracts.GetContent()) { uri ->
                if (uri != null) {
                    viewModel.addImageFromUri(uri)
                }
            }

            PdfWizardTheme(darkTheme = isDarkTheme) {
                PdfEditorScreen(
                    state = state,
                    snackbarHostState = snackbarHostState,
                    onOpenPdf = { pdfPickerLauncher.launch(arrayOf("application/pdf")) },
                    onDeletePage = viewModel::deleteCurrentPage,
                    onRotatePage = viewModel::rotateCurrentPage,
                    onMovePageLeft = viewModel::moveCurrentPageLeft,
                    onMovePageRight = viewModel::moveCurrentPageRight,
                    onDuplicatePage = viewModel::duplicateCurrentPage,
                    onInsertBlankPage = viewModel::insertBlankPage,
                    onAddAnnotation = viewModel::addAnnotation,
                    onInsertImage = { imagePickerLauncher.launch("image/*") },
                    onSave = { callback ->
                        viewModel.exportPdf { uri ->
                            callback(uri)
                            uri?.let { shareUri -> sharePdf(shareUri) }
                        }
                    },
                    onPageSelected = viewModel::setCurrentPage,
                    onEditMetadata = { viewModel.toggleMetadataEditor(true) },
                    onDismissMetadata = { viewModel.toggleMetadataEditor(false) },
                    onMetadataUpdated = viewModel::updateMetadata
                )
            }

            LaunchedEffect(state.message, state.error) {
                state.message?.let { message ->
                    coroutineScope.launch {
                        snackbarHostState.showSnackbar(message = message, duration = SnackbarDuration.Short)
                        viewModel.clearNotifications()
                    }
                }
                state.error?.let { message ->
                    coroutineScope.launch {
                        snackbarHostState.showSnackbar(message = message, duration = SnackbarDuration.Short)
                        viewModel.clearNotifications()
                    }
                }
            }
        }
    }

    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        handleIntent(intent)
    }

    private fun handleIntent(intent: Intent?) {
        val data = intent?.data ?: return
        grantUriPermission(data)
        viewModel.loadPdf(data)
    }

    private fun grantUriPermission(uri: Uri) {
        try {
            contentResolver.takePersistableUriPermission(uri, Intent.FLAG_GRANT_READ_URI_PERMISSION)
        } catch (_: SecurityException) {
            // Uri may not be persistable
        }
    }

    private fun sharePdf(uri: Uri) {
        val shareIntent = Intent(Intent.ACTION_SEND).apply {
            type = "application/pdf"
            putExtra(Intent.EXTRA_STREAM, uri)
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        startActivity(Intent.createChooser(shareIntent, getString(R.string.share_title)))
    }
}
