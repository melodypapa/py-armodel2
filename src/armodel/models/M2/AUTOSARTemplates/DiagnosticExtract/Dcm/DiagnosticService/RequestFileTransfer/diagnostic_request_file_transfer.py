"""DiagnosticRequestFileTransfer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RequestFileTransfer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticRequestFileTransfer(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestFileTransfer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_file_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestFileTransfer."""
        super().__init__()
        self.request_file_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestFileTransfer to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestFileTransfer, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request_file_ref
        if self.request_file_ref is not None:
            serialized = ARObject._serialize_item(self.request_file_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-FILE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestFileTransfer":
        """Deserialize XML element to DiagnosticRequestFileTransfer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestFileTransfer object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestFileTransfer, cls).deserialize(element)

        # Parse request_file_ref
        child = ARObject._find_child_element(element, "REQUEST-FILE-REF")
        if child is not None:
            request_file_ref_value = ARRef.deserialize(child)
            obj.request_file_ref = request_file_ref_value

        return obj



class DiagnosticRequestFileTransferBuilder:
    """Builder for DiagnosticRequestFileTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestFileTransfer = DiagnosticRequestFileTransfer()

    def build(self) -> DiagnosticRequestFileTransfer:
        """Build and return DiagnosticRequestFileTransfer object.

        Returns:
            DiagnosticRequestFileTransfer instance
        """
        # TODO: Add validation
        return self._obj
