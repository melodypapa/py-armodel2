"""DiagnosticRequestUpload AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 145)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticRequestUpload(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticRequestUpload."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_upload_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestUpload."""
        super().__init__()
        self.request_upload_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestUpload to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestUpload, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request_upload_ref
        if self.request_upload_ref is not None:
            serialized = ARObject._serialize_item(self.request_upload_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-UPLOAD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestUpload":
        """Deserialize XML element to DiagnosticRequestUpload object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestUpload object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestUpload, cls).deserialize(element)

        # Parse request_upload_ref
        child = ARObject._find_child_element(element, "REQUEST-UPLOAD-REF")
        if child is not None:
            request_upload_ref_value = ARRef.deserialize(child)
            obj.request_upload_ref = request_upload_ref_value

        return obj



class DiagnosticRequestUploadBuilder:
    """Builder for DiagnosticRequestUpload."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestUpload = DiagnosticRequestUpload()

    def build(self) -> DiagnosticRequestUpload:
        """Build and return DiagnosticRequestUpload object.

        Returns:
            DiagnosticRequestUpload instance
        """
        # TODO: Add validation
        return self._obj
