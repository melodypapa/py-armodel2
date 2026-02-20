#!/bin/bash
# Format ARXML files from demos/arxml/ and output to data/arxml/
#
# Usage:
#   ./scripts/format_arxml.sh
#   bash scripts/format_arxml.sh
#
# This script will:
#   1. Create data/arxml/ directory if it doesn't exist
#   2. Format all .arxml files from demos/arxml/
#   3. Output formatted files to data/arxml/
#   4. Show summary of successful/failed files
#
# For verbose error output on failed files, run:
#   armodel format demos/arxml/<filename> -o data/arxml/<filename> -v

# Directories
INPUT_DIR="demos/arxml"
OUTPUT_DIR="data/arxml"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "Formatting ARXML files..."
echo "Input:  $INPUT_DIR"
echo "Output: $OUTPUT_DIR"
echo ""

# Counters
total_files=0
success_count=0
failed_count=0
failed_files=()

# Loop through all .arxml files in input directory
for input_file in "$INPUT_DIR"/*.arxml; do
    if [ -f "$input_file" ]; then
        total_files=$((total_files + 1))

        # Get the basename of the file
        basename=$(basename "$input_file")
        output_file="$OUTPUT_DIR/$basename"

        echo "[$total_files] Formatting: $basename"

        # Run armodel format command
        if armodel format "$input_file" -o "$output_file" --quiet 2>/dev/null; then
            echo "      ✓ Success"
            success_count=$((success_count + 1))
        else
            echo "      ✗ Failed"
            failed_count=$((failed_count + 1))
            failed_files+=("$basename")
        fi
    fi
done

echo ""
echo "======================================="
echo "Formatting Summary:"
echo "======================================="
echo "Total files:     $total_files"
echo "Successful:      $success_count"
echo "Failed:          $failed_count"

if [ $failed_count -gt 0 ]; then
    echo ""
    echo "Failed files:"
    for file in "${failed_files[@]}"; do
        echo "  - $file"
    done
    echo ""
    echo "You can re-run with verbose mode to see errors:"
    echo "  armodel format demos/arxml/<filename> -o data/arxml/<filename> -v"
fi

echo ""
echo "Output directory: $OUTPUT_DIR"
