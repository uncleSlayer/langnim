#!/bin/bash

# Manim DSA Visualizations Runner
# Quick script for running visualizations

echo "🎬 Manim DSA Visualizations"
echo "============================"

# Function to show usage
show_usage() {
    echo "Usage: $0 [scene] [quality]"
    echo ""
    echo "Scenes:"
    echo "  bst    - Binary Search Tree"
    echo "  sort   - Bubble Sort"
    echo "  list   - Linked List"
    echo "  all    - All scenes"
    echo ""
    echo "Quality:"
    echo "  l      - Low (fast)"
    echo "  m      - Medium"
    echo "  h      - High"
    echo "  k      - 4K (slow)"
    echo ""
    echo "Examples:"
    echo "  $0 bst l     # BST with low quality"
    echo "  $0 all h     # All scenes with high quality"
    echo "  $0 sort m    # Sort with medium quality"
}

# Default values
SCENE=${1:-"all"}
QUALITY=${2:-"l"}

# Validate scene
case $SCENE in
    "bst"|"sort"|"list"|"all")
        ;;
    *)
        echo "❌ Unknown scene: $SCENE"
        show_usage
        exit 1
        ;;
esac

# Validate quality
case $QUALITY in
    "l"|"m"|"h"|"k")
        ;;
    *)
        echo "❌ Unknown quality: $QUALITY"
        show_usage
        exit 1
        ;;
esac

# Map scene names to class names
case $SCENE in
    "bst")
        SCENE_NAME="BSTVisualization"
        ;;
    "sort")
        SCENE_NAME="SortingVisualization"
        ;;
    "list")
        SCENE_NAME="LinkedListVisualization"
        ;;
    "all")
        SCENE_NAME="all"
        ;;
esac

echo "🚀 Running $SCENE with $QUALITY quality..."
echo ""

if [ "$SCENE_NAME" = "all" ]; then
    # Run all scenes
    scenes=("BSTVisualization" "SortingVisualization" "LinkedListVisualization")
    for scene in "${scenes[@]}"; do
        echo "🎬 Running $scene..."
        uv run manim main.py "$scene" -pq"$QUALITY"
        echo ""
    done
    echo "✅ All scenes completed!"
else
    # Run single scene
    uv run manim main.py "$SCENE_NAME" -pq"$QUALITY"
fi

echo ""
echo "🎉 Done! Check the media folder for output files." 