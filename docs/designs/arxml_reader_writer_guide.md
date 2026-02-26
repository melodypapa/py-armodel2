# ARXML Reader and Writer Guide

## Overview

This guide provides a comprehensive overview of the ARXML reader and writer functionality in py-armodel2, including the serialization and deserialization mechanisms.

## Architecture

### System Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              ARXML I/O System                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐         ┌──────────────┐         ┌──────────────┐        │
│  │   ARXML File │────────>│ ARXMLReader  │────────>│  AUTOSAR     │        │
│  │  (.arxml)    │         │              │         │   Object     │        │
│  └──────────────┘         └──────────────┘         └──────┬───────┘        │
│                                                                  │           │
│                                                                  │           │
│                                         ┌────────────────────────┼───────┐   │
│                                         │                        │       │   │
│                                         ▼                        ▼       │   │
│                                  ┌──────────────┐        ┌───────────┐  │   │
│                                  │ ARXMLWriter  │<───────│ serialize │  │   │
│                                  │              │        │           │  │   │
│                                  └──────┬───────┘        └───────────┘  │   │
│                                         │                                │   │
│                                         │                                │   │
│                                  ┌──────▼───────┐                        │   │
│                                  │   ARXML File │                        │   │
│                                  │  (.arxml)    │                        │   │
│                                  └──────────────┘                        │   │
│                                         ▲                                │   │
│                                         │                                │   │
│                                         │                                │   │
│                                  ┌──────┴───────┐                        │   │
│                                  │  deserialize │                        │   │
│                                  │              │                        │   │
│                                  └──────────────┘                        │   │
│                                         │                                │   │
│                                         ▼                                │   │
│                                  ┌──────────────┐                        │   │
│                                  │   ARObject   │                        │   │
│                                  │   (Base)     │                        │   │
│                                  └──────────────┘                        │   │
│                                         │                                │   │
│                                         ▼                                │   │
│                                  ┌──────────────┐                        │   │
│                                  │ NameConverter│                        │   │
│                                  │              │                        │   │
│                                  └──────────────┘                        │   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Serialization/Deserialization Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Serialization Flow                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Python Object                    XML Element                               │
│  ┌──────────────┐                 ┌──────────────┐                         │
│  │ ARObject     │                 │ <AUTOSAR>    │                         │
│  │  ├─attr1     │  serialize()    │   <ATTR-1>   │                         │
│  │  ├─attr2     │────────────────>│   <ATTR-2>   │                         │
│  │  └─children  │                 │   <CHILDREN> │                         │
│  └──────────────┘                 └──────────────┘                         │
│                                                                             │
│  Steps:                                                                    │
│  1. Get XML tag name (via NameConverter)                      │
│  2. Iterate attributes via vars(self)                                     │
│  3. Convert names: snake_case → UPPER-CASE-WITH-HYPHENS                    │
│  4. Serialize objects, lists, or primitives                               │
│  5. Handle @xml_attribute decorator                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         Deserialization Flow                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  XML Element                    Python Object                               │
│  ┌──────────────┐                 ┌──────────────┐                         │
│  │ <AUTOSAR>    │                 │ ARObject     │                         │
│  │   <ATTR-1>   │  deserialize()  │  ├─attr1     │                         │
│  │   <ATTR-2>   │<────────────────│  ├─attr2     │                         │
│  │   <CHILDREN> │                 │  └─children  │                         │
│  └──────────────┘                 └──────────────┘                         │
│                                                                             │
│  Steps:                                                                    │
│  1. Create instance via cls.__new__(cls)                                  │
│  2. Get type hints via get_type_hints()                                   │
│  3. For each attribute, find matching XML element/attribute                │
│  4. Parse value based on type hint                                         │
│  5. Recursively deserialize child objects                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Name Conversion

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        NameConverter Mappings                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Python Attributes (snake_case)       XML Tags (UPPER-CASE-WITH-HYPHENS)    │
│  ─────────────────────────────────    ─────────────────────────────────    │
│  short_name                         →  SHORT-NAME                          │
│  sw_data_def_props                  →  SW-DATA-DEF-PROPS                   │
│  compu_internal_to_phys             →  COMPU-INTERNAL-TO-PHYS              │
│                                                                             │
│  Python Classes (PascalCase)         XML Tags (UPPER-CASE-WITH-HYPHENS)    │
│  ────────────────────────────────    ─────────────────────────────────    │
│  ARPackage                          →  ARPACKAGE                           │
│  SwBaseType                         →  SW-BASE-TYPE                        │
│  ImplementationDataType             →  IMPLEMENTATION-DATA-TYPE            │
│  AUTOSAR                            →  AUTOSAR (exception)                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. ARObject Base Class

**Location:** `src/armodel2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

The `ARObject` class is the foundation for all AUTOSAR model classes, providing reflection-based serialization.

**Key Methods:**

```python
class ARObject:
    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize object to XML using reflection.
        
        Uses vars() to discover all attributes and converts them
        via NameConverter.to_xml_tag().
        """
        pass
    
    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML to Python object.
        
        Uses get_type_hints() for type information and recursively
        deserializes child objects.
        """
        pass
```

### 2. NameConverter

**Location:** `src/armodel2/serialization/name_converter.py`

Handles bidirectional name conversion between Python and AUTOSAR XML naming conventions.

**Key Methods:**

```python
class NameConverter:
    @staticmethod
    def to_xml_tag(name: str) -> str:
        """Convert Python name to XML tag.
        
        Examples:
            short_name → SHORT-NAME
            SwBaseType → SW-BASE-TYPE
        """
        pass
    
    @staticmethod
    def to_python_name(tag: str) -> str:
        """Convert XML tag to Python name.
        
        Examples:
            SHORT-NAME → short_name
            SW-DATA-DEF-PROPS → sw_data_def_props
        """
        pass
    
    @staticmethod
    def tag_to_class_name(tag: str) -> str:
        """Convert XML tag to class name.
        
        Examples:
            SW-BASE-TYPE → SwBaseType
            AR-PACKAGE → ARPackage
        """
        pass
```

### 3. ARXMLReader

**Location:** `src/armodel2/reader/reader.py`

Handles loading ARXML files and merging multiple files into a single AUTOSAR instance.

**Key Features:**
- Merge support: Multiple ARXML files can be loaded into the same AUTOSAR instance
- Schema version detection: Automatically detects AUTOSAR schema version
- Namespace handling: Properly manages XML namespaces

**Usage:**

```python
from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel2.reader import ARXMLReader

# Create AUTOSAR instance
autosar = AUTOSAR()

# Load multiple files into same instance
reader = ARXMLReader()
reader.load_arxml(autosar, "demos/arxml/AUTOSAR_Datatypes.arxml")
reader.load_arxml(autosar, "demos/arxml/another_file.arxml")

# Packages from multiple files are merged
print(f"Total packages: {len(autosar.ar_packages)}")
```

### 4. ARXMLWriter

**Location:** `src/armodel2/writer/writer.py`

Handles serializing AUTOSAR objects and saving to ARXML files.

**Key Features:**
- Pretty printing: Configurable indentation for readable XML
- Double quotes: XML declaration uses double quotes (<?xml version="1.0" encoding="UTF-8"?>)
- UTF-8 encoding: Default encoding for all files
- Namespace support: Handles XML namespaces correctly

**Usage:**

```python
from armodel2.writer import ARXMLWriter

writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
writer.save_arxml(autosar, "output.arxml")

# Or convert to string
xml_string = writer.to_string(autosar)
```

## Type Hints and Multiplicity

| AUTOSAR Multiplicity | Python Type          | Initial Value |
|---------------------|----------------------|---------------|
| `0..1`              | `Optional[Type]`     | `None`        |
| `1`                 | `Type`               | `None`        |
| `*`                 | `list[Type]`         | `[]`          |
| `0..*`              | `list[Type]`         | `[]`          |

## Common Patterns

### Pattern 1: Simple Class (No Decorators)

```python
class ARPackage(ARObject):
    short_name: Optional[str] = None
    ar_packages: list[ARPackage] = []
```

**Serialized XML:**
```xml
<AR-PACKAGES>
  <SHORT-NAME>MyPackage</SHORT-NAME>
  <AR-PACKAGES>
    <!-- Nested packages -->
  </AR-PACKAGES>
</AR-PACKAGES>
```

### Pattern 2: XML Attribute

```python
class AUTOSAR(ARObject):
    def __init__(self) -> None:
        self._schema_version: str = "4.5.0"
    
    @xml_attribute
    @property
    def schema_version(self) -> str:
        return self._schema_version
```

**Serialized XML:**
```xml
<AUTOSAR schema-version="4.5.0">
  <!-- Content -->
</AUTOSAR>
```

### Pattern 3: Custom Tag Name

```python
class AUTOSAR(ARObject):
    pass
```

## Demonstration

### Example 1: Reading and Writing ARXML

```python
#!/usr/bin/env python3
"""Demonstration of ARXML reader and writer."""

from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel2.reader import ARXMLReader
from armodel2.writer import ARXMLWriter

# Step 1: Create AUTOSAR instance
autosar = AUTOSAR()

# Step 2: Load ARXML file
print("Loading ARXML file...")
reader = ARXMLReader()
reader.load_arxml(autosar, "demos/arxml/AUTOSAR_Datatypes.arxml")

# Step 3: Inspect loaded data
print(f"\nLoaded {len(autosar.ar_packages)} packages")
for pkg in autosar.ar_packages:
    print(f"  - {pkg.short_name}")

# Step 4: Write to new file
print("\nWriting to output file...")
writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
writer.save_arxml(autosar, "output.arxml")

print("✓ Successfully written to output.arxml")

# Step 5: Verify by reading back
print("\nVerifying output...")
autosar2 = AUTOSAR()
reader2 = ARXMLReader()
reader2.load_arxml(autosar2, "output.arxml")
print(f"✓ Verified {len(autosar2.ar_packages)} packages")
```

**Output:**
```
Loading ARXML file...

Loaded 4 packages
  - AUTOSAR_Platform
  - AUTOSAR_BaseTypes
  - AUTOSAR_ImplementationDataTypes
  - AUTOSAR_CompuMethods

Writing to output file...
✓ Successfully written to output.arxml

Verifying output...
✓ Verified 4 packages
```

### Example 2: Merge Multiple Files

```python
#!/usr/bin/env python3
"""Demonstration of merging multiple ARXML files."""

from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel2.reader import ARXMLReader
from armodel2.writer import ARXMLWriter

# Create AUTOSAR instance
autosar = AUTOSAR()

# Load multiple files
reader = ARXMLReader()
files = [
    "demos/arxml/AUTOSAR_Datatypes.arxml",
    "demos/arxml/AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml",
]

for file_path in files:
    print(f"Loading {file_path}...")
    reader.load_arxml(autosar, file_path)

# All packages are merged into autosar.ar_packages
print(f"\nTotal packages after merge: {len(autosar.ar_packages)}")

# Write merged result
writer = ARXMLWriter(pretty_print=True)
writer.save_arxml(autosar, "merged.arxml")
print("✓ Merged output written to merged.arxml")
```

### Example 3: Using to_string()

```python
#!/usr/bin/env python3
"""Demonstration of XML string conversion."""

from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel2.reader import ARXMLReader
from armodel2.writer import ARXMLWriter

# Load file
autosar = AUTOSAR()
reader = ARXMLReader()
reader.load_arxml(autosar, "demos/arxml/AUTOSAR_Datatypes.arxml")

# Convert to string
writer = ARXMLWriter()
xml_string = writer.to_string(autosar)

# Print first few lines
lines = xml_string.split('\n')
print("First 5 lines of XML:")
for line in lines[:5]:
    print(line)
```

**Output:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR schema-version="4.5.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>AUTOSAR_Platform</SHORT-NAME>
```

### Example 4: Round-Trip Test

```python
#!/usr/bin/env python3
"""Demonstration of round-trip serialization."""

from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel2.reader import ARXMLReader
from armodel2.writer import ARXMLWriter

# Load original file
print("Loading original file...")
autosar1 = AUTOSAR()
reader = ARXMLReader()
reader.load_arxml(autosar1, "demos/arxml/AUTOSAR_Datatypes.arxml")

# Write to temp file
print("Writing to temp file...")
writer = ARXMLWriter()
writer.save_arxml(autosar1, "temp.arxml")

# Read back
print("Reading back...")
autosar2 = AUTOSAR()
reader2 = ARXMLReader()
reader2.load_arxml(autosar2, "temp.arxml")

# Compare
pkg_count1 = len(autosar1.ar_packages)
pkg_count2 = len(autosar2.ar_packages)

print(f"\nOriginal packages: {pkg_count1}")
print(f"Round-trip packages: {pkg_count2}")

if pkg_count1 == pkg_count2:
    print("✓ Round-trip successful!")
else:
    print("✗ Round-trip failed!")
```

## XML Declaration

The ARXMLWriter generates XML declarations with double quotes:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

This is achieved by post-processing the output to replace single quotes with double quotes in both file and string outputs.

## Performance Considerations

### Serialization Performance
- Reflection-based: Uses `vars()` for attribute discovery
- No boilerplate: Automatic attribute serialization reduces code
- Type hints: Used for deserialization, not serialization

### Deserialization Performance
- Type hints required: All class attributes must have type hints
- Recursive: Nested objects are deserialized recursively
- Factory pattern: ModelFactory caches class imports for performance

## Best Practices

1. **Always use type hints** - Required for deserialization
2. **Initialize attributes** - Set default values (None, []) in __init__
3. **Use Optional for nullable fields** - Matches AUTOSAR 0..1 multiplicity
4. **Use lists for collections** - Matches AUTOSAR * multiplicity
5. **Handle circular imports** - Use TYPE_CHECKING and forward references

## Troubleshooting

### Common Issues

**Issue: "Unrecognized XML element" warning**
- Cause: XML element doesn't match any class attribute
- Solution: Add missing attribute with proper type hint

**Issue: Serialization produces incorrect tag names**
- Cause: Name conversion mismatch
- Solution: Check NameConverter.to_xml_tag() output

**Issue: Deserialization returns None values**
- Cause: Type hints missing or incorrect
- Solution: Add proper type hints to all attributes

## References

- **Serialization Framework:** `docs/designs/serialization.md`
- **XML Serialization Decorators:** `docs/designs/decorators.md`
- **Design Rules:** `docs/designs/design_rules.md`
- **Model Design:** `docs/designs/model_design.md`
- **Integration Tests:** `docs/tests/integration/test_autosar_data_types.md`