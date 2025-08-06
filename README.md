# 🎬 Manim DSA Visualizations

A collection of Data Structures and Algorithms visualizations created with Manim.

## 📋 Available Visualizations

1. **BSTVisualization** - Binary Search Tree Insertion
   - Shows step-by-step BST construction
   - Animates search paths and node insertions
   - Demonstrates BST properties

2. **SortingVisualization** - Bubble Sort Algorithm
   - Visualizes array sorting with element swaps
   - Highlights comparisons and sorted elements
   - Shows the complete sorting process

3. **LinkedListVisualization** - Linked List Traversal
   - Creates a linked list with nodes and arrows
   - Animates traversal through the list
   - Shows time complexity information

## 🚀 Running the Visualizations

### Method 1: Simple Shell Script (Recommended)
```bash
# Run all visualizations with low quality
./run.sh

# Run specific scene with quality
./run.sh bst l      # BST with low quality
./run.sh sort h      # Sort with high quality
./run.sh list m      # List with medium quality
```

### Method 2: Python Script with Advanced Options
```bash
# List available scenes and options
python run_manim.py --list

# Show detailed help
python run_manim.py --help-scenes

# Run specific scene with options
python run_manim.py bst -q h -f mp4
python run_manim.py sort -f gif
python run_manim.py all -q l --clean
```

### Method 3: Direct Manim Commands
```bash
# Basic commands
uv run manim main.py BSTVisualization -pql
uv run manim main.py SortingVisualization -pqm
uv run manim main.py LinkedListVisualization -pqh
```

## 📁 Project Structure
```
langnim/
├── main.py                    # Main Manim visualizations
├── run.sh                     # Simple shell script runner
├── run_manim.py              # Advanced Python script runner
├── run_visualizations.py     # Basic Python script
├── pyproject.toml            # Project dependencies
├── README.md                 # This file
└── media/                    # Generated video files
```

## 🎨 Quality Options
- `l` - Low quality (fast, good for testing)
- `m` - Medium quality (balanced)
- `h` - High quality (better visuals)
- `k` - 4K quality (slow, best quality)

## 📹 Output Formats
- `mp4` - MP4 video (default)
- `gif` - GIF animation
- `png` - PNG images

## 🛠️ Script Options

### Shell Script (`run.sh`)
- Simple and fast
- Basic quality and scene selection
- Good for quick testing

### Python Script (`run_manim.py`)
- Advanced options and features
- Multiple output formats
- Clean media folder option
- Detailed progress tracking
- Error handling

### Basic Python Script (`run_visualizations.py`)
- Simple batch runner
- Good for running all scenes quickly

## 📊 Examples

```bash
# Quick test all scenes
./run.sh

# High quality BST only
python run_manim.py bst -q h

# Create GIF of sorting
python run_manim.py sort -f gif

# Clean and run all with medium quality
python run_manim.py all -q m --clean

# Save last frame of linked list
python run_manim.py list -s
```

## 🎯 Features
- **Educational**: Each visualization teaches DSA concepts
- **Interactive**: Animations show algorithm steps clearly
- **Customizable**: Easy to modify colors, timing, and data
- **Professional**: Clean, modern visual design
- **Multiple Formats**: Support for video, GIF, and image output

## 🔧 Dependencies
- Python 3.13+
- Manim Community v0.19.0+
- uv (for dependency management)

## 📝 Notes
- Videos are saved in the `media/` folder
- Cached renders are reused for faster subsequent runs
- Use `--clean` flag to clear cache and regenerate
- Preview is enabled by default (use `-q` instead of `-pq` to disable)
