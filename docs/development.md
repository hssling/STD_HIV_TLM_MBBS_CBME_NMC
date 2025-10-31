# Development Guide

This guide provides instructions for developers working on the STD & HIV Educational Dashboard.

## 🛠️ Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Docker (optional, for containerized development)

### Local Development Environment

1. **Clone the repository:**
```bash
git clone <repository-url>
cd std-hiv-educational-content
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Install development dependencies:**
```bash
pip install pytest pytest-cov flake8 black isort mypy pre-commit
```

5. **Set up pre-commit hooks:**
```bash
pre-commit install
```

6. **Run the application:**
```bash
streamlit run app.py
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_app.py
```

### Code Quality Checks
```bash
# Linting
flake8 .

# Code formatting
black --check --diff .
isort --check-only --diff .

# Type checking
mypy app.py --ignore-missing-imports
```

### Writing Tests
```python
# Example test structure
import pytest
from app import load_file_content

def test_load_file_content():
    """Test file content loading functionality."""
    content = load_file_content("README.md")
    assert isinstance(content, str)
    assert len(content) > 0

def test_quiz_functionality():
    """Test quiz system integration."""
    # Add quiz tests here
    pass
```

## 📝 Code Style Guidelines

### Python Style
- Follow PEP 8 conventions
- Use type hints for function parameters and return values
- Maximum line length: 88 characters (Black default)
- Use docstrings for all functions and classes

### Import Organization
```python
# Standard library imports
import os
import sys
from pathlib import Path

# Third-party imports
import streamlit as st
import matplotlib.pyplot as plt

# Local imports
from .utils import helper_function
```

### Naming Conventions
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`
- Files: `snake_case.py`

## 🏗️ Project Structure

```
├── app.py                          # Main application
├── create_*.py                     # Content generation scripts
├── *_Quiz.py                       # Quiz implementations
├── tests/                          # Test files
│   ├── __init__.py
│   ├── test_app.py
│   └── test_quiz.py
├── docs/                           # Documentation
│   ├── api.md
│   ├── deployment.md
│   └── development.md
├── .github/                        # GitHub configuration
│   └── workflows/
│       └── ci.yml
├── requirements.txt                # Production dependencies
├── requirements-dev.txt            # Development dependencies
├── Dockerfile                      # Container configuration
├── docker-compose.yml              # Local development setup
├── .pre-commit-config.yaml         # Pre-commit hooks
└── pyproject.toml                  # Python project configuration
```

## 🔧 Configuration Files

### pyproject.toml
```toml
[tool.black]
line-length = 88
target-version = ['py38', 'py39', 'py310', 'py311']

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

## 🚀 Deployment

### Local Testing
```bash
# Test Docker build
docker build -t std-hiv-app .

# Run container locally
docker run -p 8501:8501 std-hiv-app

# Test with docker-compose
docker-compose up
```

### Production Deployment
See `docs/deployment.md` for detailed deployment instructions.

## 📊 Content Development

### Adding New Educational Content

1. **Create content script:**
```python
# create_new_module.py
from pptx import Presentation

def create_new_module_presentation():
    prs = Presentation()
    # Add slides...
    prs.save('New_Module_Presentation.pptx')
```

2. **Update Streamlit app:**
```python
# Add to app.py
def display_new_module():
    st.markdown("## New Educational Module")
    # Add content display logic
```

3. **Add to navigation:**
```python
# Update sidebar navigation
page = st.radio(
    "Navigate to:",
    ["🏠 Home", "📚 STD Module", "🩺 HIV Module", "🆕 New Module", ...]
)
```

### Adding Quiz Questions

1. **Update quiz script:**
```python
# Add to STD_Class_MCQ_Quiz.py or HIV_Class_MCQ_Quiz.py
{
    "question": "New question text?",
    "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
    "answer": "A",
    "explanation": "Explanation for the correct answer."
}
```

2. **Test quiz integration:**
```bash
python -c "from STD_Class_MCQ_Quiz import STDQuiz; quiz = STDQuiz(); print(f'Total questions: {len(quiz.questions)}')"
```

## 🎨 Visual Assets

### Creating New Charts
```python
# Add to create_visual_assets.py
def create_new_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    # Create visualization
    plt.savefig('new_chart.png', dpi=300, bbox_inches='tight')
    plt.close()
```

### Design Guidelines
- Use consistent color scheme
- Ensure readability
- Include proper labels and legends
- Optimize for web display (300 DPI)

## 🔒 Security Considerations

### Code Security
- Validate all user inputs
- Use parameterized queries for database operations
- Implement proper error handling
- Avoid exposing sensitive information

### Content Security
- Ensure medical accuracy of content
- Cite reliable sources
- Regular content updates based on latest guidelines
- Privacy protection for any user data

## 📈 Performance Optimization

### Streamlit Best Practices
```python
# Cache expensive operations
@st.cache_data
def load_large_content():
    return expensive_operation()

# Use session state for user data
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Optimize images
st.image('chart.png', use_column_width=True)
```

### Memory Management
- Clear large objects after use
- Use generators for large datasets
- Implement pagination for long content

## 🤝 Contributing

### Pull Request Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes and add tests
4. Ensure all tests pass and code quality checks pass
5. Update documentation if needed
6. Commit changes (`git commit -m 'Add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Commit Message Guidelines
```
type(scope): description

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes
- refactor: Code refactoring
- test: Test additions
- chore: Maintenance tasks
```

## 🐛 Debugging

### Common Issues
- **Import errors:** Check virtual environment activation
- **Port conflicts:** Change Streamlit port in configuration
- **Memory issues:** Monitor with `docker stats` or system tools
- **File not found:** Check file paths and working directory

### Debug Mode
```bash
# Run with debug logging
streamlit run app.py --logger.level=debug

# Enable Streamlit debug menu
# Add to app.py
st.sidebar.checkbox("Debug mode", key="debug")
if st.session_state.debug:
    st.write(st.session_state)
```

## 📚 Resources

### Learning Resources
- [Streamlit Documentation](https://docs.streamlit.io)
- [Python Best Practices](https://python-guide.org)
- [Medical Education Guidelines](https://www.who.int/health-topics/medical-education)

### Tools and Libraries
- **Testing:** pytest, coverage.py
- **Code Quality:** flake8, black, isort, mypy
- **CI/CD:** GitHub Actions
- **Containerization:** Docker, docker-compose
