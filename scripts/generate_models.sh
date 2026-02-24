# Use python3 if available, otherwise fallback to python
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
else
    PYTHON_CMD=python
fi

$PYTHON_CMD -m tools.generate_models --members --classes --enums --primitives
$PYTHON_CMD tools/generate_models_init.py