# API Documentation

This document describes the internal API and functions available in the STD & HIV Educational Dashboard.

## 🏗️ Application Structure

### Main Application (`app.py`)

#### Core Functions

##### `load_file_content(file_path: str) -> str`
Loads content from a markdown or text file.

**Parameters:**
- `file_path` (str): Path to the file to load

**Returns:**
- `str`: File content as string, or error message if loading fails

**Example:**
```python
content = load_file_content("STD_One_Hour_Class_Script.md")
st.markdown(content)
```

##### `run_quiz_script(script_name: str) -> dict`
Runs a quiz script and returns results (placeholder for future integration).

**Parameters:**
- `script_name` (str): Name of the quiz script to run

**Returns:**
- `dict`: Dictionary containing quiz results

#### Page Functions

##### `display_home_page()`
Renders the main dashboard home page with overview and statistics.

##### `display_std_module()`
Displays the STD education module with tabs for different content types.

##### `display_hiv_module()`
Displays the HIV education module with tabs for different content types.

##### `display_quiz_section()`
Shows the interactive quiz interface with multiple quiz modes.

##### `display_quiz_interface()`
Handles the active quiz session and question display.

##### `display_visual_assets()`
Shows the gallery of visual assets and charts.

##### `display_documentation()`
Displays documentation and reference materials.

## 📊 Quiz System

### STD Quiz (`STD_Class_MCQ_Quiz.py`)

#### Class: `STDQuiz`

##### `__init__()`
Initializes the quiz with questions and scoring.

##### `load_questions() -> List[Dict]`
Loads all STD-related MCQ questions.

**Returns:**
- `List[Dict]`: List of question dictionaries with keys: 'question', 'options', 'answer', 'explanation'

##### `shuffle_questions() -> None`
Randomizes the order of questions.

##### `ask_question(question_data: Dict, question_number: int) -> bool`
Presents a single question and gets user response.

**Parameters:**
- `question_data` (Dict): Question dictionary
- `question_number` (int): Current question number

**Returns:**
- `bool`: True if answered within time limit

##### `run_quiz(num_questions: int = None) -> None`
Runs the complete quiz session.

**Parameters:**
- `num_questions` (int, optional): Number of questions to ask

##### `show_results(total_asked: int) -> None`
Displays final quiz results and performance feedback.

**Parameters:**
- `total_asked` (int): Total number of questions asked

### HIV Quiz (`HIV_Class_MCQ_Quiz.py`)

Similar structure to STD Quiz but with HIV-specific questions.

## 🎨 Visual Assets Generation (`create_visual_assets.py`)

### Chart Generation Functions

##### `create_std_classification_diagram()`
Creates STD classification flowchart using matplotlib.

##### `create_global_std_epidemiology_chart()`
Generates global STD burden bar chart.

##### `create_indian_hiv_transmission_pie()`
Creates pie chart showing HIV transmission routes in India.

##### `create_hiv_progression_timeline()`
Generates HIV disease progression timeline visualization.

##### `create_art_regimen_comparison()`
Creates comparison chart of ART regimens.

##### `create_prevention_pyramid()`
Generates HIV prevention pyramid diagram.

##### `create_u_equals_u_symbol()`
Creates U=U (Undetectable = Untransmittable) symbol.

##### `create_abc_icons()`
Generates ABC approach prevention icons.

##### `create_cd4_monitoring_chart()`
Creates CD4 count monitoring chart.

## 📊 Presentation Generation

### STD Presentation (`create_std_pptx_with_images.py`)

#### `create_std_presentation_with_images()`
Generates comprehensive STD PowerPoint presentation with embedded images.

**Content Sections:**
1. Title Slide
2. STD Definition & Classification
3. Epidemiology (Global & Indian)
4. Transmission Routes
5. Bacterial STDs (Gonorrhea, Syphilis, Chlamydia)
6. Viral STDs Overview
7. Diagnosis & Laboratory Tests
8. Treatment Guidelines
9. Prevention Strategies
10. Challenges & Future Directions

### HIV Presentation (`create_hiv_pptx_with_images.py`)

#### `create_hiv_presentation_with_images()`
Generates comprehensive HIV PowerPoint presentation with embedded images.

**Content Sections:**
1. Title Slide
2. HIV Virology & Pathogenesis
3. Epidemiology & Transmission
4. Clinical Stages & CD4 Monitoring
5. ART Guidelines & Regimens
6. Prevention Strategies (PrEP, PEP, U=U)
7. National Programs & Guidelines
8. Future Directions

## 🔧 Configuration

### Streamlit Configuration
```python
st.set_page_config(
    page_title="STD & HIV Educational Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

### Custom CSS Classes
- `.main-header`: Main page header styling
- `.module-card`: Content module cards
- `.content-section`: Content display sections
- `.quiz-result`: Quiz result feedback styling
- `.sidebar-header`: Sidebar header styling

## 📁 File Structure

```
├── app.py                          # Main Streamlit application
├── create_*.py                     # Content generation scripts
├── *_Quiz.py                       # Interactive quiz scripts
├── *.pptx                          # Generated presentations
├── *.png                           # Visual assets
├── *.md                            # Documentation files
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker configuration
├── docker-compose.yml              # Docker Compose setup
├── .github/workflows/ci.yml        # CI/CD pipeline
└── docs/                           # Documentation
    ├── deployment.md               # Deployment guide
    └── api.md                      # This API documentation
```

## 🔌 Dependencies

### Core Dependencies
- `streamlit`: Web application framework
- `python-pptx`: PowerPoint presentation creation
- `matplotlib`: Chart and visualization creation
- `seaborn`: Statistical visualization enhancements
- `numpy`: Numerical computing

### Development Dependencies
- `pytest`: Testing framework
- `flake8`: Code linting
- `black`: Code formatting
- `isort`: Import sorting
- `mypy`: Type checking

## 🚀 Deployment API

### Docker Configuration
```yaml
# docker-compose.yml services
std-hiv-app:
  build: .
  ports:
    - "8501:8501"
  environment:
    - STREAMLIT_SERVER_HEADLESS=true
```

### Environment Variables
- `STREAMLIT_SERVER_PORT`: Server port (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: 0.0.0.0)
- `STREAMLIT_SERVER_HEADLESS`: Headless mode for deployment

## 📊 Data Models

### Question Data Structure
```python
{
    "question": "Question text",
    "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
    "answer": "A",
    "explanation": "Explanation text"
}
```

### Quiz Results Structure
```python
{
    "score": 85,
    "total": 100,
    "percentage": 85.0,
    "feedback": "Very Good! Well done!"
}
```

## 🔄 Integration Points

### Future Enhancements
- Database integration for user progress tracking
- API endpoints for external integrations
- Authentication system for user management
- Analytics and usage tracking
- Multi-language support

### External APIs
- Potential integration with medical databases
- Quiz result export functionality
- Content management system integration
