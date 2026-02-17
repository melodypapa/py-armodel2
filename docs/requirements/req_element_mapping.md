# Requirement: Element Mapping

## Requirement ID
REQ-ELEMENT-MAPPING-001

## Title
AUTOSAR ARXML Element to Python Class Mapping

## Version
1.0

## Status
Approved

## Priority
High

## Description
The py-armodel2 library shall provide a consistent and predictable mapping between AUTOSAR ARXML elements and Python model classes to enable reliable serialization and deserialization of AUTOSAR models.

## Requirements

### 1. Tag to Class Name Mapping
**REQ-ELEMENT-MAPPING-001.1:** The library shall convert AUTOSAR XML kebab-case tag names to Python PascalCase class names.

**Pattern:**
```
XML Tag:        <ELEMENT-NAME>
Python Class:   ElementName
```

**Examples:**
- `SW-BASE-TYPE` → `SwBaseType`
- `IMPLEMENTATION-DATA-TYPE` → `ImplementationDataType`
- `DATA-CONSTR` → `DataConstr`
- `COMPU-METHOD` → `CompuMethod`
- `AR-PACKAGE` → `ARPackage`
- `AUTOSAR` → `AUTOSAR` (special case: uppercase)

### 2. Attribute to Property Mapping
**REQ-ELEMENT-MAPPING-001.2:** The library shall convert AUTOSAR XML kebab-case attribute names to Python snake_case property names.

**Pattern:**
```
XML Attribute:  <ATTRIBUTE-NAME>
Python Attr:    attribute_name
```

**Examples:**
- `SHORT-NAME` → `short_name`
- `CATEGORY` → `category`
- `BASE-TYPE-SIZE` → `base_type_size`
- `SW-DATA-DEF-PROPS` → `sw_data_def_props`

### 3. Namespace Handling
**REQ-ELEMENT-MAPPING-001.3:** All XML serialization shall include namespace URIs, and all deserialization shall properly extract tag names from namespaced elements.

**Pattern:**
```python
# Serialization
if namespace:
    element = ET.Element(f"{{{namespace}}}ELEMENT-NAME")
else:
    element = ET.Element("ELEMENT-NAME")

# Deserialization
tag_name = child.tag.split("}")[-1] if "}" in child.tag else child.tag
```

### 4. Class Hierarchy
**REQ-ELEMENT-MAPPING-001.4:** All model classes shall inherit from appropriate base classes following the AUTOSAR specification hierarchy.

**Hierarchy:**
```
ARObject (abstract)
├── Referrable (adds short_name)
│   ├── Identifiable (adds identifier properties)
│   │   ├── Describable (adds description properties)
│   │   └── ARElement (AUTOSAR-specific)
│   └── PackageableElement (can be in packages)
│       └── CollectableElement (can be in collections)
│           └── ARPackage (package container)
└── [Generated AUTOSAR Classes]
```

### 5. Serialize/Deserialize Methods
**REQ-ELEMENT-MAPPING-001.5:** All model classes shall implement `serialize()` and `deserialize()` methods following consistent patterns.

**Method Signatures:**
```python
def serialize(self, namespace: Optional[str] = None) -> ET.Element:
    """Convert object to XML element."""
    pass

@classmethod
def deserialize(cls, element: ET.Element) -> "ClassName":
    """Create object from XML element."""
    pass
```

### 6. Type Multiplicity
**REQ-ELEMENT-MAPPING-001.6:** Type annotations shall correctly represent AUTOSAR multiplicities.

**Mapping:**
- `multiplicity: 1` → `Type`
- `multiplicity: 0..1` → `Optional[Type]`
- `multiplicity: *` → `List[Type]`

**Examples:**
```python
self.category: str  # Required
self.base_type_size: Optional[str] = None  # Optional
self.elements: List[PackageableElement] = []  # Multiple
```

### 7. Reference Handling
**REQ-ELEMENT-MAPPING-001.7:** AUTOSAR references shall be represented as string paths or typed reference objects.

**Pattern:**
```xml
<BASE-TYPE-REF DEST="SW-BASE-TYPE">/AUTOSAR_Platform/BaseTypes/float32</BASE-TYPE-REF>
```

**Python:**
```python
self.base_type_ref: Optional[str] = None
# or
self.base_type: Optional[SwBaseType] = None  # when resolved
```

### 8. Complex Nested Structures
**REQ-ELEMENT-MAPPING-001.8:** Complex nested AUTOSAR structures shall be implemented as separate Python classes.

**Example:**
```python
class DataConstr(Referrable):
    self.data_constr_rules: Optional[DataConstrRules] = None

class DataConstrRules(ARObject):
    self.rules: List[DataConstrRule] = []

class DataConstrRule(ARObject):
    self.internal_constrs: Optional[InternalConstrs] = None
```

### 9. Builder Pattern
**REQ-ELEMENT-MAPPING-001.9:** Each model class shall provide a Builder class for fluent API instantiation.

**Pattern:**
```python
class ClassNameBuilder:
    def with_attr(self, value: str) -> "ClassNameBuilder":
        self._obj.attr = value
        return self

    def build(self) -> ClassName:
        return self._obj
```

### 10. "Any" Type Handling
**REQ-ELEMENT-MAPPING-001.10:** AUTOSAR "any (...)" types shall be represented using Python `typing.Any`.

**Rationale:**
- AUTOSAR "any (...)" indicates multiple valid types
- Python `Any` provides necessary flexibility
- Matches AUTOSAR specification's open-ended intent

**Implementation:**
```python
from typing import Any, Optional

self.sub_elements: Optional[Any] = None  # "any (ImplementationData)"
```

### 11. Element Collection Dispatch
**REQ-ELEMENT-MAPPING-001.11:** Container classes shall use TAG_CLASS_MAP for dispatching XML tags to Python classes.

**Pattern:**
```python
class ARPackage(Referrable):
    TAG_CLASS_MAP = {
        "SW-BASE-TYPE": SwBaseType,
        "IMPLEMENTATION-DATA-TYPE": ImplementationDataType,
        "DATA-CONSTR": DataConstr,
        "COMPU-METHOD": CompuMethod,
    }
```

### 12. Attribute Value Representation
**REQ-ELEMENT-MAPPING-001.12:** Simple text content shall be stored as strings, numeric values as appropriate string types.

**Rationale:**
- AUTOSAR uses string representation for many numeric values
- Preserves exact XML format
- Type conversion can be done at runtime if needed

**Examples:**
```python
self.category: str = ""  # "FIXED_LENGTH", "STANDARD"
self.base_type_size: Optional[str] = None  # "32", "64"
```

## Acceptance Criteria

1. **AC-001:** All XML tags in AUTOSAR_Datatypes.arxml map to correct Python class names
2. **AC-002:** All XML attributes map to correct Python property names
3. **AC-003:** All namespaces are properly handled in serialization and deserialization
4. **AC-004:** All model classes follow the correct inheritance hierarchy
5. **AC-005:** All model classes implement serialize() and deserialize() methods
6. **AC-006:** All type annotations correctly represent AUTOSAR multiplicities
7. **AC-007:** All references are properly represented and can be resolved
8. **AC-008:** All complex nested structures are implemented as separate classes
9. **AC-009:** All model classes have corresponding Builder classes
10. **AC-010:** All "any (...)" types use Python `typing.Any`
11. **AC-011:** All container classes use TAG_CLASS_MAP for dispatch
12. **AC-012:** All attribute values preserve their string representation

## Verification

### Unit Tests
- Test tag to class name conversion
- Test attribute to property conversion
- Test namespace handling
- Test serialize/deserialize for each class
- Test type multiplicity
- Test reference handling
- Test builder pattern

### Integration Tests
- Test loading AUTOSAR_Datatypes.arxml
- Test round-trip read/write
- Test file comparison
- Test element counts and structure

### Code Review
- Verify all classes follow mapping patterns
- Verify all type annotations are correct
- Verify all namespaces are handled properly
- Verify all builders follow fluent API pattern

## References

- AUTOSAR Specification: XML schema definitions
- docs/armodel_element_mapping.md: Comprehensive pattern documentation
- docs/reports/any_type_analysis.md: "Any" type analysis
- tests/integration/test_autosar_datatypes.py: Integration tests

## History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-16 | py-armodel2 Team | Initial version |

## Related Requirements

- REQ-CODEGEN-001: Code generation requirements
- REQ-READER-001: ARXML reader requirements
- REQ-WRITER-001: ARXML writer requirements
- REQ-TEST-001: Testing requirements