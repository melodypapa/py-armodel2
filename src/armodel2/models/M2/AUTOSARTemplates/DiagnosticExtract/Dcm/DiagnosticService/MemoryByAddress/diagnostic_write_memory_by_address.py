"""DiagnosticWriteMemoryByAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import DiagnosticMemoryAddressableRangeAccessBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticWriteMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticWriteMemoryByAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS"


    write_class_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "WRITE-CLASS-REF": lambda obj, elem: setattr(obj, "write_class_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticWriteMemoryByAddress."""
        super().__init__()
        self.write_class_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticWriteMemoryByAddress to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticWriteMemoryByAddress, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize write_class_ref
        if self.write_class_ref is not None:
            serialized = SerializationHelper.serialize_item(self.write_class_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITE-CLASS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticWriteMemoryByAddress":
        """Deserialize XML element to DiagnosticWriteMemoryByAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticWriteMemoryByAddress object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticWriteMemoryByAddress, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "WRITE-CLASS-REF":
                setattr(obj, "write_class_ref", ARRef.deserialize(child))

        return obj



class DiagnosticWriteMemoryByAddressBuilder(DiagnosticMemoryAddressableRangeAccessBuilder):
    """Builder for DiagnosticWriteMemoryByAddress with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticWriteMemoryByAddress = DiagnosticWriteMemoryByAddress()


    def with_write_class(self, value: Optional[Any]) -> "DiagnosticWriteMemoryByAddressBuilder":
        """Set write_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'write_class' is required and cannot be None")
        self._obj.write_class = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "writeClass",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticWriteMemoryByAddress:
        """Build and return the DiagnosticWriteMemoryByAddress instance with validation."""
        self._validate_instance()
        return self._obj