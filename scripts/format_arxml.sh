#!/bin/bash
# Format ARXML files from demos/arxml/ and output to data/arxml/
#
# Usage:
#   ./scripts/format_arxml.sh                    # Format all files
#   ./scripts/format_arxml.sh <file1> <file2>    # Format specific files
#   ./scripts/format_arxml.sh --verbose          # Show errors for each file
#   ./scripts/format_arxml.sh --dry-run          # List files without formatting
#
# This script will:
#   1. Create data/arxml/ directory if it doesn't exist
#   2. Format all .arxml files from demos/arxml/ (or specific files if provided)
#   3. Output formatted files to data/arxml/
#   4. Show summary of successful/failed files
#
# For verbose error output on failed files, run:
#   armodel format demos/arxml/<filename> -o data/arxml/<filename> -v

set -e

# Directories
INPUT_DIR="demos/arxml"
OUTPUT_DIR="data/arxml"

# Flags
VERBOSE=false
DRY_RUN=false
ENCODING="UTF-8"
PRESET=""

# Parse arguments
FILES_TO_FORMAT=()
while [[ $# -gt 0 ]]; do
    case $1 in
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --encoding|-e)
            ENCODING="$2"
            shift 2
            ;;
        --input|-i)
            INPUT_DIR="$2"
            shift 2
            ;;
        --output|-o)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        --validated)
            INPUT_DIR="demos/validated"
            OUTPUT_DIR="data/validated"
            PRESET="validated"
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS] [files...]"
            echo ""
            echo "Options:"
            echo "  --verbose, -v       Show detailed error messages"
            echo "  --dry-run           List files without formatting"
            echo "  --encoding, -e      Set output encoding (default: UTF-8)"
            echo "  --input, -i DIR     Set input directory (default: demos/arxml)"
            echo "  --output, -o DIR    Set output directory (default: data/arxml)"
            echo "  --validated         Use demos/validated → data/validated"
            echo "  --help, -h          Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0                                    # Format all files from demos/arxml"
            echo "  $0 BswMMode.arxml CanSystem.arxml    # Format specific files"
            echo "  $0 --verbose                         # Format all with error details"
            echo "  $0 --dry-run                         # List files without formatting"
            echo "  $0 --validated                       # Format from demos/validated"
            echo "  $0 --input demos/validated --output data/validated  # Custom directories"
            echo "  $0 --encoding UTF-8                  # Use UTF-8 encoding"
            exit 0
            ;;
        *.arxml)
            FILES_TO_FORMAT+=("$1")
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# If no specific files provided, process all .arxml files
if [ ${#FILES_TO_FORMAT[@]} -eq 0 ]; then
    for file in "$INPUT_DIR"/*.arxml; do
        if [ -f "$file" ]; then
            FILES_TO_FORMAT+=("$(basename "$file")")
        fi
    done
fi

# Sort files alphabetically
IFS=$'\n' FILES_TO_FORMAT=($(sort <<<"${FILES_TO_FORMAT[*]}"))
unset IFS

echo "======================================="
echo "ARXML Format Script"
echo "======================================="
echo "Input:    $INPUT_DIR"
echo "Output:   $OUTPUT_DIR"
echo "Files:    ${#FILES_TO_FORMAT[@]}"
echo "Encoding: $ENCODING"
echo ""

# Dry run: just list files
if [ "$DRY_RUN" = true ]; then
    echo "Files to be formatted:"
    for i in "${!FILES_TO_FORMAT[@]}"; do
        echo "  [$((i+1))] ${FILES_TO_FORMAT[$i]}"
    done
    echo ""
    echo "Dry run complete. No files were modified."
    exit 0
fi

# Counters
total_files=${#FILES_TO_FORMAT[@]}
success_count=0
failed_count=0
failed_files=()
failed_errors=()

# Process each file
for i in "${!FILES_TO_FORMAT[@]}"; do
    basename=${FILES_TO_FORMAT[$i]}
    input_file="$INPUT_DIR/$basename"
    output_file="$OUTPUT_DIR/$basename"

    # Skip if input file doesn't exist
    if [ ! -f "$input_file" ]; then
        echo "[$((i+1))/$total_files] ✗ Skipped (not found): $basename"
        failed_count=$((failed_count + 1))
        failed_files+=("$basename (file not found)")
        continue
    fi

    echo "[$((i+1))/$total_files] Formatting: $basename"

    # Run armodel format command
    if [ "$VERBOSE" = true ]; then
        # With verbose output
        if armodel format "$input_file" -o "$output_file" --encoding "$ENCODING" 2>&1; then
            echo "      ✓ Success"
            success_count=$((success_count + 1))
        else
            echo "      ✗ Failed"
            failed_count=$((failed_count + 1))
            failed_files+=("$basename")
            failed_errors+=("$(armodel format "$input_file" -o "$output_file" --encoding "$ENCODING" -v 2>&1 | head -5)")
        fi
    else
        # Quiet mode
        if armodel format "$input_file" -o "$output_file" --encoding "$ENCODING" --quiet 2>/dev/null; then
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
    for i in "${!failed_files[@]}"; do
        echo "  ✗ ${failed_files[$i]}"
        if [ "$VERBOSE" = true ] && [ -n "${failed_errors[$i]}" ]; then
            echo "    Error: ${failed_errors[$i]}"
        fi
    done
    echo ""
    echo "To debug individual files:"
    for i in "${!failed_files[@]}"; do
        filename="${failed_files[$i]}"
        echo "  armodel format demos/arxml/$filename -o data/output.arxml --encoding $ENCODING -v"
    done
fi

echo ""
echo "Output directory: $OUTPUT_DIR"

# Exit with error code if any files failed
if [ $failed_count -gt 0 ]; then
    exit 1
fi
