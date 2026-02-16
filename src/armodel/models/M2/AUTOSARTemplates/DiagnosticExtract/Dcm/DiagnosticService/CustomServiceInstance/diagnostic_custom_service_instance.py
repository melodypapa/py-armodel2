"""DiagnosticCustomServiceInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticCustomServiceInstance(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticCustomServiceInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("custom_service", None, False, False, any (DiagnosticCustom)),  # customService
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticCustomServiceInstance."""
        super().__init__()
        self.custom_service: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticCustomServiceInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCustomServiceInstance":
        """Create DiagnosticCustomServiceInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticCustomServiceInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticCustomServiceInstance since parent returns ARObject
        return cast("DiagnosticCustomServiceInstance", obj)


class DiagnosticCustomServiceInstanceBuilder:
    """Builder for DiagnosticCustomServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCustomServiceInstance = DiagnosticCustomServiceInstance()

    def build(self) -> DiagnosticCustomServiceInstance:
        """Build and return DiagnosticCustomServiceInstance object.

        Returns:
            DiagnosticCustomServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
