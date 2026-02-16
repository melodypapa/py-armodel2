"""DiagnosticCapabilityElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagRequirementIdString,
    PositiveInteger,
)


class DiagnosticCapabilityElement(ServiceNeeds):
    """AUTOSAR DiagnosticCapabilityElement."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("audiences", None, False, True, DiagnosticAudienceEnum),  # audiences
        ("diag", None, True, False, None),  # diag
        ("security_access", None, True, False, None),  # securityAccess
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticCapabilityElement."""
        super().__init__()
        self.audiences: list[DiagnosticAudienceEnum] = []
        self.diag: Optional[DiagRequirementIdString] = None
        self.security_access: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticCapabilityElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCapabilityElement":
        """Create DiagnosticCapabilityElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticCapabilityElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticCapabilityElement since parent returns ARObject
        return cast("DiagnosticCapabilityElement", obj)


class DiagnosticCapabilityElementBuilder:
    """Builder for DiagnosticCapabilityElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCapabilityElement = DiagnosticCapabilityElement()

    def build(self) -> DiagnosticCapabilityElement:
        """Build and return DiagnosticCapabilityElement object.

        Returns:
            DiagnosticCapabilityElement instance
        """
        # TODO: Add validation
        return self._obj
