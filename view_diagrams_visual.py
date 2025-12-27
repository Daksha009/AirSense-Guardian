# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

"""
Automatically open diagrams in visual viewer
Uses online Graphviz renderer with embedded content
"""
import os
import webbrowser
import urllib.parse
from pathlib import Path

def create_visual_html():
    """Create HTML file with embedded diagrams using online renderer"""
    
    # Read DOT files
    diagrams = {}
    dot_files = {
        'confusion_matrix': 'diagrams/confusion_matrix.dot',
        'deployment_pipeline': 'diagrams/deployment_pipeline.dot',
        'system_flowchart': 'diagrams/system_flowchart.dot'
    }
    
    for name, filepath in dot_files.items():
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                diagrams[name] = f.read()
    
    # Create HTML with embedded viewer
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AirSense Guardian - Visual Diagrams</title>
    <script src="https://cdn.jsdelivr.net/npm/viz.js@2.1.2/viz.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/viz.js@2.1.2/full.render.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1600px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .tabs {{
            display: flex;
            background: #f5f5f5;
            border-bottom: 2px solid #ddd;
        }}
        .tab {{
            flex: 1;
            padding: 20px;
            text-align: center;
            cursor: pointer;
            background: #f5f5f5;
            border: none;
            font-size: 1.1em;
            font-weight: bold;
            color: #666;
            transition: all 0.3s;
        }}
        .tab:hover {{
            background: #e0e0e0;
        }}
        .tab.active {{
            background: white;
            color: #667eea;
            border-bottom: 3px solid #667eea;
        }}
        .content {{
            padding: 40px;
            min-height: 600px;
        }}
        .diagram-container {{
            background: #fafafa;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
            min-height: 500px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .diagram-container svg {{
            max-width: 100%;
            height: auto;
        }}
        .description {{
            margin-top: 30px;
            padding: 20px;
            background: #e8f4f8;
            border-left: 4px solid #667eea;
            border-radius: 4px;
        }}
        .description h3 {{
            color: #2c3e50;
            margin-bottom: 15px;
        }}
        .description ul {{
            margin-left: 20px;
            line-height: 1.8;
        }}
        .loading {{
            color: #666;
            font-size: 1.2em;
        }}
        .error {{
            color: #e74c3c;
            padding: 20px;
            background: #ffe6e6;
            border-radius: 4px;
        }}
        .download-btn {{
            display: inline-block;
            margin-top: 20px;
            padding: 12px 24px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: bold;
            transition: background 0.3s;
        }}
        .download-btn:hover {{
            background: #5568d3;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 AirSense Guardian</h1>
            <p>Visual Diagram Viewer</p>
        </header>
        
        <div class="tabs">
            <button class="tab active" onclick="showTab(0)">Confusion Matrix</button>
            <button class="tab" onclick="showTab(1)">Deployment Pipeline</button>
            <button class="tab" onclick="showTab(2)">System Flowchart</button>
        </div>
        
        <div class="content">
            <div id="tab-0" class="tab-content">
                <div class="diagram-container" id="diagram-0">
                    <div class="loading">Loading diagram...</div>
                </div>
                <div class="description">
                    <h3>📈 Confusion Matrix - AQI Prediction Accuracy</h3>
                    <ul>
                        <li><strong>R² Score:</strong> 0.733 (73.3% variance explained)</li>
                        <li><strong>RMSE:</strong> 10.56 AQI points</li>
                        <li><strong>MAE:</strong> 8.39 AQI points</li>
                        <li><strong>MAPE:</strong> 8.82%</li>
                        <li>Shows prediction accuracy by AQI category (Good, Moderate, Unhealthy, etc.)</li>
                        <li>Displays True Positive rates and overall model performance</li>
                    </ul>
                </div>
            </div>
            
            <div id="tab-1" class="tab-content" style="display:none;">
                <div class="diagram-container" id="diagram-1">
                    <div class="loading">Loading diagram...</div>
                </div>
                <div class="description">
                    <h3>🚀 Model Deployment Pipeline</h3>
                    <ul>
                        <li><strong>Stage 1:</strong> Data Collection (OpenAQ, OpenWeatherMap APIs)</li>
                        <li><strong>Stage 2:</strong> Model Training (Feature Engineering, Hyperparameter Tuning)</li>
                        <li><strong>Stage 3:</strong> Model Persistence (Save model and metadata)</li>
                        <li><strong>Stage 4:</strong> Model Deployment (Flask API with endpoints)</li>
                        <li><strong>Stage 5:</strong> Production (React Frontend integration)</li>
                        <li><strong>Stage 6:</strong> Monitoring & Updates (Performance tracking, retraining)</li>
                    </ul>
                </div>
            </div>
            
            <div id="tab-2" class="tab-content" style="display:none;">
                <div class="diagram-container" id="diagram-2">
                    <div class="loading">Loading diagram...</div>
                </div>
                <div class="description">
                    <h3>🔄 System Flowchart - Complete Architecture</h3>
                    <ul>
                        <li>User journey from React Frontend to Flask Backend</li>
                        <li>Data flow: API requests → ML models → JSON responses</li>
                        <li>ML components: Source Attribution, AQI Predictor, Action Engine</li>
                        <li>Frontend display: AQI Card, Charts, Alerts, Recommendations</li>
                        <li>Error handling and auto-refresh mechanisms</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        const diagrams = {{
            'confusion_matrix': `{diagrams.get('confusion_matrix', '')}`,
            'deployment_pipeline': `{diagrams.get('deployment_pipeline', '')}`,
            'system_flowchart': `{diagrams.get('system_flowchart', '')}`
        }};

        function showTab(index) {{
            // Hide all tabs
            document.querySelectorAll('.tab-content').forEach(tab => {{
                tab.style.display = 'none';
            }});
            document.querySelectorAll('.tab').forEach(tab => {{
                tab.classList.remove('active');
            }});
            
            // Show selected tab
            document.getElementById(`tab-${{index}}`).style.display = 'block';
            event.target.classList.add('active');
            
            // Render diagram if not already rendered
            renderDiagram(index);
        }}

        function renderDiagram(index) {{
            const diagramNames = ['confusion_matrix', 'deployment_pipeline', 'system_flowchart'];
            const diagramName = diagramNames[index];
            const container = document.getElementById(`diagram-${{index}}`);
            
            if (!diagrams[diagramName]) {{
                container.innerHTML = '<div class="error">Diagram content not found</div>';
                return;
            }}
            
            try {{
                const viz = new Viz();
                viz.renderSVGElement(diagrams[diagramName])
                    .then(function(element) {{
                        container.innerHTML = '';
                        container.appendChild(element);
                    }})
                    .catch(function(error) {{
                        container.innerHTML = '<div class="error">Error rendering diagram. Please check console.</div>';
                        console.error('Error:', error);
                    }});
            }} catch (error) {{
                container.innerHTML = '<div class="error">Error loading Viz.js. Please check internet connection.</div>';
                console.error('Error:', error);
            }}
        }}

        // Render first diagram on load
        window.addEventListener('load', function() {{
            renderDiagram(0);
        }});
    </script>
</body>
</html>'''
    
    output_file = 'diagrams/visual_diagrams.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file

def main():
    """Create and open visual diagrams"""
    print("="*60)
    print("Creating Visual Diagram Viewer")
    print("="*60)
    print()
    
    html_file = create_visual_html()
    
    if os.path.exists(html_file):
        print(f"[OK] Created visual viewer: {html_file}")
        print()
        print("Opening in browser...")
        webbrowser.open(f'file:///{os.path.abspath(html_file).replace(os.sep, "/")}')
        print()
        print("="*60)
        print("[OK] Diagrams are now visible in your browser!")
        print("="*60)
        print()
        print("Features:")
        print("  - Interactive tabs to switch between diagrams")
        print("  - Fully rendered visual diagrams")
        print("  - Detailed descriptions for each diagram")
        print()
    else:
        print("[ERROR] Could not create HTML file")

if __name__ == "__main__":
    main()

