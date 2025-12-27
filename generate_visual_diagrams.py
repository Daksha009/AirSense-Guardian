# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

"""
Generate visual diagrams using multiple methods
"""
import os
import sys
import subprocess
from pathlib import Path

def try_graphviz_render(dot_file, output_file):
    """Try to render using graphviz library"""
    try:
        import graphviz
        
        with open(dot_file, 'r', encoding='utf-8') as f:
            dot_content = f.read()
        
        graph = graphviz.Source(dot_content)
        
        # Try different formats
        for fmt in ['png', 'svg', 'pdf']:
            try:
                output_path = graph.render(
                    filename=Path(output_file).stem,
                    directory=Path(output_file).parent,
                    format=fmt,
                    cleanup=True
                )
                print(f"  [OK] Generated: {output_path}")
                return output_path
            except:
                continue
        return None
    except Exception as e:
        print(f"  [INFO] Graphviz library method failed: {e}")
        return None

def try_pydot_render(dot_file, output_file):
    """Try to render using pydot"""
    try:
        import pydot
        
        graphs = pydot.graph_from_dot_file(dot_file)
        if graphs:
            graph = graphs[0]
            for fmt in ['png', 'svg', 'pdf']:
                try:
                    output_path = str(Path(output_file).with_suffix(f'.{fmt}'))
                    graph.write(output_path, format=fmt)
                    print(f"  [OK] Generated: {output_path}")
                    return output_path
                except:
                    continue
        return None
    except Exception as e:
        print(f"  [INFO] Pydot method failed: {e}")
        return None

def create_html_viewer():
    """Create an HTML file that can display diagrams using online service"""
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AirSense Guardian - Visual Diagrams</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background: #f5f5f5;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        .diagram-section {
            margin: 40px 0;
            padding: 20px;
            background: #fafafa;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        .diagram-title {
            font-size: 20px;
            font-weight: bold;
            color: white;
            margin-bottom: 15px;
            padding: 15px;
            background: linear-gradient(135deg, #3498db, #2980b9);
            border-radius: 4px;
        }
        .diagram-container {
            background: white;
            padding: 20px;
            border-radius: 4px;
            margin: 20px 0;
            text-align: center;
        }
        iframe {
            width: 100%;
            height: 800px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .instructions {
            background: #e8f4f8;
            padding: 15px;
            border-left: 4px solid #3498db;
            border-radius: 4px;
            margin: 20px 0;
        }
        .instructions h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 5px;
        }
        .btn:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 AirSense Guardian - Visual Diagrams</h1>
        
        <div class="instructions">
            <h3>📋 How to View Diagrams:</h3>
            <p>Click the buttons below to open each diagram in the online Graphviz viewer. 
            The diagrams will render automatically when you paste the DOT content.</p>
        </div>

        <div class="diagram-section">
            <div class="diagram-title">1. Confusion Matrix - AQI Prediction Accuracy</div>
            <div class="diagram-container">
                <p><strong>Model Performance Metrics:</strong></p>
                <ul style="text-align: left; display: inline-block;">
                    <li>R² Score: 0.733 (73.3% variance explained)</li>
                    <li>RMSE: 10.56 AQI points</li>
                    <li>MAE: 8.39 AQI points</li>
                    <li>MAPE: 8.82%</li>
                </ul>
                <p style="margin-top: 20px;">
                    <a href="https://dreampuf.github.io/GraphvizOnline/" target="_blank" class="btn">
                        Open Online Viewer
                    </a>
                </p>
                <p style="margin-top: 10px;">
                    <strong>File:</strong> <code>diagrams/confusion_matrix.dot</code>
                </p>
            </div>
        </div>

        <div class="diagram-section">
            <div class="diagram-title">2. Model Deployment Pipeline</div>
            <div class="diagram-container">
                <p><strong>6-Stage Deployment Process:</strong></p>
                <ol style="text-align: left; display: inline-block;">
                    <li>Data Collection & Preparation</li>
                    <li>Model Training</li>
                    <li>Model Persistence</li>
                    <li>Model Deployment</li>
                    <li>Production</li>
                    <li>Monitoring & Updates</li>
                </ol>
                <p style="margin-top: 20px;">
                    <a href="https://dreampuf.github.io/GraphvizOnline/" target="_blank" class="btn">
                        Open Online Viewer
                    </a>
                </p>
                <p style="margin-top: 10px;">
                    <strong>File:</strong> <code>diagrams/deployment_pipeline.dot</code>
                </p>
            </div>
        </div>

        <div class="diagram-section">
            <div class="diagram-title">3. System Flowchart - Complete Architecture</div>
            <div class="diagram-container">
                <p><strong>System Components:</strong></p>
                <ul style="text-align: left; display: inline-block;">
                    <li>User Interface (React Frontend)</li>
                    <li>API Layer (Flask Backend)</li>
                    <li>Data Sources (OpenAQ, OpenWeatherMap)</li>
                    <li>ML Models (Predictor, Source Attribution, Action Engine)</li>
                    <li>Visualization Components</li>
                </ul>
                <p style="margin-top: 20px;">
                    <a href="https://dreampuf.github.io/GraphvizOnline/" target="_blank" class="btn">
                        Open Online Viewer
                    </a>
                </p>
                <p style="margin-top: 10px;">
                    <strong>File:</strong> <code>diagrams/system_flowchart.dot</code>
                </p>
            </div>
        </div>
    </div>
</body>
</html>'''
    
    with open('diagrams/visual_viewer.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("  [OK] Created HTML viewer: diagrams/visual_viewer.html")

def main():
    """Generate visual diagrams"""
    print("="*60)
    print("Generating Visual Diagrams")
    print("="*60)
    print()
    
    diagrams = [
        ("diagrams/confusion_matrix.dot", "diagrams/confusion_matrix"),
        ("diagrams/deployment_pipeline.dot", "diagrams/deployment_pipeline"),
        ("diagrams/system_flowchart.dot", "diagrams/system_flowchart"),
    ]
    
    os.makedirs("diagrams", exist_ok=True)
    
    success_count = 0
    
    for dot_file, output_file in diagrams:
        if not os.path.exists(dot_file):
            print(f"[ERROR] File not found: {dot_file}")
            continue
        
        print(f"Processing: {os.path.basename(dot_file)}")
        
        # Try graphviz library
        result = try_graphviz_render(dot_file, output_file)
        if result:
            success_count += 1
            continue
        
        # Try pydot
        result = try_pydot_render(dot_file, output_file)
        if result:
            success_count += 1
            continue
        
        print(f"  [INFO] Could not generate image locally")
        print(f"  [INFO] Use online viewer: https://dreampuf.github.io/GraphvizOnline/")
        print()
    
    # Create HTML viewer
    create_html_viewer()
    
    print("="*60)
    if success_count > 0:
        print(f"Success! Generated {success_count} diagram(s)")
        print("Check the 'diagrams' folder for PNG/SVG files")
    else:
        print("Could not generate images locally (Graphviz binary not installed)")
        print("Created HTML viewer: diagrams/visual_viewer.html")
        print()
        print("To view diagrams:")
        print("  1. Open: diagrams/visual_viewer.html in browser")
        print("  2. Or use: https://dreampuf.github.io/GraphvizOnline/")
        print("  3. Copy DOT file content and paste to view")
    print("="*60)

if __name__ == "__main__":
    main()

