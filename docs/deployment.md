# Deployment Guide

**Author:** Dr. Siddalingaiah H S, Professor, Community Medicine, SIMSRH, Tumkur
**Email:** hssling@yahoo.com | **Phone:** +91-8941087719
**Date:** November 2024
**License:** MIT License

This guide covers various deployment options for the STD & HIV Educational Dashboard.

## 🚀 Quick Start

### Local Development
```bash
# Clone the repository
git clone <repository-url>
cd std-hiv-educational-content

# Install dependencies
pip install -r requirements.txt

# Run the application
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

## ☁️ Cloud Deployment Options

### 1. Streamlit Cloud (Recommended)
1. Fork this repository on GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select the repository and main file (`app.py`)
5. Deploy!

### 2. Heroku
```bash
# Create requirements.txt with gunicorn
echo "gunicorn==20.1.0" >> requirements.txt

# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.headless=true" > Procfile

# Deploy
git push heroku main
```

### 3. AWS EC2
```bash
# On EC2 instance
sudo apt update
sudo apt install python3-pip nginx

# Install dependencies
pip3 install -r requirements.txt

# Configure nginx (see nginx.conf)
sudo cp nginx.conf /etc/nginx/sites-available/std-hiv-app
sudo ln -s /etc/nginx/sites-available/std-hiv-app /etc/nginx/sites-enabled/

# Start services
sudo systemctl start nginx
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

### 4. Google Cloud Run
```bash
# Build and deploy
gcloud run deploy std-hiv-app \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### 5. Azure App Service
```bash
# Create web app
az webapp up --name std-hiv-app --resource-group myResourceGroup --runtime "PYTHON:3.10"

# Configure deployment
az webapp config set --name std-hiv-app --resource-group myResourceGroup \
  --startup-file "streamlit run app.py --server.port=8000 --server.address=0.0.0.0"
```

## 🔧 Configuration

### Environment Variables
```bash
# Streamlit configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Custom configuration
APP_TITLE="STD & HIV Educational Dashboard"
MAX_UPLOAD_SIZE=50  # MB
```

### Custom Domain
1. Update `CNAME` file with your domain
2. Configure DNS to point to deployment platform
3. Update CORS settings if needed

## 📊 Monitoring & Analytics

### Basic Monitoring
```python
# Add to app.py for basic analytics
import streamlit_analytics
streamlit_analytics.start_tracking()
```

### Health Checks
- Application health: `GET /health`
- Docker health: Built-in health checks
- Uptime monitoring: Use services like UptimeRobot

## 🔒 Security Considerations

### HTTPS
- Always use HTTPS in production
- Configure SSL certificates
- Use security headers

### Access Control
```python
# Basic authentication
import streamlit_authenticator as stauth

# Configure authentication
config = {...}  # User credentials
authenticator = stauth.Authenticate(config, ...)
```

### Data Protection
- No sensitive medical data stored
- Educational content only
- Regular security updates

## 🚀 Performance Optimization

### Streamlit Optimization
```python
# Add to app.py
st.set_page_config(
    page_title="STD & HIV Education",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Cache expensive operations
@st.cache_data
def load_content():
    return expensive_operation()
```

### CDN for Static Assets
- Host images on CDN
- Use web-optimized formats
- Implement lazy loading

## 🐛 Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Find process using port
lsof -i :8501
# Kill process
kill -9 <PID>
```

**Memory issues:**
```bash
# Monitor memory usage
docker stats
# Increase container memory
docker run --memory=2g std-hiv-app
```

**Import errors:**
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

## 📈 Scaling

### Horizontal Scaling
- Use load balancer
- Multiple container instances
- Session state management

### Database Integration
For user progress tracking:
```python
# Add database support
import sqlite3

def init_db():
    conn = sqlite3.connect('user_progress.db')
    # Create tables for quiz results, user sessions, etc.
```

## 🔄 CI/CD Integration

The project includes GitHub Actions for automated:
- Testing (multiple Python versions)
- Linting (flake8, black, isort)
- Type checking (mypy)
- Docker building
- Deployment to multiple platforms

See `.github/workflows/ci.yml` for details.
