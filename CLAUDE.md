# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**py-armodel2** is a Python library project for working with AUTOSAR (Automotive Open System Architecture) models. The repository currently contains XML schema definitions and test data for AUTOSAR models, but the Python library implementation has not yet been created.

**Current State**: This repository is in early development stage containing only reference data and schemas. No Python source code, build system, or test framework exists yet.

## Repository Structure

```
py-armodel2/
├── demos/
│   ├── xsd/              # AUTOSAR XML Schema Definition files
│   │   ├── AUTOSAR_00044/ # AUTOSAR Classic Platform 4.3.1 (2017)
│   │   ├── AUTOSAR_00046/ # AUTOSAR CP 4.4.0/AP 18-10 (2018)
│   │   ├── AUTOSAR_00052/ # AUTOSAR CP/AP 23-11 R23-11 (2023) - Latest
│   │   └── old/           # Legacy schema versions
│   └── arxml/             # AUTOSAR XML model files (test data)
└── docs/                  # Documentation (currently empty)
```

## AUTOSAR Schema Versions

The repository maintains multiple AUTOSAR XML schema versions for backward compatibility:

- **AUTOSAR_00044.xsd**: Classic Platform 4.3.1, AP 17-10 (2017)
- **AUTOSAR_00046.xsd**: CP 4.4.0, AP 18-10 (2018) - Includes COMPACT and STRICT_COMPACT variants
- **AUTOSAR_00052.xsd**: CP and AP Release 23-11, version 4.9.0 (2023) - Most recent

Schema variants:
- **Standard**: Full schema with all validation rules
- **COMPACT**: Performance-optimized version with reduced validation overhead
- **STRICT_COMPACT**: Combined strict multiplicity validation with compact performance

## Architecture

### Schema-Driven Design

The project is designed around AUTOSAR XML schemas that define:
- **Structure**: XML element hierarchy and relationships
- **Validation**: Type constraints, multiplicities, and value ranges
- **Namespaces**: AUTOSAR standard XML namespaces for different elements

### Multi-Version Support

The architecture must support multiple AUTOSAR standard versions simultaneously:
- Schema version detection and selection
- Version-specific parsing and validation
- Backward compatibility for older ARXML files
- Forward compatibility considerations

### Data Types

ARXML files in `demos/arxml/` contain various AUTOSAR model elements:
- **Base type definitions**: Primitive data types
- **Application data types**: Domain-specific types
- **Port interfaces**: Component communication interfaces
- **Computation methods**: Data transformation rules
- **Component types**: Software component specifications
- **Collection specifications**: Domain-specific groupings (Body, Chassis, Powertrain, etc.)

## Development Commands

**Note**: No build system, test framework, or development tooling currently exists. These would need to be implemented as part of the Python library development.

Expected future commands (to be implemented):
- Build: `python -m build` or `pip install -e .`
- Test: `pytest tests/` or `python -m pytest`
- Lint: `flake8` or `ruff check`
- Type checking: `mypy`

## Key Implementation Considerations

When implementing the Python library, consider:

1. **XML Parsing**: Use `lxml` or `xml.etree.ElementTree` for ARXML parsing
2. **Schema Validation**: Integrate XSD validation using `lxml` schema validation
3. **Version Handling**: Implement schema version detection from ARXML namespace declarations
4. **Object Model**: Create Python classes representing AUTOSAR elements
5. **Performance**: Consider using compact schemas for validation to reduce overhead
6. **Testing**: Use ARXML files in `demos/arxml/` as test fixtures

## AUTOSAR References

- Official AUTOSAR specifications: https://www.autosar.org
- Schema version numbering follows AUTOSAR document identification (e.g., AUTOSAR_00052)
- Each schema version corresponds to specific AUTOSAR Classic Platform and Adaptive Platform releases
