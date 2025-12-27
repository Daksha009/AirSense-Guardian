# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

"""
Open and render Graphviz diagrams
"""
import os
import subprocess
import webbrowser
from pathlib import Path

def render_and_open_diagram(dot_file, output_name):
    """Try to render diagram and open it"""
    try:
        import graphviz
        
        # Read DOT file
        with open(dot_file, 'r', encoding='utf-8') as f:
            dot_content = f.read()
        
        # Create graph
        graph = graphviz.Source(dot_content)
        
        # Try to render
        try:
            output_path = graph.render(
                filename=output_name,
                directory='diagrams',
                format='png',
                cleanup=True
            )
            print(f"[OK] Generated: {output_path}")
            
            # Open the image
            if os.path.exists(output_path):
                os.startfile(output_path)
                return True
        except Exception as e:
            print(f"[INFO] Could not render locally: {e}")
            print(f"[INFO] Opening DOT file instead...")
            
            # Open DOT file in default editor
            os.startfile(dot_file)
            return False
            
    except ImportError:
        print("[INFO] graphviz library not available")
        # Open DOT file
        os.startfile(dot_file)
        return False
    except Exception as e:
        print(f"[INFO] Error: {e}")
        # Open DOT file
        os.startfile(dot_file)
        return False

def open_online_viewer(dot_file):
    """Open online Graphviz viewer"""
    print(f"\n[INFO] To view online:")
    print(f"  1. Go to: https://dreampuf.github.io/GraphvizOnline/")
    print(f"  2. Copy content from: {dot_file}")
    print(f"  3. Paste and view!")

def main():
    """Open all diagrams"""
    print("="*60)
    print("Opening AirSense Guardian Diagrams")
    print("="*60)
    print()
    
    diagrams = [
        ("diagrams/confusion_matrix.dot", "confusion_matrix", "Confusion Matrix"),
        ("diagrams/deployment_pipeline.dot", "deployment_pipeline", "Deployment Pipeline"),
        ("diagrams/system_flowchart.dot", "system_flowchart", "System Flowchart"),
    ]
    
    for dot_file, output_name, description in diagrams:
        if os.path.exists(dot_file):
            print(f"Opening {description}...")
            render_and_open_diagram(dot_file, output_name)
            print()
        else:
            print(f"[ERROR] File not found: {dot_file}")
            print()
    
    print("="*60)
    print("All diagrams opened!")
    print("="*60)
    print()
    print("If images were generated, they're in the 'diagrams' folder.")
    print("If DOT files opened, you can view them online at:")
    print("  https://dreampuf.github.io/GraphvizOnline/")
    print()

if __name__ == "__main__":
    main()

