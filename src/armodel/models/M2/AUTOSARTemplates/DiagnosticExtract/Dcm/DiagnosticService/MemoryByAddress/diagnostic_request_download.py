"""DiagnosticRequestDownload AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 144)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticRequestDownload(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticRequestDownload."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestDownload."""
        super().__init__()
        self.request_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestDownload to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestDownload, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request_ref
        if self.request_ref is not None:
            serialized = ARObject._serialize_item(self.request_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestDownload":
        """Deserialize XML element to DiagnosticRequestDownload object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestDownload object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestDownload, cls).deserialize(element)

        # Parse request_ref
        child = ARObject._find_child_element(element, "REQUEST-REF")
        if child is not None:
            request_ref_value = ARRef.deserialize(child)
            obj.request_ref = request_ref_value

        return obj



class DiagnosticRequestDownloadBuilder:
    """Builder for DiagnosticRequestDownload."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestDownload = DiagnosticRequestDownload()

    def build(self) -> DiagnosticRequestDownload:
        """Build and return DiagnosticRequestDownload object.

        Returns:
            DiagnosticRequestDownload instance
        """
        # TODO: Add validation
        return self._obj
