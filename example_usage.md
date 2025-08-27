# Image to HTML Converter - Usage Examples

This script converts images to HTML files with three different embedding methods.

## Basic Usage

### Convert an image to responsive HTML (default)
```bash
python image_to_html.py path/to/your/image.jpg
```

### Convert with custom title
```bash
python image_to_html.py path/to/your/image.jpg -t "My Custom Title"
```

### Convert with specific output file
```bash
python image_to_html.py path/to/your/image.jpg -o "my_report.html"
```

## Different Modes

### 1. Responsive Mode (Default)
Creates a professional, responsive HTML page with the image embedded as base64:
```bash
python image_to_html.py image.png -m responsive
```

### 2. Base64 Mode
Creates simple HTML with the image embedded as base64 (self-contained):
```bash
python image_to_html.py image.png -m base64
```

### 3. Reference Mode
Creates HTML that references the image file (keeps files separate):
```bash
python image_to_html.py image.png -m reference
```

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- WebP (.webp)
- SVG (.svg)

## Examples for Your ReportingAsCode Project

### Create a report template with embedded image
```bash
python image_to_html.py chart.png -t "Q4 Sales Chart" -o "sales_report.html"
```

### Create multiple report sections
```bash
python image_to_html.py dashboard.png -t "Executive Dashboard" -o "dashboard_section.html"
python image_to_html.py metrics.png -t "Key Metrics" -o "metrics_section.html"
```

### Create a self-contained report (base64 mode)
```bash
python image_to_html.py logo.png -m base64 -t "Company Logo" -o "logo_section.html"
```

## Command Line Options

- `image_path`: Path to the input image file (required)
- `-o, --output`: Output HTML file path (optional, auto-generated if not specified)
- `-t, --title`: Title for the HTML page (default: "Image Display")
- `-m, --mode`: HTML generation mode: base64, reference, or responsive (default: responsive)

## Output

The script will create an HTML file that you can:
- Open in any web browser
- Include in your report generation workflow
- Use as a template for further customization
- Embed in other HTML documents
