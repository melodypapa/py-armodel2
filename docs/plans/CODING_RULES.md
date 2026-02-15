# Coding Rules for py-armodel2

**Purpose:** Define class-based rules for generating Python classes from mapping.json

## Rule Categories

Design rules are categorized by their type and scope:

### 1. Naming Conventions (CLASS-BASED)
- **CODING_RULE_001**: File names must use snake_case
- **CODING_RULE_002**: Class names must use PascalCase

### 2. Class Structure (CLASS-BASED)
- **CODING_RULE_004**: Every generated class must inherit from ARObject
- **CODING_RULE_005**: Each class must include `serialize()` and `deserialize()` methods
- **CODING_RULE_006**: Each class must include a builder class for easy instantiation
- **CODING_RULE_007**: Builder class must be named `<ClassName>Builder`

### 3. Serialization/Deserialization (CLASS-BASED)
- **CODING_RULE_008**: `serialize()` returns `lxml.etree.Element`
- **CODING_RULE_009**: `deserialize()` is a `@classmethod` accepting an element parameter
- **CODING_RULE_010**: All child elements must be serialized using their `serialize()` methods
- **CODING_RULE_011**: All child elements must be deserialized using `deserialize()` methods

### 4. Package Structure (CLASS-BASED)
- **CODING_RULE_012**: Package hierarchy must match `mapping.json` package_path exactly
- **CODING_RULE_013**: Each class gets its own file in matching directory
- **CODING_RULE_014**: `__init__.py` exports all classes in package

### 5. Splitable Elements (CLASS-BASED)
- **CODING_RULE_015**: Elements marked as `splitable: true` in mapping.json must include split metadata
- **CODING_RULE_016**: Splitable elements must have `get_split_filename()` method
- **CODING_RULE_017**: Splitable elements must have `serialize()` override for multi-file projects

### 6. Type Safety (CLASS-BASED)
- **CODING_RULE_018**: Use type hints for all class attributes
- **CODING_RULE_019**: Use Optional[T] for nullable attributes
- **CODING_RULE_020**: Document complex types with docstrings

### 7. Validation (CLASS-BASED)
- **CODING_RULE_021**: All attributes must be validated in `builder.build()` method
- **CODING_RULE_022**: Raise ValueError for invalid attribute values
- **CODING_RULE_023**: Validate required attributes are present

### 8. Documentation (CLASS-BASED)
- **CODING_RULE_024**: Each class must have a docstring
- **CODING_RULE_025**: Each method must have a docstring
- **CODING_RULE_026**: Document complex logic with inline comments

### 9. Testing (CLASS-BASED)
- **CODING_RULE_027**: Each class must have unit tests
- **CODING_RULE_028**: Tests must cover serialize/deserialize
- **CODING_RULE_029**: Tests must verify builder functionality

### 10. Code Quality (CLASS-BASED)
- **CODING_RULE_030**: No hardcoded values (use config where appropriate)
- **CODING_RULE_031**: Follow PEP 8 style guide
- **CODING_RULE_032**: Maximum line length 100 characters
