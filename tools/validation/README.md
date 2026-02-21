# JSON to XSD Validation Tool

**Created**: 2026-02-21
**Status**: ✅ Implemented
**Issue**: N/A (new tool)

## Executive Summary

A validation tool that compares JSON class definitions (from `docs/json/packages/`) against the AUTOSAR XSD schema (`demos/xsd/AUTOSAR_00052/AUTOSAR_00052.xsd`) to detect discrepancies in member names, types, and cardinality.

## Problem Statement

The codebase has JSON mapping files that define AUTOSAR classes, but no automated validation that these mappings match the official XSD schema. This can lead to:
- Missing members in JSON that exist in XSD
- Type mismatches between definitions
- Cardinality differences
- Outdated mappings when new AUTOSAR versions are released

## Implementation

### Architecture

```
tools/validation/
  __init__.py
  main.py                                   # CLI entry point
  xsd_parser.py                              # XSD parsing using lxml
  json_loader.py                             # JSON loading
  comparator.py                              # Comparison engine
  reporter.py                                # Report generation
  models.py                                  # Data models
```

### Key Features

1. **Memory-efficient XSD parsing**: Uses `lxml.etree.iterparse()` to stream the 145K-line XSD file
2. **Exact name extraction**: Extracts JSON member names from `mmt.qualifiedName` metadata (no name conversion needed)
3. **Inheritance handling**: Separates own members from inherited members to avoid false positives
4. **Multiple output formats**: Console (with ANSI color codes) and Markdown reports
5. **Severity levels**: ERROR, WARNING, INFO with filtering support
6. **Skip list support**: Respects `tools/skip_classes.yaml` for manually maintained classes

### Usage

```bash
# Validate all classes against AUTOSAR 00052
python -m tools.validation

# Validate specific class
python -m tools.validation --class Collection

# Save Markdown report
python -m tools.validation --output validation_report.md

# Only show errors and warnings
python -m tools.validation --severity WARNING

# Use different XSD version
python -m tools.validation --xsd-version 00051

# Verbose output
python -m tools.validation -v
```

### CLI Arguments

| Argument | Description |
|----------|-------------|
| `--xsd-version` | AUTOSAR XSD schema version (default: 00052) |
| `--class` | Validate only specific class |
| `-o, --output` | Output Markdown report file path |
| `--severity` | Minimum severity level: ERROR, WARNING, INFO (default: INFO) |
| `--no-color` | Disable colored console output |
| `--json-dir` | Directory containing JSON package files (default: docs/json/packages) |
| `--xsd-dir` | Directory containing XSD schema files (default: demos/xsd) |
| `--skip-list` | Path to skip_classes.yaml file (default: tools/skip_classes.yaml) |
| `-v, --verbose` | Show verbose output |

### Discrepancy Types

| Type | Description | Severity |
|------|-------------|----------|
| `missing_xsd_type` | Class in JSON but not in XSD | INFO |
| `missing_member` | Member in XSD but not in JSON | ERROR/WARNING |
| `extra_member` | Member in JSON but not in XSD | ERROR/INFO |
| `type_mismatch` | Different types between XSD and JSON | WARNING |
| `multiplicity_mismatch` | Different cardinality | ERROR/WARNING |
| `ref_kind_mismatch` | is_ref differs | WARNING |

### Validation Results

Running the tool on all classes against AUTOSAR 00052:

```bash
python -m tools.validation --severity ERROR -o validation_report.md
```

**Results**:
- **Total discrepancies**: 6,896
- **Errors**: 139
- **Warnings**: 4,344
- **Info**: 2,413

### Example Output

```
======================================================================
VALIDATION REPORT
======================================================================
Total discrepancies: 11

Summary:
  ERRORS: 0
  WARNINGS: 8
  INFO: 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WARNINGS (Non-Critical Issues)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [Collection.element] missing_member: Member exists in XSD but not in JSON
    Member exists in XSD but not in JSON
      xsd_type:
      xsd_multiplicity: 0..1
      xsd_reference_kind: ref
```

### Key Implementation Details

#### XSD Parser (`xsd_parser.py`)

Uses `lxml.etree.iterparse()` for memory-efficient streaming:

```python
context = etree.iterparse(
    str(self.xsd_path),
    events=("end",),
    tag=f"{{{self.XSD_NS}}}complexType",
)

for event, elem in context:
    self._parse_complex_type(elem)
    elem.clear()  # Free memory
```

Extracts exact JSON names from `mmt.qualifiedName`:

```xml
<xsd:element name="AUTO-COLLECT">
  <xsd:appinfo>mmt.qualifiedName="Collection.autoCollect"</xsd:appinfo>
</xsd:element>
```

#### Inheritance Handling

The XSD parser separates:
- `members`: Only the class's own members (from the group matching the class name)
- `all_members`: All members including inherited (from base type groups)

This prevents false positives where inherited members are flagged as missing from JSON.

#### Type Normalization

Types are normalized for comparison by removing:
- `AR:` prefix → `AR:TestType` → `TestType`
- `--SUBTYPES-ENUM` suffix → `TestType--SUBTYPES-ENUM` → `TestType`
- `--SIMPLE` suffix → `TestType--SIMPLE` → `TestType`
- `-ENUM` suffix → `TestType-ENUM` → `TestType`

#### Multiplicity Mapping

| XSD Cardinality | JSON Multiplicity |
|-----------------|-------------------|
| `minOccurs="0" maxOccurs="1"` | `0..1` |
| `minOccurs="1" maxOccurs="1"` | `1` |
| `minOccurs="0" maxOccurs="unbounded"` or `-1` | `*` |

### Testing

Unit tests in `tests/unit/tools/test_xsd_validation.py`:

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python3 -m pytest tests/unit/tools/test_xsd_validation.py -v
```

**Test Coverage**:
- XSD parser: 8 tests (multiplicity conversion, reference type detection)
- JSON loader: 1 test (loading classes from JSON)
- Schema comparator: 12 tests (comparison logic, type normalization, skip classes)
- Reporter: 3 tests (summary, filtering)

**Result**: 24 tests passed

### Dependencies

Added to `pyproject.toml`:

```toml
dependencies = [
    "lxml>=4.9.0",
    "pyyaml>=6.0",
]
```

### Known Limitations

1. **Manually maintained classes**: Classes in `tools/skip_classes.yaml` won't be found in XSD (expected)
2. **Complex inheritance**: Deep inheritance chains require recursive resolution
3. **XSD imports**: Some groups defined in separate files (not fully handled)
4. **Performance**: Full validation takes ~30 seconds for 1,623 classes on typical hardware
5. **Anonymous complexTypes**: Elements with anonymous inline complexTypes may show empty types in discrepancies

### Success Criteria

| Criteria | Status |
|----------|--------|
| Successfully parse AUTOSAR_00052.xsd (145K lines) | ✅ |
| Load all JSON class definitions | ✅ |
| Detect missing members in JSON | ✅ |
| Detect type mismatches | ✅ |
| Detect cardinality differences | ✅ |
| Generate colored console output | ✅ |
| Generate Markdown report | ✅ |
| Complete validation efficiently | ✅ |
| Exit with error code if discrepancies found | ✅ |
| All unit tests pass | ✅ |
| Code passes linting | ✅ |

### Future Enhancements

1. **HTML report**: Interactive report with filtering and detailed discrepancy views
2. **CI/CD integration**: Exit with error code if discrepancies found (already implemented)
3. **Auto-fix suggestions**: Suggest JSON corrections for common discrepancies
4. **Multiple schema versions**: Validate against multiple XSD versions simultaneously
5. **Diff mode**: Compare discrepancies between different schema versions
6. **Web UI**: Browser-based interface for exploring validation results

### Files Created/Modified

**New Files**:
- `tools/validation/main.py` - Main CLI entry point
- `tools/validation/README.md` - This file
- `tools/validation/__init__.py` - Module initialization
- `tools/validation/models.py` - Data models
- `tools/validation/xsd_parser.py` - XSD parsing logic
- `tools/validation/json_loader.py` - JSON loading logic
- `tools/validation/comparator.py` - Comparison engine
- `tools/validation/reporter.py` - Report generation
- `tests/unit/tools/test_xsd_validation.py` - Unit tests

**Modified Files**:
- `pyproject.toml` - Added lxml>=4.9.0 dependency

### References

- XSD Schema: `demos/xsd/AUTOSAR_00052/AUTOSAR_00052.xsd`
- JSON Definitions: `docs/json/packages/*.classes.json`
- Schema Config: `src/armodel/cfg/schemas/config.yaml`
- Skip List: `tools/skip_classes.yaml`