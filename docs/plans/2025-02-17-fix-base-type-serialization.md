# Fix BaseType serialize() and deserialize() Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix binary comparison test by implementing flat XML format handling in BaseType serialization/deserialization.

**Architecture:** Add `_extract_text()` helper to ARObject, implement flat format serialize/deserialize in BaseType parent class, remove duplicate code from SwBaseType. All BaseType subclasses inherit the fix.

**Tech Stack:** Python 3.9+, pytest, xml.etree.ElementTree, reflection-based deserialization framework

**Design reference:** `docs/plans/2025-02-17-fix-base-type-serialization-design.md`

---

## Task 1: Add `_extract_text()` Helper to ARObject

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

**Step 1: Read the ARObject file to understand structure**

Run: `head -300 src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

Look for existing static methods and where to add the new method (around line 285-298 after `_strip_namespace`).

**Step 2: Add `_extract_text()` static method after existing static methods**

Find the line with `_strip_namespace` method (around line 297). Add the following method after it:

```python
    @staticmethod
    def _extract_text(element: ET.Element) -> Optional[str]:
        """Extract text content from XML element, returning None if missing or empty.

        Protected static helper method for deserialization. Accessible to all subclasses.

        Args:
            element: XML element to extract text from

        Returns:
            Text content or None if element is missing or empty
        """
        if element is None or element.text is None:
            return None
        text = element.text.strip()
        return text if text else None
```

**Step 3: Verify the file compiles**

Run: `python -m py_compile src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

Expected: No output (successful compilation)

**Step 4: Run linter**

Run: `ruff check src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

Expected: No errors

**Step 5: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py
git commit -m "feat: Add _extract_text() helper to ARObject

Add protected static method for safely extracting text from XML elements.
Returns None for missing or empty elements. Reusable by all subclasses.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 2: Write Failing Tests for `_extract_text()`

**Files:**
- Create: `tests/unit/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/test_ar_object.py`

**Step 1: Check if test file exists**

Run: `ls tests/unit/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/test_ar_object.py 2>/dev/null || echo "File does not exist"`

**Step 2: Create test directory structure if needed**

Run: `mkdir -p tests/unit/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject`

**Step 3: Write test for `_extract_text()` with all edge cases**

Create `tests/unit/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/test_ar_object.py`:

```python
"""Unit tests for ARObject."""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
    ARObject,
)


class TestARObject:
    """Test ARObject base class."""

    def test_extract_text_with_valid_element(self):
        """Test _extract_text with valid element containing text."""
        elem = ET.Element('TEST')
        elem.text = "  value  "
        result = ARObject._extract_text(elem)
        assert result == "value", f"Expected 'value', got '{result}'"

    def test_extract_text_with_none(self):
        """Test _extract_text with None element."""
        result = ARObject._extract_text(None)
        assert result is None, f"Expected None, got {result}"

    def test_extract_text_with_empty_element(self):
        """Test _extract_text with element having no text."""
        elem = ET.Element('TEST')
        result = ARObject._extract_text(elem)
        assert result is None, f"Expected None, got {result}"

    def test_extract_text_with_whitespace_only(self):
        """Test _extract_text with element containing only whitespace."""
        elem = ET.Element('TEST')
        elem.text = "   "
        result = ARObject._extract_text(elem)
        assert result is None, f"Expected None for whitespace-only, got '{result}'"
```

**Step 4: Run tests to verify they pass**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/test_ar_object.py -v`

Expected: All 4 tests PASS

**Step 5: Commit**

```bash
git add tests/unit/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/test_ar_object.py
git commit -m "test: Add unit tests for ARObject._extract_text()

Test cases:
- Valid element with text (strips whitespace)
- None element (returns None)
- Empty element (returns None)
- Whitespace-only element (returns None)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Fix BaseType.serialize()

**Files:**
- Modify: `src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py`

**Step 1: Read the current BaseType file**

Run: `cat src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py`

Note the incomplete serialize() method (lines 32-48) and broken deserialize() method (lines 49-72).

**Step 2: Replace the serialize() method with complete implementation**

Find the serialize() method (starting at line 32). Replace the entire method with:

```python
    def serialize(self) -> ET.Element:
        """Serialize BaseType to XML element with flat structure.

        Outputs BASE-TYPE-SIZE, BASE-TYPE-ENCODING, etc. as direct children
        instead of wrapping them in BASE-TYPE-DEFINITION element.

        Returns:
            xml.etree.ElementTree.Element representing this BaseType
        """
        # Call parent serialize for inherited fields (short_name, category, etc.)
        elem = super().serialize()

        # Flatten base_type_definition fields as direct children
        if self.base_type_definition is not None:
            if hasattr(self.base_type_definition, 'base_type_size') and \
               self.base_type_definition.base_type_size is not None:
                child = ET.Element('BASE-TYPE-SIZE')
                child.text = str(self.base_type_definition.base_type_size)
                elem.append(child)

            if hasattr(self.base_type_definition, 'base_type_encoding') and \
               self.base_type_definition.base_type_encoding is not None:
                child = ET.Element('BASE-TYPE-ENCODING')
                child.text = str(self.base_type_definition.base_type_encoding)
                elem.append(child)

            if hasattr(self.base_type_definition, 'mem_alignment') and \
               self.base_type_definition.mem_alignment is not None:
                child = ET.Element('MEM-ALIGNMENT')
                child.text = str(self.base_type_definition.mem_alignment)
                elem.append(child)

            if hasattr(self.base_type_definition, 'byte_order') and \
               self.base_type_definition.byte_order is not None:
                child = ET.Element('BYTE-ORDER')
                child.text = str(self.base_type_definition.byte_order)
                elem.append(child)

            if hasattr(self.base_type_definition, 'native') and \
               self.base_type_definition.native is not None:
                child = ET.Element('NATIVE-DECLARATION')
                child.text = str(self.base_type_definition.native)
                elem.append(child)

        return elem
```

**Step 3: Verify the file compiles**

Run: `python -m py_compile src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py`

Expected: No output (successful compilation)

**Step 4: Run linter**

Run: `ruff check src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py`

Expected: No errors

**Step 5: Commit**

```bash
git add src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py
git commit -m "feat: Implement BaseType.serialize() with flat XML format

Override parent serialize() to output base_type_definition fields as
direct children (flat structure) instead of wrapping in BASE-TYPE-DEFINITION.

Calls super().serialize() for inherited fields, then appends each
base_type_definition field as direct child element.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Fix BaseType.deserialize()

**Files:**
- Modify: `src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py`

**Step 1: Replace the deserialize() method with working implementation**

Find the deserialize() method (starting at line 49). Replace the entire method with:

```python
    @classmethod
    def deserialize(cls, element: ET.Element) -> BaseType:
        """Deserialize XML element to BaseType with flat structure.

        Expects BASE-TYPE-SIZE, BASE-TYPE-ENCODING, etc. as direct children
        of the element (not wrapped in BASE-TYPE-DEFINITION).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BaseType object
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_direct_definition import BaseTypeDirectDefinition

        # Use parent's standard deserialize for common fields (short_name, category, etc.)
        obj = super().deserialize(element)

        # Create BaseTypeDirectDefinition and populate from direct children
        defn = BaseTypeDirectDefinition()
        defn.base_type_size = ARObject._extract_text(element.find('BASE-TYPE-SIZE'))
        defn.base_type_encoding = ARObject._extract_text(element.find('BASE-TYPE-ENCODING'))
        defn.mem_alignment = ARObject._extract_text(element.find('MEM-ALIGNMENT'))
        defn.byte_order = ARObject._extract_text(element.find('BYTE-ORDER'))
        defn.native = ARObject._extract_text(element.find('NATIVE-DECLARATION'))

        obj.base_type_definition = defn

        return obj
```

**Step 2: Verify the file compiles**

Run: `python -m py_compile src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py`

Expected: No output (successful compilation)

**Step 3: Run linter**

Run: `ruff check src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py`

Expected: No errors

**Step 4: Commit**

```bash
git add src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py
git commit -m "feat: Implement BaseType.deserialize() for flat XML format

Handle flat XML structure where BASE-TYPE-SIZE, BASE-TYPE-ENCODING, etc.
are direct children of the element (not wrapped in BASE-TYPE-DEFINITION).

Uses ARObject._extract_text() helper for safe text extraction.
Creates BaseTypeDirectDefinition and populates from direct child elements.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 5: Remove SwBaseType.serialize() Override

**Files:**
- Modify: `src/armodel/models/M2/MSR/AsamHdo/BaseTypes/sw_base_type.py`

**Step 1: Read the SwBaseType file**

Run: `cat src/armodel/models/M2/MSR/AsamHdo/BaseTypes/sw_base_type.py`

Note the custom serialize() method (lines 29-105) that is no longer needed.

**Step 2: Remove the custom serialize() method**

Delete lines 29-105 (the entire serialize() method). The file should now contain only:

```python
"""SwBaseType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 337)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 290)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2060)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type import (
    BaseType,
)


class SwBaseType(BaseType):
    """AUTOSAR SwBaseType."""

    def __init__(self) -> None:
        """Initialize SwBaseType."""
        super().__init__()


class SwBaseTypeBuilder:
    """Builder for SwBaseType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwBaseType = SwBaseType()

    def build(self) -> SwBaseType:
        """Build and return SwBaseType object.

        Returns:
            SwBaseType instance
        """
        # TODO: Add validation
        return self._obj
```

**Step 3: Verify the file compiles**

Run: `python -m py_compile src/armodel/models/M2/MSR/AsamHdo/BaseTypes/sw_base_type.py`

Expected: No output (successful compilation)

**Step 4: Run linter**

Run: `ruff check src/armodel/models/M2/MSR/AsamHdo/BaseTypes/sw_base_type.py`

Expected: No errors

**Step 5: Commit**

```bash
git add src/armodel/models/M2/MSR/AsamHdo/BaseTypes/sw_base_type.py
git commit -m "refactor: Remove SwBaseType.serialize() override

No longer needed - parent BaseType.serialize() now handles flat format
correctly. SwBaseType inherits the fixed implementation.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 6: Write Unit Tests for BaseType

**Files:**
- Create: `tests/unit/models/M2/MSR/AsamHdo/BaseTypes/test_base_type.py`

**Step 1: Create test directory structure**

Run: `mkdir -p tests/unit/models/M2/MSR/AsamHdo/BaseTypes`

**Step 2: Write comprehensive tests for BaseType serialize and deserialize**

Create `tests/unit/models/M2/MSR/AsamHdo/BaseTypes/test_base_type.py`:

```python
"""Unit tests for BaseType."""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_direct_definition import (
    BaseTypeDirectDefinition,
)


class TestBaseType:
    """Test BaseType serialization and deserialization."""

    def test_serialize_with_all_fields(self):
        """Test serialization with all base_type_definition fields present."""
        obj = SwBaseType()
        obj.short_name = "float32"
        obj.category = "FIXED_LENGTH"

        # Create base_type_definition with all fields
        defn = BaseTypeDirectDefinition()
        defn.base_type_size = "32"
        defn.base_type_encoding = "IEEE754"
        defn.mem_alignment = "32"
        defn.byte_order = "MOTOTOROLA"
        defn.native = "float"
        obj.base_type_definition = defn

        # Serialize
        elem = obj.serialize()

        # Verify tag name
        assert elem.tag == "SW-BASE-TYPE"

        # Verify direct children (flat structure)
        assert elem.find('SHORT-NAME').text == "float32"
        assert elem.find('CATEGORY').text == "FIXED_LENGTH"
        assert elem.find('BASE-TYPE-SIZE').text == "32"
        assert elem.find('BASE-TYPE-ENCODING').text == "IEEE754"
        assert elem.find('MEM-ALIGNMENT').text == "32"
        assert elem.find('BYTE-ORDER').text == "MOTOTOROLA"
        assert elem.find('NATIVE-DECLARATION').text == "float"

        # Verify NO BASE-TYPE-DEFINITION wrapper
        assert elem.find('BASE-TYPE-DEFINITION') is None, "Should be flat structure, no wrapper"

    def test_serialize_with_optional_fields_missing(self):
        """Test serialization with optional fields missing."""
        obj = SwBaseType()
        obj.short_name = "sint16"
        obj.category = "FIXED_LENGTH"

        # Create base_type_definition with only required fields
        defn = BaseTypeDirectDefinition()
        defn.base_type_size = "16"
        defn.base_type_encoding = "2C"
        defn.mem_alignment = "16"
        # byte_order and native omitted (None)
        obj.base_type_definition = defn

        # Serialize
        elem = obj.serialize()

        # Verify required fields present
        assert elem.find('BASE-TYPE-SIZE').text == "16"
        assert elem.find('BASE-TYPE-ENCODING').text == "2C"
        assert elem.find('MEM-ALIGNMENT').text == "16"

        # Verify optional fields NOT present
        assert elem.find('BYTE-ORDER') is None
        assert elem.find('NATIVE-DECLARATION') is None

    def test_deserialize_flat_format_all_fields(self):
        """Test deserializing flat XML format with all fields."""
        xml = """<SW-BASE-TYPE>
                  <SHORT-NAME>float32</SHORT-NAME>
                  <CATEGORY>FIXED_LENGTH</CATEGORY>
                  <BASE-TYPE-SIZE>32</BASE-TYPE-SIZE>
                  <BASE-TYPE-ENCODING>IEEE754</BASE-TYPE-ENCODING>
                  <MEM-ALIGNMENT>32</MEM-ALIGNMENT>
                  <BYTE-ORDER>MOTOTOROLA</BYTE-ORDER>
                  <NATIVE-DECLARATION>float</NATIVE-DECLARATION>
                </SW-BASE-TYPE>"""
        element = ET.fromstring(xml)
        obj = SwBaseType.deserialize(element)

        # Verify base object properties
        assert obj.short_name == "float32"
        assert obj.category == "FIXED_LENGTH"

        # Verify base_type_definition was created
        assert obj.base_type_definition is not None, "base_type_definition should not be None"
        assert isinstance(obj.base_type_definition, BaseTypeDirectDefinition)

        # Verify all fields were extracted
        assert obj.base_type_definition.base_type_size == "32"
        assert obj.base_type_definition.base_type_encoding == "IEEE754"
        assert obj.base_type_definition.mem_alignment == "32"
        assert obj.base_type_definition.byte_order == "MOTOTOROLA"
        assert obj.base_type_definition.native == "float"

    def test_deserialize_flat_format_missing_optional_fields(self):
        """Test deserializing flat XML format with optional fields missing."""
        xml = """<SW-BASE-TYPE>
                  <SHORT-NAME>sint16</SHORT-NAME>
                  <CATEGORY>FIXED_LENGTH</CATEGORY>
                  <BASE-TYPE-SIZE>16</BASE-TYPE-SIZE>
                  <BASE-TYPE-ENCODING>2C</BASE-TYPE-ENCODING>
                  <MEM-ALIGNMENT>16</MEM-ALIGNMENT>
                </SW-BASE-TYPE>"""
        element = ET.fromstring(xml)
        obj = SwBaseType.deserialize(element)

        assert obj.short_name == "sint16"
        assert obj.base_type_definition is not None

        # Verify required fields
        assert obj.base_type_definition.base_type_size == "16"
        assert obj.base_type_definition.base_type_encoding == "2C"
        assert obj.base_type_definition.mem_alignment == "16"

        # Verify optional fields are None
        assert obj.base_type_definition.byte_order is None
        assert obj.base_type_definition.native is None

    def test_round_trip_preserves_data(self):
        """Test that serialize -> deserialize -> serialize preserves data."""
        # Create original object
        obj1 = SwBaseType()
        obj1.short_name = "uint32"
        obj1.category = "FIXED_LENGTH"

        defn = BaseTypeDirectDefinition()
        defn.base_type_size = "32"
        defn.base_type_encoding = "2C"
        defn.mem_alignment = "32"
        defn.native = "unsigned int"
        obj1.base_type_definition = defn

        # Serialize
        elem1 = obj1.serialize()

        # Deserialize
        obj2 = SwBaseType.deserialize(elem1)

        # Serialize again
        elem2 = obj2.serialize()

        # Verify data preserved
        assert obj2.short_name == obj1.short_name
        assert obj2.category == obj1.category
        assert obj2.base_type_definition.base_type_size == obj1.base_type_definition.base_type_size
        assert obj2.base_type_definition.base_type_encoding == obj1.base_type_definition.base_type_encoding
        assert obj2.base_type_definition.mem_alignment == obj1.base_type_definition.mem_alignment
        assert obj2.base_type_definition.native == obj1.base_type_definition.native

        # Verify XML is identical (byte-for-byte)
        xml1 = ET.tostring(elem1, encoding='unicode')
        xml2 = ET.tostring(elem2, encoding='unicode')
        assert xml1 == xml2, "Round-trip should produce identical XML"
```

**Step 3: Run tests to verify they all pass**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/M2/MSR/AsamHdo/BaseTypes/test_base_type.py -v`

Expected: All 5 tests PASS

**Step 4: Commit**

```bash
git add tests/unit/models/M2/MSR/AsamHdo/BaseTypes/test_base_type.py
git commit -m "test: Add unit tests for BaseType serialize/deserialize

Test cases:
- Serialize with all fields (flat structure, no wrapper)
- Serialize with optional fields missing
- Deserialize flat format with all fields
- Deserialize flat format with missing optional fields
- Round-trip preserves data and produces identical XML

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 7: Verify Real File Deserialization Works

**Files:**
- Test: `tests/integration/test_autosar_datatypes.py`

**Step 1: Run integration test to verify binary comparison now passes**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_binary_file_comparison -v`

Expected: PASS (round-trip now produces byte-identical file)

**Step 2: If test fails, debug the issue**

Check which field is not being preserved by examining the diff:

Run: `diff demos/arxml/AUTOSAR_Datatypes.arxml /tmp/test_generated.arxml | head -50`

Look for missing fields or structure differences.

**Step 3: Run all integration tests**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py -v`

Expected:
- ✅ `test_binary_file_comparison` - PASS
- ✅ `test_xml_content_comparison` - PASS

**Step 4: No commit needed**

This is a verification step. If tests pass, proceed to next task. If tests fail, debug the implementation.

---

## Task 8: Run Full Test Suite

**Step 1: Run all unit tests**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/ -v --tb=short`

Expected: All tests pass (or pre-existing failures only)

**Step 2: Run all integration tests**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/ -v --tb=short`

Expected: All tests pass

**Step 3: Run linter**

Run: `ruff check src/ tests/`

Expected: No errors

**Step 4: Run type checker**

Run: `mypy src/`

Expected: No errors in modified files

**Step 5: Create summary of changes**

Run: `git log --oneline HEAD~7..HEAD`

This should show all commits from this implementation plan.

**Step 6: Final summary**

Report:
- Total files modified: 5 (ARObject, BaseType, SwBaseType, plus 2 test files)
- Total lines added: ~400
- Tests passing: All new unit tests + integration tests
- Binary comparison test: FIXED (now produces byte-identical output)
- Data loss issue: FIXED (all fields preserved during round-trip)

---

## Verification Checklist

After completing all tasks, verify:

- [ ] `ARObject._extract_text()` method added and tested
- [ ] `BaseType.serialize()` outputs flat format (no BASE-TYPE-DEFINITION wrapper)
- [ ] `BaseType.deserialize()` handles flat format
- [ ] `SwBaseType.serialize()` override removed (inherits from parent)
- [ ] Real file (AUTOSAR_Datatypes.arxml) round-trips correctly
- [ ] All fields (base_type_size, base_type_encoding, mem_alignment, native) preserved
- [ ] Binary comparison test passes (byte-identical output)
- [ ] All new code is linted and type-checked
- [ ] All commits have descriptive messages

---

## Notes

**Success Criteria:**
- Binary comparison test passes (byte-identical round-trip)
- All data preserved during serialization/deserialization
- Code is simpler (single implementation in parent class)
- All subclasses benefit from the fix

**Future Enhancements:**
- If other model classes have similar flat/nested format issues, consider adding a decorator to mark fields for flattened serialization
- The `_extract_text()` helper can be reused by other custom deserialize() methods
