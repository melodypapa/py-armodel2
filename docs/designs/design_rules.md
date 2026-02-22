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
- **DESIGN_RULE_008**: `serialize(namespace: str)` returns `xml.etree.ElementTree.Element`
- **DESIGN_RULE_009**: `deserialize()` is a `@classmethod` accepting an `element: ET.Element` parameter
- **DESIGN_RULE_010**: All child elements must be serialized using their `serialize()` methods
- **DESIGN_RULE_011**: All child elements must be deserialized using their `deserialize()` methods
- **DESIGN_RULE_012**: Use `vars()` for automatic attribute discovery in serialization
- **DESIGN_RULE_013**: Use `get_type_hints()` for type-based deserialization
- **DESIGN_RULE_014**: All class attributes must have type hints at class level (not just in `__init__`)
- **DESIGN_RULE_015**: Use `NameConverter.to_xml_tag()` for snake_case → UPPER-CASE-WITH-HYPHENS conversion
- **DESIGN_RULE_016**: Use `@xml_attribute` decorator for XML attributes (instead of elements) - see `docs/designs/decorators.md` for complete decorator documentation
- **DESIGN_RULE_017**: XML tag names are automatically generated from class names
- **DESIGN_RULE_018**: List attributes create wrapper elements (e.g., `ar_packages` → `<AR-PACKAGES>`)

### 4. Package Structure
- **DESIGN_RULE_019**: Package hierarchy must match `mapping.json` package_path exactly
- **DESIGN_RULE_020**: Each class gets its own file in the matching directory
- **DESIGN_RULE_021**: `__init__.py` exports all classes in package

### 5. Splitable Elements
- **DESIGN_RULE_022**: Elements marked as `splitable: true` in mapping.json must include split metadata
- **DESIGN_RULE_023**: Splitable elements must have `get_split_filename()` method

### 6. Type Safety
- **DESIGN_RULE_024**: Use type hints for all class attributes
- **DESIGN_RULE_025**: Use Optional[T] for nullable attributes
- **DESIGN_RULE_026**: Document complex types with docstrings

### 7. Validation
- **DESIGN_RULE_027**: All attributes must be validated in `builder.build()` method
- **DESIGN_RULE_028**: Raise ValueError for invalid attribute values
- **DESIGN_RULE_029**: Validate required attributes are present

### 8. Documentation
- **DESIGN_RULE_030**: Each class must have a docstring
- **DESIGN_RULE_031**: Each method must have a docstring
- **DESIGN_RULE_032**: Document complex logic with inline comments

### 9. Testing
- **DESIGN_RULE_033**: Each class must have unit tests
- **DESIGN_RULE_034**: Tests must cover serialize/deserialize
- **DESIGN_RULE_035**: Tests must verify builder functionality

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
- **DESIGN_RULE_041**: Use block import statements and define __all__ in __init__.py files
  - Use full absolute imports with block format (multi-line with parentheses)
  - Block import format for single class: `from armodel.models.M2.AUTOSARTemplates.Package.module import (\n    Class,\n)`
  - Block import format for multiple classes: `from armodel.models.M2.AUTOSARTemplates.Package.module import (\n    Class1,\n    Class2,\n    Class3,\n)`
  - Avoid wildcard imports (`from module import *`) in production code
  - Prefer explicit imports over `__init__.py` re-exports when possible to clarify dependencies
  - Every `__init__.py` file must define `__all__` to explicitly list public exports
  - `__all__` should contain only the public API classes and functions intended for external use
  - Use alphabetical ordering for `__all__` entries to improve maintainability
  - Example:
    ```python
    # __init__.py
    from armodel.models.M2.AUTOSARTemplates.Package.some_class import (
        SomeClass,
    )
    from armodel.models.M2.AUTOSARTemplates.Package.another_class import (
        AnotherClass,
    )

    __all__ = [
        "AnotherClass",
        "SomeClass",
    ]
    ```
  - Block import format improves readability and makes it easier to add/remove imports
  - This enables safe star imports (`from package import *`) and clarifies the public API
  - Exclude internal implementation details from `__all__` (e.g., private classes starting with underscore)
- **DESIGN_RULE_042**: Use `from __future__ import annotations` combined with TYPE_CHECKING for circular imports
  - Add `from __future__ import annotations` at the top of files that may have circular dependencies
  - Use `TYPE_CHECKING` to import classes only for type hints: `if TYPE_CHECKING: from ... import SomeClass`
  - For `_xml_members` tuples that reference classes involved in circular imports, use string class names instead of class objects
  - Example: `_xml_members = [("item_contents", None, False, False, "DocumentationBlock")]`
  - The `ARObject.deserialize()` method automatically resolves string class names to actual class objects
  - This approach maintains type safety (annotations are strings and not evaluated at runtime) while avoiding circular imports
- **DESIGN_RULE_042**: Handle circular imports using future annotations and TYPE_CHECKING
  - When circular imports are unavoidable, use `from __future__ import annotations` at the top of the file
  - Use `TYPE_CHECKING` to import types only for type checking, not at runtime
  - Use lazy import functions for classes needed in `_xml_members` to break circular dependencies
  - Example pattern:
    ```python
    from __future__ import annotations  # Must be first import
    from typing import TYPE_CHECKING
    
    if TYPE_CHECKING:
        from armodel.models.M2.SomeModule import SomeClass
    
    def _get_some_class():
        from armodel.models.M2.SomeModule import SomeClass
        return SomeClass
    
    class MyClass:
        _xml_members = [("attr", None, False, False, _get_some_class)]
        
        def __init__(self) -> None:
            self.attr: SomeClass = None  # Type hint works because of future annotations
    ```
