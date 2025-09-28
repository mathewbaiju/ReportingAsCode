#!/usr/bin/env python3
"""
Beacon Monthly Report Generator
Reads Input Values.json and generates the HTML report dynamically.
"""

import json
import os
from pathlib import Path


def load_json_config(json_file_path):
    """Load the JSON configuration file."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise Exception(f"Error loading JSON file: {e}")


def generate_html_report(config):
    """Generate the HTML report from the JSON configuration."""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['report_metadata']['title']} - {config['report_metadata']['month']}</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: {config['styling']['container_max_width']};
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        /* Header */
        .header {{
            background: {config['header_styling']['background_color']};
            color: {config['header_styling']['text_color']};
            padding: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo-section {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        
        .logo {{
            font-size: 24px;
            font-weight: bold;
            background: {config['header_styling']['logo_background']};
            padding: 10px 15px;
            border-radius: 8px;
            border: 1px solid {config['header_styling']['logo_border']};
        }}
        
        .report-title {{
            font-size: 28px;
            font-weight: 300;
        }}
        
        .date-badge {{
            background: {config['header_styling']['text_color']};
            color: #333;
            padding: 12px 24px;
            border-radius: 25px;
            font-weight: bold;
            font-size: 18px;
            box-shadow: 0 4px 15px rgba(255,215,0,0.3);
        }}
        
        /* Main Content */
        .main-content {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: {config['styling']['main_content_gap']};
            padding: {config['styling']['main_content_gap']};
            align-items: start;
        }}
        
        .left-column {{
            display: flex;
            flex-direction: column;
            gap: 45px;
            height: fit-content;
            padding-top: 20px;
        }}
        
        .right-column {{
            display: flex;
            flex-direction: column;
            gap: 35px;
            justify-content: flex-start;
            height: fit-content;
        }}
        
        /* Metric Cards */
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: {config['styling']['metrics_grid_gap']};
        }}
        
        .metric-card {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border: 1px solid #e1e8ed;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .metric-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }}
        
        .metric-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 15px;
        }}
        
        .metric-icon {{
            width: 40px;
            height: 40px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }}
        
        .views-icon {{ background: #e3f2fd; color: #1976d2; }}
        .users-icon {{ background: #f3e5f5; color: #7b1fa2; }}
        .items-icon {{ background: #e8f5e8; color: #388e3c; }}
        
        .metric-title {{
            font-size: 16px;
            font-weight: 600;
            color: #555;
        }}
        
        .metric-value {{
            font-size: 32px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }}
        
        .metric-change {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 15px;
        }}
        
        .change-arrow {{
            width: 0;
            height: 0;
            border-left: 8px solid transparent;
            border-right: 8px solid transparent;
            border-bottom: 12px solid #4caf50;
        }}
        
        .change-text {{
            font-size: 16px;
            color: #4caf50;
            font-weight: 700;
        }}
        
        .no-change {{
            background: #f5f5f5;
            color: #666;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
        }}
        
        .metric-description {{
            font-size: 13px;
            color: #666;
            line-height: 1.4;
        }}
        
        /* Chart and User Quotes Container - Side by Side */
        .quotes-chart-container {{
            display: grid;
            grid-template-columns: 1.5fr 1fr;
            gap: {config['styling']['quotes_chart_gap']};
        }}
        
        /* User Quotes Section */
        .quotes-section {{
            background: white;
            border-radius: 15px;
            padding: 25px;
            border: 1px solid #e1e8ed;
        }}
        
        .quotes-title {{
            font-size: 18px;
            font-weight: 600;
            color: #333;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .quote-content {{
            font-style: italic;
            font-size: 15px;
            line-height: 1.6;
            color: #333;
            margin-bottom: 20px;
            background: rgba(255,255,255,0.7);
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #ff9800;
        }}
        
        .quote-attribution {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        
        .profile-pic {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #ff9800;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 16px;
        }}
        
        .attribution-text {{
            font-size: 13px;
            color: #666;
            line-height: 1.4;
        }}
        
        /* Chart Section */
        .chart-section {{
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border: 1px solid #e1e8ed;
        }}
        
        .chart-title {{
            font-size: 18px;
            font-weight: 600;
            color: #333;
            margin-bottom: 20px;
        }}
        
        .chart-container {{
            display: flex;
            align-items: center;
            gap: 30px;
        }}
        
        .pie-chart {{
            width: 320px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        
        .pie-container {{
            position: relative;
            width: 200px;
            height: 200px;
            border-radius: 50%;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }}
        
        .pie-slice {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            clip-path: polygon(50% 50%, 50% 0%, 100% 0%, 100% 100%, 0% 100%, 0% 0%, 50% 0%);
        }}
        
        .slice-label {{
            position: absolute;
            background: rgba(255, 255, 255, 0.95);
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: bold;
            text-align: center;
            color: #333;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
            white-space: nowrap;
            z-index: 10;
        }}
        
        .chart-legend {{
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 12px;
            padding: 20px;
            background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
            border-radius: 12px;
            border: 1px solid #e0e0e0;
        }}
        
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        
        .legend-color {{
            width: 16px;
            height: 16px;
            border-radius: 3px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .legend-text {{
            font-size: 13px;
            font-weight: 600;
            color: #2c3e50;
        }}
        
        /* Right Column Sections */
        .info-section {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border: 1px solid #e1e8ed;
            display: flex;
            flex-direction: column;
        }}
        
        .section-title {{
            font-size: 18px;
            font-weight: 600;
            color: #333;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .highlights-icon {{ color: #4caf50; }}
        .upnext-icon {{ color: #2196f3; }}
        
        .bullet-list {{
            list-style: none;
        }}
        
        .bullet-list li {{
            position: relative;
            padding-left: 25px;
            margin-bottom: 15px;
            line-height: 1.5;
            color: #555;
        }}
        
        .bullet-list li:before {{
            content: "•";
            position: absolute;
            left: 0;
            color: #667eea;
            font-size: 20px;
            font-weight: bold;
        }}
        
        /* Footer */
        .footer {{
            background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
            color: white;
            padding: 25px 30px;
            text-align: center;
            font-size: 16px;
            line-height: 1.5;
        }}
        
        /* Responsive Design */
        @media (max-width: {config['styling']['responsive_breakpoint']}) {{
            .main-content {{
                grid-template-columns: 1fr;
            }}
            
            .metrics-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
        
        @media (max-width: 768px) {{
            .header {{
                flex-direction: column;
                gap: 20px;
                text-align: center;
            }}
            
            .metrics-grid {{
                grid-template-columns: 1fr;
            }}
            
            .quotes-chart-container {{
                grid-template-columns: 1fr;
                gap: 20px;
            }}
            
            .chart-container {{
                flex-direction: column;
                text-align: center;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <div class="logo-section">
                <div class="logo">{config['report_metadata']['company_logo']}</div>
                <div class="report-title">{config['report_metadata']['title']}</div>
            </div>
            <div class="date-badge">{config['report_metadata']['month']}</div>
        </div>
        
        <!-- Main Content -->
        <div class="main-content">
            <!-- Left Column -->
            <div class="left-column">
                <!-- Metrics Grid -->
                <div class="metrics-grid">
                    <!-- Views Card -->
                    <div class="metric-card">
                        <div class="metric-header">
                            <div class="metric-icon views-icon">👁️</div>
                            <div class="metric-title">Views</div>
                        </div>
                        <div class="metric-value">{config['metrics']['views']['value']}</div>
                        <div class="metric-change">
                            <div class="change-arrow"></div>
                            <div class="change-text">{config['metrics']['views']['change_percentage']}</div>
                        </div>
                        <div class="metric-description">
                            {config['metrics']['views']['description']}
                        </div>
                    </div>
                    
                    <!-- Returning Users Card -->
                    <div class="metric-card">
                        <div class="metric-header">
                            <div class="metric-icon users-icon">👥</div>
                            <div class="metric-title">Returning Users</div>
                        </div>
                        <div class="metric-value">{config['metrics']['returning_users']['value']}</div>
                        <div class="metric-change">
                            <div class="change-arrow"></div>
                            <div class="change-text">{config['metrics']['returning_users']['change_percentage']}</div>
                        </div>
                        <div class="metric-description">
                            {config['metrics']['returning_users']['description']}
                        </div>
                    </div>
                    
                    <!-- Items in Catalog Card -->
                    <div class="metric-card">
                        <div class="metric-header">
                            <div class="metric-icon items-icon">📋</div>
                            <div class="metric-title">Items in Catalog</div>
                        </div>
                        <div class="metric-value">{config['metrics']['catalog_items']['value']}</div>
                        <div class="metric-change">
                            <div class="change-arrow"></div>
                            <div class="change-text">{config['metrics']['catalog_items']['change_percentage']}</div>
                        </div>
                        <div class="metric-description">
                            {config['metrics']['catalog_items']['description']}
                        </div>
                    </div>
                </div>
                
                <!-- Chart and User Quotes Section - Side by Side -->
                <div class="quotes-chart-container">
                    <!-- Chart Section -->
                    <div class="chart-section">
                        <div class="chart-title">
                            📊 {config['division_chart']['title']}
                        </div>
                        <div class="chart-container">
                            <div class="pie-chart">
                                <div class="pie-container">
"""

    # Generate pie chart using conic-gradient
    # Calculate the conic-gradient stops
    current_angle = 0
    conic_gradient_parts = []
    
    for division in config['division_chart']['divisions']:
        # Convert percentage to degrees (360 * percentage / 100)
        angle = (division['percentage'] * 360) / 100
        end_angle = current_angle + angle
        
        conic_gradient_parts.append(f"{division['gradient_start']} {current_angle}deg {end_angle}deg")
        current_angle = end_angle
    
    # Create the conic-gradient CSS
    conic_gradient_css = ", ".join(conic_gradient_parts)
    
    html_content += f"""                                    <div class="pie-slice" style="background: conic-gradient({conic_gradient_css});">
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Legend -->
                            <div class="chart-legend">
"""

    # Generate legend items
    for division in config['division_chart']['divisions']:
        html_content += f"""                                <div class="legend-item">
                                    <div class="legend-color" style="background: {division['gradient_start']}; width: 16px; height: 16px; border-radius: 3px;"></div>
                                    <div class="legend-text">{division['name']} ({division['percentage']}%)</div>
                                </div>
"""

    html_content += f"""                            </div>
                        </div>
                    </div>
                    
                    <!-- User Quotes Section -->
                    <div class="quotes-section">
                        <div class="quotes-title">
                            💬 User Quotes
                        </div>
                        <div class="quote-content">
                            "{config['user_quote']['content']}"
                        </div>
                        <div class="quote-attribution">
                            <div class="profile-pic">{config['user_quote']['initials']}</div>
                            <div class="attribution-text">
                                <strong>{config['user_quote']['author']}</strong><br>
                                {config['user_quote']['title']}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Right Column -->
            <div class="right-column">
                <!-- Highlights Section -->
                <div class="info-section">
                    <div class="section-title">
                        <span class="highlights-icon">✨</span> {config['highlights']['title']}
                    </div>
                    <ul class="bullet-list">
"""

    # Generate highlights items
    for item in config['highlights']['items']:
        html_content += f"""                        <li>{item}</li>
"""

    html_content += f"""                    </ul>
                </div>
                
                <!-- Up Next Section -->
                <div class="info-section">
                    <div class="section-title">
                        <span class="upnext-icon">🚀</span> {config['up_next']['title']}
                    </div>
                    <ul class="bullet-list">
"""

    # Generate up next items
    for item in config['up_next']['items']:
        html_content += f"""                        <li>{item}</li>
"""

    html_content += f"""                    </ul>
                </div>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            {config['footer']['text']}
        </div>
    </div>
    
    <script>
        mermaid.initialize({{ 
            startOnLoad: true,
            theme: 'default',
            pie: {{
                useWidth: 800,
                useHeight: 600
            }}
        }});
    </script>
</body>
</html>"""

    return html_content


def main():
    """Main function to generate the report."""
    
    # File paths
    json_file = "Input Values.json"
    output_file = "beacon_monthly_report_generated.html"
    
    # Check if JSON file exists
    if not os.path.exists(json_file):
        print(f"❌ Error: {json_file} not found!")
        return 1
    
    try:
        # Load configuration
        print(f"📖 Loading configuration from {json_file}...")
        config = load_json_config(json_file)
        
        # Generate HTML report
        print("🔨 Generating HTML report...")
        html_content = generate_html_report(config)
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Successfully generated: {output_file}")
        print(f"📊 Report title: {config['report_metadata']['title']}")
        print(f"📅 Month: {config['report_metadata']['month']}")
        print(f"📈 Divisions: {len(config['division_chart']['divisions'])} divisions")
        print(f"💬 Quote author: {config['user_quote']['author']}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
