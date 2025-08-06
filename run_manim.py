#!/usr/bin/env python3
"""
Comprehensive script to run Manim DSA visualizations with various options.
"""

import subprocess
import sys
import os
import argparse
import time
from pathlib import Path

class ManimRunner:
    def __init__(self):
        self.scenes = {
            "bst": "BSTVisualization",
            "sort": "SortingVisualization", 
            "list": "LinkedListVisualization",
            "all": "all"
        }
        
        self.quality_options = {
            "l": "low",
            "m": "medium", 
            "h": "high",
            "k": "4k"
        }
        
        self.output_formats = {
            "mp4": "mp4",
            "gif": "gif",
            "png": "png"
        }

    def run_visualization(self, scene_name, quality="l", output_format="mp4", preview=True, save_last_frame=False):
        """
        Run a Manim visualization with specified options.
        
        Args:
            scene_name: Name of the scene class
            quality: Quality setting ('l', 'm', 'h', 'k')
            output_format: Output format ('mp4', 'gif', 'png')
            preview: Whether to show preview
            save_last_frame: Whether to save last frame
        """
        # Build command
        cmd_parts = ["uv", "run", "manim", "main.py", scene_name]
        
        # Quality flag
        cmd_parts.append(f"-q{quality}")
        
        # Output format
        if output_format != "mp4":
            cmd_parts.append(f"-f{output_format}")
        
        # Preview flag
        if preview:
            cmd_parts.append("-p")
        
        # Save last frame
        if save_last_frame:
            cmd_parts.append("-s")
        
        cmd = " ".join(cmd_parts)
        
        print(f"🎬 Running {scene_name}...")
        print(f"   Quality: {self.quality_options[quality]}")
        print(f"   Format: {output_format}")
        print(f"   Preview: {'Yes' if preview else 'No'}")
        
        start_time = time.time()
        
        try:
            result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            end_time = time.time()
            duration = end_time - start_time
            
            print(f"✅ {scene_name} completed successfully! ({duration:.1f}s)")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running {scene_name}: {e}")
            if e.stderr:
                print(f"Error details: {e.stderr}")
            return False

    def list_scenes(self):
        """List all available scenes."""
        print("📋 Available Scenes:")
        print("=" * 30)
        for key, scene in self.scenes.items():
            if key != "all":
                print(f"  {key:8} -> {scene}")
        print()

    def list_quality_options(self):
        """List all quality options."""
        print("🎨 Quality Options:")
        print("=" * 20)
        for key, desc in self.quality_options.items():
            print(f"  {key} -> {desc}")
        print()

    def clean_media_folder(self):
        """Clean the media folder."""
        media_path = Path("media")
        if media_path.exists():
            print("🧹 Cleaning media folder...")
            import shutil
            shutil.rmtree(media_path)
            print("✅ Media folder cleaned!")

    def show_help(self):
        """Show comprehensive help."""
        print("""
🎬 Manim DSA Visualizations Runner
====================================

USAGE:
  python run_manim.py [scene] [options]

SCENES:
  bst      - Binary Search Tree Insertion
  sort     - Bubble Sort Visualization  
  list     - Linked List Traversal
  all      - Run all scenes

QUALITY:
  -q l     - Low quality (fast)
  -q m     - Medium quality
  -q h     - High quality
  -q k     - 4K quality (slow)

FORMATS:
  -f mp4   - MP4 video (default)
  -f gif   - GIF animation
  -f png   - PNG images

OPTIONS:
  -p       - Show preview (default)
  -s       - Save last frame
  --clean  - Clean media folder first
  --list   - List available scenes
  --help   - Show this help

EXAMPLES:
  python run_manim.py bst -q h          # High quality BST
  python run_manim.py all -q l          # All scenes, low quality
  python run_manim.py sort -f gif       # Bubble sort as GIF
  python run_manim.py list --clean      # Clean and run linked list
        """)

def main():
    parser = argparse.ArgumentParser(description="Run Manim DSA visualizations")
    parser.add_argument("scene", nargs="?", default="all", 
                       help="Scene to run (bst, sort, list, all)")
    parser.add_argument("-q", "--quality", default="l", choices=["l", "m", "h", "k"],
                       help="Quality setting")
    parser.add_argument("-f", "--format", default="mp4", choices=["mp4", "gif", "png"],
                       help="Output format")
    parser.add_argument("-p", "--preview", action="store_true", default=True,
                       help="Show preview")
    parser.add_argument("-s", "--save-frame", action="store_true",
                       help="Save last frame")
    parser.add_argument("--clean", action="store_true",
                       help="Clean media folder first")
    parser.add_argument("--list", action="store_true",
                       help="List available scenes")
    parser.add_argument("--help-scenes", action="store_true",
                       help="Show detailed help")

    args = parser.parse_args()

    runner = ManimRunner()

    # Handle special flags
    if args.help_scenes:
        runner.show_help()
        return

    if args.list:
        runner.list_scenes()
        runner.list_quality_options()
        return

    # Clean if requested
    if args.clean:
        runner.clean_media_folder()

    # Determine scenes to run
    if args.scene == "all":
        scenes_to_run = [scene for key, scene in runner.scenes.items() if key != "all"]
    elif args.scene in runner.scenes:
        scenes_to_run = [runner.scenes[args.scene]]
    else:
        print(f"❌ Unknown scene: {args.scene}")
        runner.list_scenes()
        return

    # Run visualizations
    print("🚀 Starting Manim DSA Visualizations...")
    print("=" * 50)
    
    success_count = 0
    total_count = len(scenes_to_run)
    
    for scene in scenes_to_run:
        success = runner.run_visualization(
            scene, 
            quality=args.quality,
            output_format=args.format,
            preview=args.preview,
            save_last_frame=args.save_frame
        )
        if success:
            success_count += 1
        print()

    # Summary
    print("📊 Summary:")
    print(f"   Successful: {success_count}/{total_count}")
    print(f"   Failed: {total_count - success_count}/{total_count}")
    
    if success_count == total_count:
        print("🎉 All visualizations completed successfully!")
    else:
        print("⚠️  Some visualizations failed. Check the output above.")

if __name__ == "__main__":
    main() 