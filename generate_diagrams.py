"""
Generate Graphviz diagrams for AirSense Guardian
Requires: pip install graphviz
"""
import os
import subprocess
import sys

def check_graphviz():
    """Check if Graphviz is installed"""
    try:
        result = subprocess.run(['dot', '-V'], capture_output=True, text=True)
        print(f"[OK] Graphviz found: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("[ERROR] Graphviz not found!")
        print("\nPlease install Graphviz:")
        print("  Windows: choco install graphviz")
        print("  Or download from: https://graphviz.org/download/")
        return False

def generate_diagram(dot_file, output_name, format='png'):
    """Generate diagram from DOT file"""
    if not os.path.exists(dot_file):
        print(f"[ERROR] File not found: {dot_file}")
        return False
    
    output_file = f"diagrams/{output_name}.{format}"
    os.makedirs("diagrams", exist_ok=True)
    
    try:
        cmd = ['dot', f'-T{format}', dot_file, '-o', output_file]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"[OK] Generated: {output_file}")
            return True
        else:
            print(f"[ERROR] Failed to generate {output_name}:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"[ERROR] Exception: {e}")
        return False

def main():
    """Generate all diagrams"""
    print("="*60)
    print("AirSense Guardian - Diagram Generator")
    print("="*60)
    print()
    
    # Check Graphviz
    if not check_graphviz():
        print("\n[INFO] You can still view DOT files in online tools:")
        print("  https://dreampuf.github.io/GraphvizOnline/")
        return
    
    print()
    print("Generating diagrams...")
    print()
    
    # Diagrams to generate
    diagrams = [
        ("diagrams/confusion_matrix.dot", "confusion_matrix", "Confusion Matrix"),
        ("diagrams/deployment_pipeline.dot", "deployment_pipeline", "Deployment Pipeline"),
        ("diagrams/system_flowchart.dot", "system_flowchart", "System Flowchart"),
    ]
    
    success_count = 0
    for dot_file, output_name, description in diagrams:
        print(f"Generating {description}...")
        if generate_diagram(dot_file, output_name):
            success_count += 1
        print()
    
    print("="*60)
    print(f"Complete! Generated {success_count}/{len(diagrams)} diagrams")
    print("="*60)
    print()
    print("Output files:")
    for _, output_name, _ in diagrams:
        print(f"  - diagrams/{output_name}.png")
    print()

if __name__ == "__main__":
    main()

