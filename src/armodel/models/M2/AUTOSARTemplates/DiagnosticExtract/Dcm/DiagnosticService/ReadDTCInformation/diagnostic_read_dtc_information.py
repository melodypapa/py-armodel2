"""DiagnosticReadDTCInformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 136)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDTCInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadDTCInformation(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDTCInformation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    read: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDTCInformation."""
        super().__init__()
        self.read: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticReadDTCInformation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticReadDTCInformation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize read
        if self.read is not None:
            serialized = ARObject._serialize_item(self.read, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("READ")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDTCInformation":
        """Deserialize XML element to DiagnosticReadDTCInformation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDTCInformation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDTCInformation, cls).deserialize(element)

        # Parse read
        child = ARObject._find_child_element(element, "READ")
        if child is not None:
            read_value = child.text
            obj.read = read_value

        return obj



class DiagnosticReadDTCInformationBuilder:
    """Builder for DiagnosticReadDTCInformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDTCInformation = DiagnosticReadDTCInformation()

    def build(self) -> DiagnosticReadDTCInformation:
        """Build and return DiagnosticReadDTCInformation object.

        Returns:
            DiagnosticReadDTCInformation instance
        """
        # TODO: Add validation
        return self._obj
