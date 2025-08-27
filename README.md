# ReportingAsCode
Creating a report template based on HTML files to allow report generation programmatically

## Features

### 1. Beacon Monthly Report Generator
Generate professional HTML reports from JSON configuration:

- **Dynamic Content**: All report content is configurable via JSON
- **Professional Styling**: Modern, responsive design with gradients and animations
- **Easy Updates**: Change values without editing HTML directly

#### Quick Start
```bash
# Generate report from JSON configuration
python3 generate_report.py

# The script reads "Input Values.json" and creates "beacon_monthly_report_generated.html"
```

#### Configuration
Edit `Input Values.json` to customize:
- Report metadata (title, month, company logo)
- Metrics (views, users, catalog items)
- User quotes and attribution
- Division chart data and colors
- Highlights and upcoming features
- Styling preferences

### 2. Image to HTML Converter
Convert images to HTML files with multiple embedding options:

- **Responsive Mode**: Professional, responsive HTML with embedded images (default)
- **Base64 Mode**: Simple HTML with base64 encoded images (self-contained)
- **Reference Mode**: HTML that references image files (keeps files separate)

#### Quick Start
```bash
# Convert image to responsive HTML
python3 image_to_html.py your_image.png

# Convert with custom title and output
python3 image_to_html.py chart.png -t "Q4 Sales Chart" -o "sales_report.html"

# Use different modes
python3 image_to_html.py logo.png -m base64    # Self-contained
python3 image_to_html.py chart.png -m reference # File reference
```

#### Supported Formats
- JPEG, PNG, GIF, BMP, WebP, SVG

#### Use Cases
- Create report templates with embedded images
- Generate self-contained HTML reports
- Build image galleries for reports
- Convert charts and diagrams to web format
