"""DiagnosticServiceInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticServiceInstance(DiagnosticCommonElement):
    """AUTOSAR DiagnosticServiceInstance."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("access", None, False, False, DiagnosticAccessPermission),  # access
        ("service_class", None, False, False, DiagnosticServiceClass),  # serviceClass
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticServiceInstance."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None
        self.service_class: Optional[DiagnosticServiceClass] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticServiceInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceInstance":
        """Create DiagnosticServiceInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticServiceInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticServiceInstance since parent returns ARObject
        return cast("DiagnosticServiceInstance", obj)


class DiagnosticServiceInstanceBuilder:
    """Builder for DiagnosticServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceInstance = DiagnosticServiceInstance()

    def build(self) -> DiagnosticServiceInstance:
        """Build and return DiagnosticServiceInstance object.

        Returns:
            DiagnosticServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
