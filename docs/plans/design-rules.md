# Design Rules for py-armodel2

**Purpose:** Define rules for generating Python classes from mapping.json

## Rule Categories

Design rules are categorized by their type and scope:

### 1. Naming Conventions
- **DR-001**: File names must use snake_case
- **DR-002**: Class names must use PascalCase
- **DR-003**: Module names must use snake_case

### 2. Class Structure
- **DR-004**: Every generated class must inherit from ARObject
- **DR-005**: Class must include `serialize()` and `deserialize()` methods
- **DR-006**: Class must include a builder class for easy instantiation
- **DR-007**: Builder class must be named `<ClassName>Builder`

### 3. Serialization/Deserialization
- **DR-008**: `serialize()` returns `lxml.etree.Element`
- **DR-009**: `deserialize()` is a `@classmethod` accepting an element parameter
- **DR-010**: All child elements must be serialized using their `serialize()` methods
- **DR-011**: All child elements must be deserialized using `deserialize()` methods

### 4. Package Structure
- **DR-012**: Package hierarchy must match `mapping.json` package_path exactly
- **DR-013**: Each class gets its own file in the matching directory
- **DR-014**: `__init__.py` exports all classes in package

### 5. Splitable Elements
- **DR-015**: Elements marked as `splitable: true` in mapping.json must include split metadata
- **DR-016**: Splitable elements must have `get_split_filename()` method

### 6. Type Safety
- **DR-017**: Use type hints for all class attributes
- **DR-018**: Use Optional[T] for nullable attributes
- **DR-019**: Document complex types with docstrings

### 7. Validation
- **DR-020**: All attributes must be validated in `builder.build()` method
- **DR-021**: Raise ValueError for invalid attribute values
- **DR-022**: Validate required attributes are present

### 8. Documentation
- **DR-023**: Each class must have a docstring
- **DR-024**: Each method must have a docstring
- **DR-025**: Document complex logic with inline comments

### 9. Testing
- **DR-026**: Each class must have unit tests
- **DR-027**: Tests must cover serialize/deserialize
- **DR-028**: Tests must verify builder functionality

### 10. Code Quality
- **DR-029**: No hardcoded values (use config where appropriate)
- **DR-030**: Follow PEP 8 style guide
- **DR-031**: Maximum line length 100 characters
