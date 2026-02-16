"""DiagnosticRequestControlOfOnBoardDeviceClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRequestControlOfOnBoardDeviceClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDeviceClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDeviceClass."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestControlOfOnBoardDeviceClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestControlOfOnBoardDeviceClass":
        """Create DiagnosticRequestControlOfOnBoardDeviceClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestControlOfOnBoardDeviceClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestControlOfOnBoardDeviceClass since parent returns ARObject
        return cast("DiagnosticRequestControlOfOnBoardDeviceClass", obj)


class DiagnosticRequestControlOfOnBoardDeviceClassBuilder:
    """Builder for DiagnosticRequestControlOfOnBoardDeviceClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestControlOfOnBoardDeviceClass = DiagnosticRequestControlOfOnBoardDeviceClass()

    def build(self) -> DiagnosticRequestControlOfOnBoardDeviceClass:
        """Build and return DiagnosticRequestControlOfOnBoardDeviceClass object.

        Returns:
            DiagnosticRequestControlOfOnBoardDeviceClass instance
        """
        # TODO: Add validation
        return self._obj
