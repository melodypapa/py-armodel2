"""DiagnosticSecurityAccess AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
    DiagnosticSecurityLevel,
)


class DiagnosticSecurityAccess(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSecurityAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request_seed_id", None, True, False, None),  # requestSeedId
        ("security_access", None, False, False, any (DiagnosticSecurity)),  # securityAccess
        ("security_delay", None, True, False, None),  # securityDelay
        ("security_level", None, False, False, DiagnosticSecurityLevel),  # securityLevel
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSecurityAccess."""
        super().__init__()
        self.request_seed_id: Optional[PositiveInteger] = None
        self.security_access: Optional[Any] = None
        self.security_delay: Optional[TimeValue] = None
        self.security_level: Optional[DiagnosticSecurityLevel] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSecurityAccess to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityAccess":
        """Create DiagnosticSecurityAccess from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSecurityAccess instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSecurityAccess since parent returns ARObject
        return cast("DiagnosticSecurityAccess", obj)


class DiagnosticSecurityAccessBuilder:
    """Builder for DiagnosticSecurityAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityAccess = DiagnosticSecurityAccess()

    def build(self) -> DiagnosticSecurityAccess:
        """Build and return DiagnosticSecurityAccess object.

        Returns:
            DiagnosticSecurityAccess instance
        """
        # TODO: Add validation
        return self._obj
