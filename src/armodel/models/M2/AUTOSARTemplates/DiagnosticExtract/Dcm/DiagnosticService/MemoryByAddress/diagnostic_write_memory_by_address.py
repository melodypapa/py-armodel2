"""DiagnosticWriteMemoryByAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticWriteMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticWriteMemoryByAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    write_class_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticWriteMemoryByAddress."""
        super().__init__()
        self.write_class_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticWriteMemoryByAddress to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticWriteMemoryByAddress, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize write_class_ref
        if self.write_class_ref is not None:
            serialized = ARObject._serialize_item(self.write_class_ref, "Any")
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

        # Parse write_class_ref
        child = ARObject._find_child_element(element, "WRITE-CLASS-REF")
        if child is not None:
            write_class_ref_value = ARRef.deserialize(child)
            obj.write_class_ref = write_class_ref_value

        return obj



class DiagnosticWriteMemoryByAddressBuilder:
    """Builder for DiagnosticWriteMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticWriteMemoryByAddress = DiagnosticWriteMemoryByAddress()

    def build(self) -> DiagnosticWriteMemoryByAddress:
        """Build and return DiagnosticWriteMemoryByAddress object.

        Returns:
            DiagnosticWriteMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
