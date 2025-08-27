#!/usr/bin/env python3
"""
Image to HTML Converter
Converts images to HTML files with various embedding options.
"""

import base64
import os
import argparse
from pathlib import Path
from typing import Optional


def image_to_base64(image_path: str) -> str:
    """Convert image to base64 string."""
    try:
        with open(image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return encoded_string
    except Exception as e:
        raise Exception(f"Error reading image file: {e}")


def get_image_mime_type(image_path: str) -> str:
    """Get MIME type based on file extension."""
    ext = Path(image_path).suffix.lower()
    mime_types = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.bmp': 'image/bmp',
        '.webp': 'image/webp',
        '.svg': 'image/svg+xml'
    }
    return mime_types.get(ext, 'image/jpeg')


def create_html_with_base64(image_path: str, title: str = "Image Display") -> str:
    """Create HTML with base64 encoded image."""
    try:
        base64_string = image_to_base64(image_path)
        mime_type = get_image_mime_type(image_path)
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }}
        .image-container {{
            text-align: center;
            margin: 20px 0;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .image-info {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            margin-top: 20px;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <div class="image-container">
            <img src="data:{mime_type};base64,{base64_string}" alt="Embedded Image">
        </div>
        <div class="image-info">
            <p><strong>Source:</strong> {os.path.basename(image_path)}</p>
            <p><strong>Type:</strong> {mime_type}</p>
            <p><strong>Embedding:</strong> Base64 encoded (self-contained)</p>
        </div>
    </div>
</body>
</html>"""
        
        return html_content
    except Exception as e:
        raise Exception(f"Error creating HTML with base64: {e}")


def create_html_with_reference(image_path: str, title: str = "Image Display") -> str:
    """Create HTML that references the image file."""
    image_filename = os.path.basename(image_path)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }}
        .image-container {{
            text-align: center;
            margin: 20px 0;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .image-info {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            margin-top: 20px;
            font-size: 14px;
            color: #666;
        }}
        .warning {{
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            color: #856404;
            padding: 15px;
            border-radius: 4px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <div class="image-container">
            <img src="{image_filename}" alt="Referenced Image">
        </div>
        <div class="image-info">
            <p><strong>Source:</strong> {image_filename}</p>
            <p><strong>Embedding:</strong> File reference</p>
        </div>
        <div class="warning">
            <p><strong>Note:</strong> This HTML file references the image file. Make sure the image file is in the same directory as the HTML file for proper display.</p>
        </div>
    </div>
</body>
</html>"""
    
    return html_content


def create_responsive_html(image_path: str, title: str = "Responsive Image Display") -> str:
    """Create HTML with responsive design and multiple image sizes."""
    try:
        base64_string = image_to_base64(image_path)
        mime_type = get_image_mime_type(image_path)
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .header {{
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            font-size: 1.1rem;
            opacity: 0.9;
        }}
        
        .image-card {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        
        .image-container {{
            text-align: center;
            margin: 20px 0;
        }}
        
        .responsive-image {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .responsive-image:hover {{
            transform: scale(1.02);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }}
        
        .image-info {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 20px;
            border-radius: 10px;
            margin-top: 25px;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }}
        
        .info-item {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        
        .info-item strong {{
            color: #667eea;
            display: block;
            margin-bottom: 5px;
        }}
        
        .responsive-features {{
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }}
        
        .features-list {{
            list-style: none;
            padding: 0;
        }}
        
        .features-list li {{
            padding: 8px 0;
            position: relative;
            padding-left: 25px;
        }}
        
        .features-list li:before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: #4caf50;
            font-weight: bold;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 15px;
            }}
            
            .header h1 {{
                font-size: 2rem;
            }}
            
            .image-card {{
                padding: 20px;
            }}
            
            .info-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <p>Professional image display with responsive design</p>
        </div>
        
        <div class="image-card">
            <div class="image-container">
                <img src="data:{mime_type};base64,{base64_string}" 
                     alt="Responsive Image" 
                     class="responsive-image">
            </div>
            
            <div class="image-info">
                <h3>Image Information</h3>
                <div class="info-grid">
                    <div class="info-item">
                        <strong>Filename</strong>
                        {os.path.basename(image_path)}
                    </div>
                    <div class="info-item">
                        <strong>Type</strong>
                        {mime_type}
                    </div>
                    <div class="info-item">
                        <strong>Embedding</strong>
                        Base64 encoded
                    </div>
                    <div class="info-item">
                        <strong>Design</strong>
                        Responsive
                    </div>
                </div>
            </div>
            
            <div class="responsive-features">
                <h3>Responsive Features</h3>
                <ul class="features-list">
                    <li>Automatically scales to fit screen size</li>
                    <li>Mobile-friendly design</li>
                    <li>Smooth hover animations</li>
                    <li>Professional styling</li>
                    <li>Cross-browser compatibility</li>
                    <li>Self-contained (no external dependencies)</li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>"""
        
        return html_content
    except Exception as e:
        raise Exception(f"Error creating responsive HTML: {e}")


def main():
    """Main function to handle command line arguments and conversion."""
    parser = argparse.ArgumentParser(
        description="Convert images to HTML files with various embedding options"
    )
    parser.add_argument("image_path", help="Path to the input image file")
    parser.add_argument(
        "-o", "--output", 
        help="Output HTML file path (default: auto-generated)"
    )
    parser.add_argument(
        "-t", "--title", 
        default="Image Display",
        help="Title for the HTML page (default: 'Image Display')"
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["base64", "reference", "responsive"],
        default="responsive",
        help="HTML generation mode (default: responsive)"
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.image_path):
        print(f"Error: Image file '{args.image_path}' not found.")
        return 1
    
    # Generate output filename if not specified
    if not args.output:
        base_name = Path(args.image_path).stem
        args.output = f"{base_name}.html"
    
    try:
        # Generate HTML based on selected mode
        if args.mode == "base64":
            html_content = create_html_with_base64(args.image_path, args.title)
        elif args.mode == "reference":
            html_content = create_html_with_reference(args.image_path, args.title)
        elif args.mode == "responsive":
            html_content = create_responsive_html(args.image_path, args.title)
        
        # Write HTML file
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Successfully created HTML file: {args.output}")
        print(f"📁 Input image: {args.image_path}")
        print(f"🎨 Mode: {args.mode}")
        print(f"📝 Title: {args.title}")
        
        if args.mode == "reference":
            print("\n⚠️  Note: Make sure the image file is in the same directory as the HTML file.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
