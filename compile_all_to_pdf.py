#!/usr/bin/env python3
"""
Comprehensive PDF Compiler for STD & HIV Educational Content
Compiles all educational materials into a single PDF with blue hypertext index

Author: Dr. Siddalingaiah H S
Professor, Community Medicine
SIMSRH, Tumkur
Email: hssling@yahoo.com
Phone: +91-8941087719

Date: November 2024
License: MIT License
"""

import os
import sys
from pathlib import Path
import markdown
from bs4 import BeautifulSoup
import re
from typing import List, Dict, Tuple

class ComprehensivePDFCompiler:
    """
    Compiles all STD & HIV educational content into a single PDF with hyperlinked index
    """

    def __init__(self):
        self.content_files = [
            # Core educational content
            "STD_and_HIV_TLM.md",
            "STD_Class_Video_Script.md",
            "STD_Class_Visualizations.md",
            "HIV_Class_Video_Script.md",
            "HIV_Class_Visualizations.md",
            "STD_One_Hour_Class_Script.md",
            "HIV_One_Hour_Class_Script.md",
            "Visual_Assets_Guide.md",

            # Documentation
            "docs/api.md",
            "docs/deployment.md",
            "docs/development.md",

            # README and other docs
            "README.md"
        ]

        self.output_pdf = "STD_HIV_Comprehensive_Educational_Content.pdf"
        self.temp_html = "comprehensive_content_temp.html"

    def read_markdown_file(self, file_path: str) -> Tuple[str, str]:
        """
        Read and convert markdown file to HTML with enhanced formatting

        Args:
            file_path: Path to markdown file

        Returns:
            Tuple of (title, html_content)
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title from first heading
            lines = content.split('\n')
            title = "Untitled"
            for line in lines[:10]:  # Check first 10 lines for title
                if line.startswith('# '):
                    title = line[2:].strip()
                    break

            # Enhanced markdown conversion with more extensions
            extensions = [
                'toc',           # Table of contents
                'tables',        # Table support
                'fenced_code',   # Code blocks
                'codehilite',    # Syntax highlighting
                'footnotes',     # Footnotes
                'attr_list',     # Attribute lists
                'def_list',      # Definition lists
                'abbr',          # Abbreviations
                'md_in_html',    # Markdown in HTML blocks
                'meta',          # Metadata
                'nl2br',         # Newlines to <br>
                'sane_lists'     # Sane list handling
            ]

            # Convert markdown to HTML with enhanced extensions
            html_content = markdown.markdown(content, extensions=extensions, extension_configs={
                'codehilite': {
                    'linenums': False,
                    'guess_lang': False,
                },
                'toc': {
                    'permalink': True,
                    'permalink_class': 'headerlink',
                }
            })

            # Post-process HTML for better PDF formatting
            html_content = self.post_process_html(html_content)

            return title, html_content

        except Exception as e:
            print(f"⚠️ Error reading {file_path}: {e}")
            return f"Error: {file_path}", f"<p>Error loading content from {file_path}</p>"

    def post_process_html(self, html_content: str) -> str:
        """
        Post-process HTML content for better PDF formatting

        Args:
            html_content: Raw HTML from markdown conversion

        Returns:
            Processed HTML with improved formatting
        """
        # Add proper styling for code blocks
        html_content = html_content.replace('<code>', '<code style="background: #f8f9fa; padding: 2px 4px; border-radius: 3px; font-family: monospace;">')
        html_content = html_content.replace('<pre>', '<pre style="background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 4px; padding: 15px; margin: 15px 0; font-family: monospace; font-size: 12px; overflow-x: auto;">')

        # Improve table styling
        html_content = html_content.replace('<table>', '<table style="width: 100%; border-collapse: collapse; margin: 15px 0; border: 1px solid #dee2e6;">')
        html_content = html_content.replace('<th>', '<th style="border: 1px solid #dee2e6; padding: 8px; text-align: left; background: #f8f9fa; font-weight: bold;">')
        html_content = html_content.replace('<td>', '<td style="border: 1px solid #dee2e6; padding: 8px; text-align: left;">')

        # Improve blockquote styling
        html_content = html_content.replace('<blockquote>', '<blockquote style="border-left: 4px solid #2E86AB; padding-left: 15px; margin: 15px 0; background: #f8f9fa; padding: 10px 15px;">')

        # Improve list styling
        html_content = html_content.replace('<ul>', '<ul style="margin: 15px 0; padding-left: 30px;">')
        html_content = html_content.replace('<ol>', '<ol style="margin: 15px 0; padding-left: 30px;">')

        # Improve link styling
        html_content = html_content.replace('<a href=', '<a style="color: #0066CC; text-decoration: underline;" href=')

        # Improve emphasis styling
        html_content = html_content.replace('<strong>', '<strong style="font-weight: bold;">')
        html_content = html_content.replace('<em>', '<em style="font-style: italic;">')

        return html_content

    def generate_table_of_contents(self, sections: List[Dict[str, str]]) -> str:
        """
        Generate HTML table of contents with blue hyperlinks

        Args:
            sections: List of dicts with 'title' and 'anchor' keys

        Returns:
            HTML string for table of contents
        """
        toc_html = """
        <div class="toc-container">
            <h1 style="color: #2E86AB; border-bottom: 3px solid #2E86AB; padding-bottom: 10px;">
                📚 Table of Contents
            </h1>
            <div class="toc-content">
        """

        for i, section in enumerate(sections, 1):
            title = section['title']
            anchor = section['anchor']
            toc_html += f"""
                <div class="toc-item">
                    <a href="#{anchor}" style="color: #0066CC; text-decoration: none; font-weight: bold;">
                        {i}. {title}
                    </a>
                </div>
            """

        toc_html += """
            </div>
        </div>
        <div style="page-break-before: always;"></div>
        """

        return toc_html

    def create_comprehensive_html(self) -> str:
        """
        Create comprehensive HTML document with all content

        Returns:
            Complete HTML string
        """
        sections = []

        # HTML template with blue hyperlink styling
        html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>STD & HIV Comprehensive Educational Content</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20mm;
            background: white;
        }

        .header {
            text-align: center;
            border-bottom: 4px solid #2E86AB;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }

        .header h1 {
            color: #2E86AB;
            font-size: 28px;
            margin-bottom: 10px;
        }

        .header .subtitle {
            color: #666;
            font-size: 16px;
            font-style: italic;
        }

        .author-info {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 30px;
            border-left: 4px solid #2E86AB;
        }

        .toc-container {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }

        .toc-content {
            max-height: 400px;
            overflow-y: auto;
        }

        .toc-item {
            margin: 8px 0;
            padding: 5px 0;
            border-bottom: 1px solid #eee;
        }

        .toc-item a {
            color: #0066CC !important;
            text-decoration: none;
            font-weight: bold;
            font-size: 14px;
        }

        .toc-item a:hover {
            text-decoration: underline;
        }

        .section {
            margin-bottom: 40px;
            page-break-inside: avoid;
        }

        .section h1 {
            color: #2E86AB;
            border-bottom: 2px solid #2E86AB;
            padding-bottom: 8px;
            margin-top: 30px;
            page-break-after: avoid;
        }

        .section h2 {
            color: #0066CC;
            margin-top: 25px;
            page-break-after: avoid;
        }

        .section h3 {
            color: #333;
            margin-top: 20px;
        }

        .section a {
            color: #0066CC;
            text-decoration: underline;
        }

        .section a:hover {
            color: #004499;
        }

        .code-block {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            padding: 15px;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            overflow-x: auto;
        }

        .table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }

        .table th, .table td {
            border: 1px solid #dee2e6;
            padding: 8px;
            text-align: left;
        }

        .table th {
            background: #f8f9fa;
            font-weight: bold;
        }

        .highlight {
            background: #fff3cd;
            padding: 10px;
            border-left: 4px solid #ffc107;
            margin: 15px 0;
        }

        .footer {
            margin-top: 50px;
            padding-top: 20px;
            border-top: 2px solid #2E86AB;
            text-align: center;
            color: #666;
            font-size: 12px;
        }

        @media print {
            body {
                margin: 0;
                padding: 15mm;
            }

            .toc-item a {
                color: #0066CC !important;
            }

            .section a {
                color: #0066CC !important;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <h1>🏥 STD & HIV Comprehensive Educational Content</h1>
        <div class="subtitle">Complete Medical Education Materials with Interactive Index</div>
    </div>

    <!-- Author Information -->
    <div class="author-info">
        <strong>Author:</strong> Dr. Siddalingaiah H S<br>
        <strong>Position:</strong> Professor, Community Medicine<br>
        <strong>Institution:</strong> SIMSRH, Tumkur<br>
        <strong>Email:</strong> hssling@yahoo.com<br>
        <strong>Phone:</strong> +91-8941087719<br>
        <strong>Date:</strong> November 2024<br>
        <strong>License:</strong> MIT License
    </div>

    <!-- Table of Contents will be inserted here -->

    <!-- Content Sections will be inserted here -->

    <!-- Footer -->
    <div class="footer">
        <p>This comprehensive document contains all educational materials for STD & HIV medical education.</p>
        <p>Generated automatically from source markdown files. All hyperlinks are functional for navigation.</p>
        <p>© 2024 Dr. Siddalingaiah H S - SIMSRH, Tumkur</p>
    </div>
</body>
</html>"""

        # Generate content sections
        content_sections = []
        toc_sections = []

        for file_path in self.content_files:
            if os.path.exists(file_path):
                title, html_content = self.read_markdown_file(file_path)

                # Create anchor from filename
                anchor = re.sub(r'[^\w\-]', '_', file_path.replace('/', '_').replace('\\', '_'))

                # Add to TOC
                toc_sections.append({
                    'title': title,
                    'anchor': anchor
                })

                # Create section HTML
                section_html = f"""
                <div class="section" id="{anchor}">
                    <h1>{title}</h1>
                    <div class="content">
                        {html_content}
                    </div>
                </div>
                """

                content_sections.append(section_html)
            else:
                print(f"⚠️ File not found: {file_path}")

        # Generate TOC
        toc_html = self.generate_table_of_contents(toc_sections)

        # Combine everything
        final_html = html_template.replace("<!-- Table of Contents will be inserted here -->", toc_html)
        final_html = final_html.replace("<!-- Content Sections will be inserted here -->",
                                       "\n".join(content_sections))

        return final_html

    def save_html_file(self, html_content: str) -> bool:
        """
        Save HTML content to temporary file

        Args:
            html_content: HTML string to save

        Returns:
            True if successful
        """
        try:
            with open(self.temp_html, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✅ HTML file saved: {self.temp_html}")
            return True
        except Exception as e:
            print(f"❌ Error saving HTML file: {e}")
            return False

    def generate_pdf_from_html(self) -> bool:
        """
        Generate PDF from HTML using available libraries

        Returns:
            True if successful
        """
        if not os.path.exists(self.temp_html):
            print(f"❌ Error: {self.temp_html} not found!")
            return False

        print("🔄 Generating comprehensive PDF...")

        success = False

        # Method 1: Try weasyprint (most reliable for complex HTML)
        try:
            from weasyprint import HTML, CSS
            print("📄 Using weasyprint for PDF generation...")

            # Custom CSS for PDF generation
            css = CSS(string="""
                @page {
                    size: A4;
                    margin: 20mm;
                }

                a {
                    color: #0066CC !important;
                    text-decoration: underline;
                }

                .toc-item a {
                    color: #0066CC !important;
                    text-decoration: none;
                }
            """)

            html_doc = HTML(filename=self.temp_html)
            html_doc.write_pdf(self.output_pdf, stylesheets=[css])

            success = True
            print(f"✅ PDF generated successfully: {self.output_pdf}")

        except ImportError:
            print("⚠️ weasyprint not available, trying alternative methods...")
        except Exception as e:
            print(f"⚠️ weasyprint failed: {e}")

        # Method 2: Try pdfkit
        if not success:
            try:
                import pdfkit
                print("📄 Using pdfkit for PDF generation...")

                options = {
                    'page-size': 'A4',
                    'margin-top': '20mm',
                    'margin-right': '20mm',
                    'margin-bottom': '20mm',
                    'margin-left': '20mm',
                    'encoding': 'UTF-8',
                    'enable-local-file-access': None,
                    'print-media-type': None,
                    'disable-smart-shrinking': None,
                    'zoom': '1.0'
                }

                pdfkit.from_file(self.temp_html, self.output_pdf, options=options)
                success = True
                print(f"✅ PDF generated successfully: {self.output_pdf}")

            except ImportError:
                print("⚠️ pdfkit not available")
            except Exception as e:
                print(f"⚠️ pdfkit failed: {e}")

        # Method 3: Try xhtml2pdf
        if not success:
            try:
                from xhtml2pdf import pisa
                print("📄 Using xhtml2pdf for PDF generation...")

                with open(self.temp_html, 'r', encoding='utf-8') as f:
                    html_content = f.read()

                with open(self.output_pdf, 'wb') as f:
                    pisa.CreatePDF(html_content, dest=f)

                success = True
                print(f"✅ PDF generated successfully: {self.output_pdf}")

            except ImportError:
                print("⚠️ xhtml2pdf not available")
            except Exception as e:
                print(f"⚠️ xhtml2pdf failed: {e}")

        if not success:
            print("❌ No PDF generation library available!")
            print("\n📦 Install PDF generation libraries:")
            print("   pip install weasyprint     # Recommended")
            print("   pip install pdfkit         # Requires wkhtmltopdf")
            print("   pip install xhtml2pdf      # Alternative")
            return False

        # Verify PDF was created
        if os.path.exists(self.output_pdf):
            file_size = os.path.getsize(self.output_pdf) / (1024 * 1024)  # MB
            print(f"📊 PDF size: {file_size:.1f} MB")
            return True
        else:
            print("❌ PDF file was not created!")
            return False

    def cleanup_temp_files(self):
        """
        Clean up temporary HTML file
        """
        if os.path.exists(self.temp_html):
            try:
                os.remove(self.temp_html)
                print(f"🧹 Cleaned up temporary file: {self.temp_html}")
            except Exception as e:
                print(f"⚠️ Could not remove temp file: {e}")

    def compile_comprehensive_pdf(self) -> bool:
        """
        Main method to compile all content into comprehensive PDF

        Returns:
            True if successful
        """
        print("🏥 STD & HIV Educational Content - Comprehensive PDF Compiler")
        print("=" * 70)

        try:
            # Check if required files exist
            missing_files = [f for f in self.content_files if not os.path.exists(f)]
            if missing_files:
                print("⚠️ Warning: Some content files not found:")
                for file in missing_files:
                    print(f"   - {file}")
                print("   Continuing with available files...\n")

            # Generate comprehensive HTML
            print("📝 Generating comprehensive HTML content...")
            html_content = self.create_comprehensive_html()

            # Save HTML file
            if not self.save_html_file(html_content):
                return False

            # Generate PDF
            if not self.generate_pdf_from_html():
                return False

            # Cleanup
            self.cleanup_temp_files()

            print("\n🎉 Success! Comprehensive PDF created successfully.")
            print(f"   📄 Output: {self.output_pdf}")
            print("   🔗 Contains blue hyperlinked table of contents")
            print("   📚 Includes all educational materials")

            return True

        except Exception as e:
            print(f"❌ Error during compilation: {e}")
            self.cleanup_temp_files()
            return False

def main():
    """
    Main function
    """
    compiler = ComprehensivePDFCompiler()
    success = compiler.compile_comprehensive_pdf()

    if not success:
        print("\n📋 Troubleshooting:")
        print("1. Ensure all required Python packages are installed")
        print("2. Check that markdown files exist in the project directory")
        print("3. Verify write permissions for output directory")
        print("\n📦 Required packages:")
        print("   pip install markdown beautifulsoup4 weasyprint")
        print("   # OR: pip install markdown beautifulsoup4 pdfkit")
        print("   # OR: pip install markdown beautifulsoup4 xhtml2pdf")

        sys.exit(1)

if __name__ == "__main__":
    main()
