"""
Download Graphviz diagrams as PNG images locally
"""
import os
import requests
import base64
from pathlib import Path

def download_diagram_online(dot_content, output_file):
    """Download diagram using online Graphviz service"""
    try:
        # Use QuickChart Graphviz API
        url = "https://quickchart.io/graphviz"
        
        # Encode DOT content
        payload = {
            'graph': dot_content
        }
        
        response = requests.post(url, json=payload, timeout=30)
        
        if response.status_code == 200:
            # Save the image
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"  [OK] Downloaded: {output_file}")
            return True
        else:
            print(f"  [ERROR] API returned status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"  [ERROR] {e}")
        return False

def download_via_graphviz_online(dot_content, output_file):
    """Alternative: Use graphviz-online API"""
    try:
        # Use graphviz-online service
        url = "https://dreampuf.github.io/GraphvizOnline/graphviz"
        
        # Try direct conversion
        import urllib.parse
        encoded = urllib.parse.quote(dot_content)
        
        # Alternative approach: use a different service
        # Using a public Graphviz renderer
        api_url = "https://api.graphviz.org/render"
        
        params = {
            'format': 'png',
            'dot': dot_content
        }
        
        response = requests.get(api_url, params=params, timeout=30)
        
        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"  [OK] Downloaded: {output_file}")
            return True
        else:
            return False
            
    except Exception as e:
        return False

def create_image_from_dot_local(dot_file, output_file):
    """Try to create image using local Graphviz if available"""
    try:
        import subprocess
        
        # Try using dot command directly
        result = subprocess.run(
            ['dot', '-Tpng', dot_file, '-o', output_file],
            capture_output=True,
            timeout=10
        )
        
        if result.returncode == 0 and os.path.exists(output_file):
            print(f"  [OK] Generated locally: {output_file}")
            return True
        else:
            return False
    except:
        return False

def download_diagram_alternative(dot_content, output_file):
    """Use alternative method: save DOT and provide instructions"""
    # Save DOT file
    dot_file = output_file.replace('.png', '.dot')
    with open(dot_file, 'w', encoding='utf-8') as f:
        f.write(dot_content)
    
    # Try using an online converter service
    try:
        # Use a public Graphviz rendering service
        # Method: Use QuickChart or similar
        import json
        
        # Try QuickChart Graphviz
        url = "https://quickchart.io/graphviz"
        headers = {'Content-Type': 'application/json'}
        data = {'graph': dot_content}
        
        response = requests.post(url, json=data, headers=headers, timeout=30)
        
        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"  [OK] Downloaded: {output_file}")
            return True
    except:
        pass
    
    return False

def main():
    """Download all three diagrams"""
    print("="*60)
    print("Downloading Graphviz Diagrams as Images")
    print("="*60)
    print()
    
    diagrams = [
        ("diagrams/confusion_matrix.dot", "diagrams/confusion_matrix.png", "Confusion Matrix"),
        ("diagrams/deployment_pipeline.dot", "diagrams/deployment_pipeline.png", "Deployment Pipeline"),
        ("diagrams/system_flowchart.dot", "diagrams/system_flowchart.png", "System Flowchart"),
    ]
    
    os.makedirs("diagrams", exist_ok=True)
    
    success_count = 0
    
    for dot_file, output_file, name in diagrams:
        if not os.path.exists(dot_file):
            print(f"[ERROR] File not found: {dot_file}")
            continue
        
        print(f"Processing: {name}...")
        
        # Read DOT content
        with open(dot_file, 'r', encoding='utf-8') as f:
            dot_content = f.read()
        
        # Try local generation first
        if create_image_from_dot_local(dot_file, output_file):
            success_count += 1
            continue
        
        # Try online download
        if download_diagram_online(dot_content, output_file):
            success_count += 1
            continue
        
        # Try alternative method
        if download_diagram_alternative(dot_content, output_file):
            success_count += 1
            continue
        
        print(f"  [INFO] Could not generate image automatically")
        print(f"  [INFO] DOT file saved: {dot_file}")
        print(f"  [INFO] Use online viewer: https://dreampuf.github.io/GraphvizOnline/")
        print()
    
    print("="*60)
    if success_count > 0:
        print(f"Success! Downloaded {success_count} diagram(s)")
        print("Check the 'diagrams' folder for PNG files")
    else:
        print("Could not download images automatically")
        print()
        print("Alternative methods:")
        print("1. Install Graphviz: choco install graphviz")
        print("2. Use online viewer: https://dreampuf.github.io/GraphvizOnline/")
        print("3. Copy DOT content and paste in online viewer, then download")
    print("="*60)

if __name__ == "__main__":
    main()

