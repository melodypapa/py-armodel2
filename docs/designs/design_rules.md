# Design Rules for py-armodel2

**Purpose:** Define rules for generating Python classes from mapping.json

## Rule Categories

Design rules are categorized by their type and scope:

### 1. Naming Conventions
- **DESIGN_RULE_001**: File names must use snake_case
- **DESIGN_RULE_002**: Class names must use PascalCase
- **DESIGN_RULE_003**: Module names must use snake_case

### 2. Class Structure
- **DESIGN_RULE_004**: Every generated class must inherit from ARObject
- **DESIGN_RULE_005**: Class must include `serialize()` and `deserialize()` methods
- **DESIGN_RULE_006**: Class must include a builder class for easy instantiation
- **DESIGN_RULE_007**: Builder class must be named `<ClassName>Builder`

### 3. Serialization/Deserialization
- **DESIGN_RULE_008**: `serialize()` returns `lxml.etree.Element`
- **DESIGN_RULE_009**: `deserialize()` is a `@classmethod` accepting an element parameter
- **DESIGN_RULE_010**: All child elements must be serialized using their `serialize()` methods
- **DESIGN_RULE_011**: All child elements must be deserialized using `deserialize()` methods

### 4. Package Structure
- **DESIGN_RULE_012**: Package hierarchy must match `mapping.json` package_path exactly
- **DESIGN_RULE_013**: Each class gets its own file in the matching directory
- **DESIGN_RULE_014**: `__init__.py` exports all classes in package

### 5. Splitable Elements
- **DESIGN_RULE_015**: Elements marked as `splitable: true` in mapping.json must include split metadata
- **DESIGN_RULE_016**: Splitable elements must have `get_split_filename()` method

### 6. Type Safety
- **DESIGN_RULE_017**: Use type hints for all class attributes
- **DESIGN_RULE_018**: Use Optional[T] for nullable attributes
- **DESIGN_RULE_019**: Document complex types with docstrings

### 7. Validation
- **DESIGN_RULE_020**: All attributes must be validated in `builder.build()` method
- **DESIGN_RULE_021**: Raise ValueError for invalid attribute values
- **DESIGN_RULE_022**: Validate required attributes are present

### 8. Documentation
- **DESIGN_RULE_023**: Each class must have a docstring
- **DESIGN_RULE_024**: Each method must have a docstring
- **DESIGN_RULE_025**: Document complex logic with inline comments

### 9. Testing
- **DESIGN_RULE_026**: Each class must have unit tests
- **DESIGN_RULE_027**: Tests must cover serialize/deserialize
- **DESIGN_RULE_028**: Tests must verify builder functionality

### 10. Architecture
- **DESIGN_RULE_032**: Use class-based architecture instead of module-based
- **DESIGN_RULE_033**: All infrastructure modules (core, reader, writer, cfg) must use class-based design
- **DESIGN_RULE_034**: Infrastructure classes should use dependency injection for testability
- **DESIGN_RULE_035**: Singleton pattern should be used for shared state managers

### 11. Infrastructure Classes
- **DESIGN_RULE_036**: SchemaVersionManager manages schema version detection and configuration
- **DESIGN_RULE_037**: ConfigurationManager provides configuration loading with caching
- **DESIGN_RULE_038**: ARXMLReader handles ARXML file loading and mapping to objects
- **DESIGN_RULE_039**: ARXMLWriter handles object serialization and ARXML file saving

### 12. Code Quality
- **DESIGN_RULE_029**: No hardcoded values (use config where appropriate)
- **DESIGN_RULE_030**: Follow PEP 8 style guide
- **DESIGN_RULE_031**: Maximum line length 100 characters
- **DESIGN_RULE_040**: All import statements must be defined at the beginning of the file
- **DESIGN_RULE_041**: Use full names for import statements to avoid circular import issues
  - When importing from the same package, use relative imports (e.g., `from .module import Class`)
  - When importing from different packages, use full absolute imports (e.g., `from armodel.models.M2.AUTOSARTemplates.Package.module import Class`)
  - Avoid wildcard imports (`from module import *`)
  - Prefer explicit imports over `__init__.py` re-exports when possible to clarify dependencies
