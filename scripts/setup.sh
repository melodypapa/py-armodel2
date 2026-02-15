#!/bin/bash
set -e

echo "Installing py-armodel2 in development mode..."

# Install in development mode
pip install -e ".[dev]"

# Run tests to verify
pytest

echo "Setup complete!"
