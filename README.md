# STD & HIV Educational Content Project

An interactive educational platform providing comprehensive teaching materials for Sexually Transmitted Diseases (STD) and Human Immunodeficiency Virus (HIV) education.

## 📋 Overview

This project contains educational materials designed for medical students, healthcare professionals, and public health educators. The content includes:

- **PowerPoint Presentations**: Detailed lecture slides for STD and HIV classes
- **Interactive Quizzes**: Multiple-choice question assessments
- **Video Scripts**: Structured content for video-based learning
- **Visual Assets**: Charts, diagrams, and infographics
- **Teaching Scripts**: One-hour class scripts for practical implementation

## 🎯 Features

- **Comprehensive Coverage**: STD classification, HIV progression, prevention strategies
- **Visual Learning**: Integrated charts, timelines, and epidemiological data
- **Assessment Tools**: MCQ quizzes for knowledge evaluation
- **Flexible Delivery**: PPTX, video scripts, and web dashboard formats
- **Medical Accuracy**: Content validated for healthcare education

## 📁 Project Structure

```
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore rules
├── app.py                            # Streamlit dashboard
├── STD_and_HIV_TLM.md                # Main teaching learning material
├── create_visual_assets.py           # Visual asset generation script
├── create_std_pptx.py                # STD presentation generator
├── create_hiv_pptx.py                # HIV presentation generator
├── create_std_pptx_with_images.py    # STD presentation with visuals
├── create_hiv_pptx_with_images.py    # HIV presentation with visuals
├── STD_Class_MCQ_Quiz.py             # STD assessment quiz
├── HIV_Class_MCQ_Quiz.py             # HIV assessment quiz
├── STD_Class_Video_Script.md         # STD video content
├── HIV_Class_Video_Script.md         # HIV video content
├── STD_Class_Visualizations.md       # STD visual guides
├── HIV_Class_Visualizations.md       # HIV visual guides
├── STD_One_Hour_Class_Script.md      # STD class script
├── HIV_One_Hour_Class_Script.md      # HIV class script
├── Visual_Assets_Guide.md            # Asset creation guide
├── *.pptx                           # PowerPoint presentations
└── *.png                            # Visual assets and charts
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager
- Docker (optional, for containerized deployment)

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd std-hiv-educational-content
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit dashboard:
```bash
streamlit run app.py
```

### Docker Deployment

```bash
# Build and run with Docker
docker build -t std-hiv-app .
docker run -p 8501:8501 std-hiv-app

# Or use docker-compose
docker-compose up -d
```

### Cloud Deployment

The application can be deployed to multiple cloud platforms:

- **Streamlit Cloud** (Recommended): Connect your GitHub repository
- **Heroku**: Add `Procfile` and deploy
- **AWS/GCP/Azure**: Use containerized deployment
- **GitHub Pages**: Static export for documentation

See [Deployment Guide](docs/deployment.md) for detailed instructions.

## 📖 Content Modules

### STD Education Module
- **Classification & Epidemiology**: Comprehensive STD categorization
- **Clinical Presentation**: Symptoms and diagnostic criteria
- **Management Strategies**: Treatment protocols and guidelines
- **Prevention**: Public health approaches and interventions

### HIV Education Module
- **Virology & Pathogenesis**: HIV lifecycle and disease progression
- **Clinical Stages**: CD4 monitoring and ART initiation
- **Antiretroviral Therapy**: Regimen selection and monitoring
- **Prevention**: U=U messaging and PrEP strategies

## 🛠️ Usage

### For Educators
1. Use PowerPoint presentations for classroom teaching
2. Implement quiz assessments for student evaluation
3. Follow video scripts for multimedia content creation
4. Access web dashboard for interactive learning

### For Developers
- Modify Python scripts to customize content
- Extend Streamlit app with additional features
- Generate new visual assets using provided tools

## 📊 Interactive Dashboard

The Streamlit web application provides:
- **Content Browser**: Navigate through all educational materials
- **Quiz Interface**: Interactive assessment tools
- **Visual Gallery**: Display of charts and infographics
- **Script Viewer**: Formatted display of teaching scripts

## � PDF Index

A comprehensive hypertext PDF index has been created for easy navigation and reference:

### Features
- **Blue-themed professional design** optimized for printing
- **Interactive HTML version** (`index.html`) with working hyperlinks
- **PDF generation script** (`generate_pdf_index.py`) for automated conversion
- **Complete content catalog** with descriptions and access links
- **Statistics overview** showing content metrics
- **Quick navigation** with anchor links to sections

### PDF Generation Options

**Automatic Generation:**
```bash
python generate_pdf_index.py
```

**Manual Generation:**
1. Open `index.html` in web browser
2. Print to PDF (Ctrl+P / Cmd+P)
3. Select A4 paper size with narrow margins
4. Enable background graphics
5. Save as `STD_HIV_Educational_Index.pdf`

**Requirements for Automatic PDF:**
```bash
pip install weasyprint  # Recommended
# OR
pip install pdfkit      # Requires wkhtmltopdf
# OR
pip install pyppeteer   # Requires Chromium
# OR
pip install xhtml2pdf   # Uses ReportLab
```

## �🔄 CI/CD Pipeline

This project includes automated testing and deployment pipelines:

### GitHub Actions Workflow
- **Multi-Python Version Testing**: Tests on Python 3.8, 3.9, 3.10, 3.11
- **Code Quality Checks**: Linting with flake8, formatting with black, import sorting with isort
- **Type Checking**: Static type analysis with mypy
- **Docker Build**: Automated container image building and testing
- **Deployment**: Automatic deployment to configured platforms

### Quality Gates
- All tests must pass
- Code coverage requirements met
- No linting errors
- Type checking passes
- Docker build succeeds

See `.github/workflows/ci.yml` for complete pipeline configuration.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes and ensure tests pass
4. Run code quality checks: `flake8 . && black --check . && isort --check-only .`
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

See [Development Guide](docs/development.md) for detailed contribution guidelines.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

### **Dr. Siddalingaiah H S**
**Professor, Community Medicine**  
**SIMSRH**  
**Tumkur, Karnataka, India**  

**Contact Information:**
- 📧 Email: hssling@yahoo.com
- 📱 Phone: +91 8941087719

**Academic Background:**
- MBBS, MD (Community Medicine)
- Extensive experience in medical education and public health
- Special interest in STD/HIV prevention and control

**Professional Contributions:**
- Development of innovative teaching methodologies
- Research in community-based health interventions
- Training programs for healthcare professionals
- Educational content creation for medical students

### **Technical Implementation**
- **Content Generation**: Python-based automated content creation
- **Web Development**: Streamlit dashboard for interactive learning
- **Documentation**: Comprehensive technical and deployment guides
- **CI/CD Pipeline**: Automated testing and deployment workflows

## 🙏 Acknowledgments

- Medical content validated for educational accuracy
- Visual assets designed for clarity and engagement
- Built with educational best practices in mind

## 📞 Support

For questions or support regarding the educational content, please refer to the teaching scripts and documentation within the project files.

