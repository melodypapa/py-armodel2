# CLI ARXML Formatter Design

**Date:** 2026-02-18
**Status:** Approved
**Author:** Claude (brainstorming session)

## Overview

Design a multi-command CLI interface for py-armodel2, starting with an `armodel format` command that reads unformatted ARXML files and produces formatted output. The CLI uses a professional multi-command structure to enable future extensibility.

## Requirements

### Functional Requirements
- FR1: CLI must read unformatted ARXML files and produce formatted output
- FR2: Error handling behavior must be configurable via GlobalSettingsManager and CLI arguments
- FR3: CLI must support `--strict` and `--permissive` modes for validation
- FR4: Command structure must be extensible for future commands (validate, convert, info, etc.)

### Non-Functional Requirements
- NFR1: CLI must return appropriate exit codes for scripting/CI integration
- NFR2: CLI must be testable at unit, integration, and e2e levels
- NFR3: CLI must follow existing codebase patterns (class-based, dependency injection)
- NFR4: CLI must integrate with existing ARXMLReader/ARXMLWriter infrastructure

## Architecture

### Multi-Command Structure

The CLI uses a subcommand-based architecture similar to `git` or `docker`:

```
armodel format INPUT -o OUTPUT [OPTIONS]
armodel validate INPUT [OPTIONS]  # Future
armodel info INPUT [OPTIONS]      # Future
```

### Components

**`src/armodel/cli/main.py`** - CLI entry point and router
- `main()` function creates the argument parser and dispatches commands
- Handles global arguments (`--verbose`, `--version`, `--help`)
- Integrates with GlobalSettingsManager for configuration

**`src/armodel/cli/commands/`** - Command implementations
- `format.py` - Implements `armodel format` command
- `__init__.py` - Command registry
- Future: `validate.py`, `info.py`, etc.

**`src/armodel/cli/common.py`** - Shared utilities
- File I/O helpers
- Error message formatting
- Exit code constants

Each command module:
- Defines its own arguments using argparse
- Integrates with GlobalSettingsManager for validation settings
- Handles its own errors and returns appropriate exit codes
- Uses ARXMLReader/ARXMLWriter for core functionality

## Data Flow

### Format Command Flow

1. **Parse CLI arguments** - Input file, output file, options
2. **Configure GlobalSettingsManager** - Apply CLI overrides
3. **Load ARXML** - ARXMLReader loads and parses input file
4. **Serialize ARXML** - ARXMLWriter serializes with pretty-print formatting
5. **Write output** - Save formatted ARXML to output file
6. **Report result** - Print success message with statistics
7. **Exit cleanly** - Return exit code 0

### Error Handling

| Error Type | Exit Code | Behavior |
|------------|-----------|----------|
| File not found | 1 | Print error, exit |
| Parse error (invalid ARXML) | 2 | Respects `--strict`/`--permissive` |
| Write error (permissions) | 3 | Print error, exit |
| Unhandled exception | 4 | Print stack trace if `--verbose` |

## Command Interface

### `armodel format` Command

```bash
armodel format INPUT -o OUTPUT [OPTIONS]

Arguments:
  INPUT              Input ARXML file to format

Options:
  -o, --output OUTPUT    Output ARXML file path (required)
  --strict               Enable strict validation (fail on errors)
  --permissive           Enable permissive mode (continue on warnings)
  --encoding ENCODING    Output encoding (default: UTF-8)
  --no-pretty-print      Disable pretty-printing
  -v, --verbose          Show detailed error messages
  -q, --quiet            Suppress output messages
```

### Usage Examples

```bash
# Basic formatting
armodel format unformatted.arxml -o formatted.arxml

# Strict validation mode
armodel format input.arxml -o output.arxml --strict

# Quiet mode for scripts
armodel format input.arxml -o output.arxml --quiet

# Custom encoding
armodel format input.arxml -o output.arxml --encoding UTF-16
```

## Configuration

### GlobalSettingsManager Integration

The CLI configures GlobalSettingsManager based on CLI arguments:

```python
settings = GlobalSettingsManager()

# Default (from GlobalSettingsManager.DEFAULTS):
# - strict_validation: False
# - warn_on_unrecognized: True

# CLI overrides:
# --strict     → strict_validation = True
# --permissive → strict_validation = False
```

## Implementation Notes

### Dependencies
- Use `argparse` (stdlib) for CLI argument parsing
- No additional CLI library dependencies required
- Leverage existing `ARXMLReader` and `ARXMLWriter` classes

### Exit Codes
```python
EXIT_SUCCESS = 0
EXIT_FILE_NOT_FOUND = 1
EXIT_PARSE_ERROR = 2
EXIT_WRITE_ERROR = 3
EXIT_UNHANDLED_ERROR = 4
```

## Testing Strategy

### Unit Tests (`tests/unit/cli/`)
- Test argument parsing for each command
- Test error handling and exit codes
- Test file I/O helpers
- Mock ARXMLReader/ARXMLWriter

### Integration Tests (`tests/integration/cli/`)
- Test full format command with real ARXML files
- Verify output files are valid ARXML
- Test various ARXML versions (00044, 00046, 00052)
- Test error scenarios

### Test Fixtures
- Use existing ARXML files in `demos/arxml/` and `tests/fixtures/arxml/`
- Add small invalid ARXML files for error testing

## Future Extensions

The multi-command architecture enables:
- `armodel validate` - Validate ARXML against XSD schema
- `armodel info` - Display ARXML file information (version, packages, elements)
- `armodel convert` - Convert between ARXML schema versions
- `armodel diff` - Compare two ARXML files
- `armodel query` - Query ARXML elements using XPath or similar

## References

- ARXMLReader: `src/armodel/reader/__init__.py`
- ARXMLWriter: `src/armodel/writer/__init__.py`
- GlobalSettingsManager: `src/armodel/core/global_settings.py`
- Design Rules: `docs/designs/design_rules.md`
