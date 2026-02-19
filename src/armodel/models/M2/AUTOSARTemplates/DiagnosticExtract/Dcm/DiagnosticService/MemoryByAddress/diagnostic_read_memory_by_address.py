"""DiagnosticReadMemoryByAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 141)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticReadMemoryByAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    read_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadMemoryByAddress."""
        super().__init__()
        self.read_class: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticReadMemoryByAddress to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticReadMemoryByAddress, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize read_class
        if self.read_class is not None:
            serialized = ARObject._serialize_item(self.read_class, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("READ-CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadMemoryByAddress":
        """Deserialize XML element to DiagnosticReadMemoryByAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadMemoryByAddress object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadMemoryByAddress, cls).deserialize(element)

        # Parse read_class
        child = ARObject._find_child_element(element, "READ-CLASS")
        if child is not None:
            read_class_value = child.text
            obj.read_class = read_class_value

        return obj



class DiagnosticReadMemoryByAddressBuilder:
    """Builder for DiagnosticReadMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadMemoryByAddress = DiagnosticReadMemoryByAddress()

    def build(self) -> DiagnosticReadMemoryByAddress:
        """Build and return DiagnosticReadMemoryByAddress object.

        Returns:
            DiagnosticReadMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
