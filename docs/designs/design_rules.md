# Design Rules for py-armodel2

**Purpose:** Define rules for generating Python classes from mapping.json

## Rule Categories

Design rules are categorized by their type and scope:

### 1. Naming Conventions
- **CODING_RULE_001**: File names must use snake_case
- **CODING_RULE_002**: Class names must use PascalCase
- **CODING_RULE_003**: Module names must use snake_case

### 2. Class Structure
- **CODING_RULE_004**: Every generated class must inherit from ARObject
- **CODING_RULE_005**: Class must include `serialize()` and `deserialize()` methods
- **CODING_RULE_006**: Class must include a builder class for easy instantiation
- **CODING_RULE_007**: Builder class must be named `<ClassName>Builder`

### 3. Serialization/Deserialization
- **CODING_RULE_008**: `serialize()` returns `lxml.etree.Element`
- **CODING_RULE_009**: `deserialize()` is a `@classmethod` accepting an element parameter
- **CODING_RULE_010**: All child elements must be serialized using their `serialize()` methods
- **CODING_RULE_011**: All child elements must be deserialized using `deserialize()` methods

### 4. Package Structure
- **CODING_RULE_012**: Package hierarchy must match `mapping.json` package_path exactly
- **CODING_RULE_013**: Each class gets its own file in the matching directory
- **CODING_RULE_014**: `__init__.py` exports all classes in package

### 5. Splitable Elements
- **CODING_RULE_015**: Elements marked as `splitable: true` in mapping.json must include split metadata
- **CODING_RULE_016**: Splitable elements must have `get_split_filename()` method

### 6. Type Safety
- **CODING_RULE_017**: Use type hints for all class attributes
- **CODING_RULE_018**: Use Optional[T] for nullable attributes
- **CODING_RULE_019**: Document complex types with docstrings

### 7. Validation
- **CODING_RULE_020**: All attributes must be validated in `builder.build()` method
- **CODING_RULE_021**: Raise ValueError for invalid attribute values
- **CODING_RULE_022**: Validate required attributes are present

### 8. Documentation
- **CODING_RULE_023**: Each class must have a docstring
- **CODING_RULE_024**: Each method must have a docstring
- **CODING_RULE_025**: Document complex logic with inline comments

### 9. Testing
- **CODING_RULE_026**: Each class must have unit tests
- **CODING_RULE_027**: Tests must cover serialize/deserialize
- **CODING_RULE_028**: Tests must verify builder functionality

### 10. Code Quality
- **CODING_RULE_029**: No hardcoded values (use config where appropriate)
- **CODING_RULE_030**: Follow PEP 8 style guide
- **CODING_RULE_031**: Maximum line length 100 characters
