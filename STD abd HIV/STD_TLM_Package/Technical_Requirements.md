# Technical Requirements for STD TLM Package

## System Requirements

### Minimum Hardware Specifications
- Processor: Intel Core i3 or equivalent (2.0 GHz or higher)
- RAM: 4 GB minimum, 8 GB recommended
- Storage: 500 MB free space for package installation
- Display: 1024x768 resolution minimum
- Internet: Required for interactive web-based materials

### Recommended Hardware Specifications
- Processor: Intel Core i5 or equivalent (2.5 GHz or higher)
- RAM: 8 GB or higher
- Storage: 1 GB free space
- Display: 1920x1080 resolution or higher
- Internet: Broadband connection for optimal performance

## Software Dependencies

### Required Software
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: Version 3.7 or higher
- **Web Browser**: Modern browser with JavaScript enabled
  - Google Chrome 80+
  - Mozilla Firefox 75+
  - Microsoft Edge 80+
  - Safari 13+ (macOS only)

### Optional Software
- **Microsoft PowerPoint**: For editing presentation files
- **PDF Reader**: Adobe Acrobat Reader or equivalent
- **Code Editor**: VS Code, PyCharm, or similar for customization

## Python Dependencies

### Core Dependencies (install via pip)
```
matplotlib>=3.3.0
pandas>=1.2.0
numpy>=1.19.0
streamlit>=0.80.0 (optional, for enhanced interactive features)
```

### Installation Instructions
1. Ensure Python 3.7+ is installed
2. Install required packages:
   ```bash
   pip install matplotlib pandas numpy
   ```
3. For interactive features:
   ```bash
   pip install streamlit
   ```

## Web Technologies

### Supported Browsers
- HTML5 compatible browsers
- CSS3 support for styling
- JavaScript ES6+ support
- Local file access enabled (for offline use)

### Browser Settings
- Enable JavaScript
- Allow pop-ups (if required by interactive elements)
- Enable local file access for HTML files
- Disable browser extensions that may interfere

## File Formats

### Supported Formats
- **Documents**: Markdown (.md), PDF
- **Presentations**: PowerPoint (.pptx)
- **Images**: PNG, JPG, SVG
- **Scripts**: Python (.py), HTML (.html)
- **Data**: CSV, JSON

### Compatibility Notes
- All files are cross-platform compatible
- UTF-8 encoding for text files
- Relative paths used for internal linking

## Network Requirements

### Online Features
- Interactive web materials require internet for:
  - External libraries (CDN hosted)
  - Analytics (optional)
  - Updates and support

### Offline Usage
- All materials can be used offline
- Local web server may be needed for some interactive features
- Download external dependencies for offline use

## Installation and Setup

### Package Installation
1. Extract the TLM package to a local directory
2. Ensure write permissions for the directory
3. Run setup scripts if provided
4. Test all components in target environment

### Environment Testing
1. Open HTML files in supported browser
2. Run Python scripts to verify dependencies
3. Open presentations in compatible software
4. Test interactive elements functionality

## Troubleshooting

### Common Issues
- **Python scripts fail**: Check Python version and dependencies
- **HTML files don't load**: Verify browser compatibility
- **Images don't display**: Check file paths and permissions
- **Presentations corrupted**: Use compatible PowerPoint version

### Support Resources
- Check implementation guide for detailed instructions
- Verify system meets minimum requirements
- Test in recommended browser first

## Security Considerations

### Safe Execution
- All scripts are designed for educational use
- No external network calls in core functionality
- Local execution only (no server components)
- No data collection or tracking

### File Permissions
- Read-only access recommended for distribution
- Execute permissions for Python scripts
- Web browser access for HTML files

## Version Compatibility

### Package Version
- Current Version: 1.0
- Compatible Python Versions: 3.7 - 3.11
- Tested on: Windows 10/11, macOS 11/12, Ubuntu 20.04

### Update Policy
- Major updates may require dependency changes
- Backward compatibility maintained where possible
- Update notifications through documentation