#!/usr/bin/env python3
"""
Script to run all Manim visualizations with different quality settings.
"""

import subprocess
import sys
import os

def run_visualization(scene_name, quality="l"):
    """
    Run a Manim visualization with specified quality.
    
    Args:
        scene_name: Name of the scene class
        quality: Quality setting ('l' for low, 'm' for medium, 'h' for high)
    """
    cmd = f"uv run manim main.py {scene_name} -pq{quality}"
    print(f"Running {scene_name} with quality {quality}...")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {scene_name} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {scene_name}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    scenes = [
        "BSTVisualization",
        "SortingVisualization", 
        "LinkedListVisualization"
    ]
    
    print("🎬 Manim DSA Visualizations")
    print("=" * 40)
    
    # Run with low quality for quick testing
    print("\n🚀 Running all visualizations with low quality...")
    for scene in scenes:
        run_visualization(scene, "l")
        print()
    
    print("✨ All visualizations completed!")
    print("\nTo run individual scenes with different quality:")
    print("  - Low quality:   uv run manim main.py SceneName -pql")
    print("  - Medium quality: uv run manim main.py SceneName -pqm") 
    print("  - High quality:   uv run manim main.py SceneName -pqh")
    print("  - No preview:     uv run manim main.py SceneName -q")

if __name__ == "__main__":
    main() 