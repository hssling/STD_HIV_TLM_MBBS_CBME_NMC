#!/usr/bin/env python3
"""
PDF Index Generator for STD & HIV Educational Content
Converts the HTML index to a professional PDF document

Author: Dr. Siddalingaiah H S
Professor, Community Medicine
SIMSRH, Tumkur
Email: hssling@yahoo.com
Phone: +91 8941087719

Generates PDF documentation from HTML index
"""

import os
import sys
from pathlib import Path

def generate_pdf_from_html():
    """
    Generate PDF from HTML index using available PDF generation libraries
    """
    html_file = "index.html"
    pdf_file = "STD_HIV_Educational_Index.pdf"

    if not os.path.exists(html_file):
        print(f"❌ Error: {html_file} not found!")
        return False

    print("🔄 Generating PDF index...")

    # Try different PDF generation methods
    success = False

    # Method 1: Try pdfkit (requires wkhtmltopdf)
    try:
        import pdfkit
        print("📄 Using pdfkit for PDF generation...")

        # PDF generation options for better formatting
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
            'no-outline': None,
            'enable-local-file-access': None,
            'print-media-type': None,
            'disable-smart-shrinking': None
        }

        pdfkit.from_file(html_file, pdf_file, options=options)
        success = True
        print(f"✅ PDF generated successfully: {pdf_file}")

    except ImportError:
        print("⚠️ pdfkit not available, trying alternative methods...")
    except Exception as e:
        print(f"⚠️ pdfkit failed: {e}")

    # Method 2: Try weasyprint
    if not success:
        try:
            from weasyprint import HTML, CSS
            print("📄 Using weasyprint for PDF generation...")

            # Generate PDF with weasyprint
            HTML(html_file).write_pdf(pdf_file)
            success = True
            print(f"✅ PDF generated successfully: {pdf_file}")

        except ImportError:
            print("⚠️ weasyprint not available, trying alternative methods...")
        except Exception as e:
            print(f"⚠️ weasyprint failed: {e}")

    # Method 3: Try pyppeteer (requires chromium)
    if not success:
        try:
            import asyncio
            from pyppeteer import launch
            print("📄 Using pyppeteer for PDF generation...")

            async def generate_pdf():
                browser = await launch()
                page = await browser.newPage()
                await page.goto(f'file://{os.path.abspath(html_file)}')
                await page.pdf({'path': pdf_file, 'format': 'A4'})
                await browser.close()

            asyncio.get_event_loop().run_until_complete(generate_pdf())
            success = True
            print(f"✅ PDF generated successfully: {pdf_file}")

        except ImportError:
            print("⚠️ pyppeteer not available")
        except Exception as e:
            print(f"⚠️ pyppeteer failed: {e}")

    # Method 4: Try xhtml2pdf (reportlab)
    if not success:
        try:
            from xhtml2pdf import pisa
            print("📄 Using xhtml2pdf for PDF generation...")

            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            with open(pdf_file, 'wb') as f:
                pisa.CreatePDF(html_content, dest=f)
            success = True
            print(f"✅ PDF generated successfully: {pdf_file}")

        except ImportError:
            print("⚠️ xhtml2pdf not available")
        except Exception as e:
            print(f"⚠️ xhtml2pdf failed: {e}")

    if not success:
        print("❌ No PDF generation library available!")
        print("\n📦 To generate PDFs, install one of these libraries:")
        print("   pip install pdfkit        # Requires wkhtmltopdf system package")
        print("   pip install weasyprint     # Pure Python, most reliable")
        print("   pip install pyppeteer      # Requires chromium")
        print("   pip install xhtml2pdf      # Uses reportlab")
        print("\n💡 Alternative: Open index.html in a web browser and print to PDF manually")
        return False

    # Verify PDF was created
    if os.path.exists(pdf_file):
        file_size = os.path.getsize(pdf_file) / 1024  # KB
        print(f"📊 PDF size: {file_size:.1f} KB")
        return True
    else:
        print("❌ PDF file was not created!")
        return False

def print_manual_instructions():
    """
    Print instructions for manual PDF generation
    """
    print("\n📋 Manual PDF Generation Instructions:")
    print("=" * 50)
    print("1. Open 'index.html' in your web browser")
    print("2. Press Ctrl+P (or Cmd+P on Mac) to open print dialog")
    print("3. Select 'Save as PDF' or 'Print to PDF'")
    print("4. Choose A4 paper size")
    print("5. Set margins to default/narrow")
    print("6. Enable 'Print backgrounds' if available")
    print("7. Save as 'STD_HIV_Educational_Index.pdf'")
    print("\n🌐 Browser Compatibility:")
    print("   ✅ Chrome/Chromium - Best results")
    print("   ✅ Firefox - Good results")
    print("   ✅ Safari - Good results")
    print("   ✅ Edge - Good results")

def main():
    """
    Main function to generate PDF index
    """
    print("🏥 STD & HIV Educational Content - PDF Index Generator")
    print("=" * 60)

    # Check if HTML file exists
    if not os.path.exists("index.html"):
        print("❌ Error: index.html not found in current directory!")
        print("   Make sure you're running this script from the project root.")
        sys.exit(1)

    # Try to generate PDF automatically
    if generate_pdf_from_html():
        print("\n🎉 Success! Your PDF index has been created.")
        print("   You can now share or print the comprehensive index.")
    else:
        print("\n📄 Automatic PDF generation failed.")
        print_manual_instructions()

    print("\n📖 The HTML index (index.html) can also be viewed directly in any web browser.")
    print("   It contains hyperlinks to all educational materials and is fully interactive.")

if __name__ == "__main__":
    main()
