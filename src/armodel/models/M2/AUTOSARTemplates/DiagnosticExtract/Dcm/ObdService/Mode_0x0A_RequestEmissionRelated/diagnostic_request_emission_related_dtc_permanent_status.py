"""DiagnosticRequestEmissionRelatedDTCPermanentStatus AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x0A_RequestEmissionRelated.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestEmissionRelatedDTCPermanentStatus(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTCPermanentStatus."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestEmissionRelatedDTCPermanentStatus."""
        super().__init__()
        self.request: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestEmissionRelatedDTCPermanentStatus to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestEmissionRelatedDTCPermanentStatus, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request
        if self.request is not None:
            serialized = ARObject._serialize_item(self.request, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestEmissionRelatedDTCPermanentStatus":
        """Deserialize XML element to DiagnosticRequestEmissionRelatedDTCPermanentStatus object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestEmissionRelatedDTCPermanentStatus object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestEmissionRelatedDTCPermanentStatus, cls).deserialize(element)

        # Parse request
        child = ARObject._find_child_element(element, "REQUEST")
        if child is not None:
            request_value = child.text
            obj.request = request_value

        return obj



class DiagnosticRequestEmissionRelatedDTCPermanentStatusBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTCPermanentStatus."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTCPermanentStatus = DiagnosticRequestEmissionRelatedDTCPermanentStatus()

    def build(self) -> DiagnosticRequestEmissionRelatedDTCPermanentStatus:
        """Build and return DiagnosticRequestEmissionRelatedDTCPermanentStatus object.

        Returns:
            DiagnosticRequestEmissionRelatedDTCPermanentStatus instance
        """
        # TODO: Add validation
        return self._obj
