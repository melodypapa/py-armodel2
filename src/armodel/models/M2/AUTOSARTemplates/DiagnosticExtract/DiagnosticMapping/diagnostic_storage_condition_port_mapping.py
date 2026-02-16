"""DiagnosticStorageConditionPortMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticStorageConditionPortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_storage", None, False, False, any (DiagnosticStorage)),  # diagnosticStorage
        ("swc_flat_service", None, False, False, any (SwcService)),  # swcFlatService
        ("swc_service", None, False, False, any (SwcService)),  # swcService
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionPortMapping."""
        super().__init__()
        self.diagnostic_storage: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticStorageConditionPortMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionPortMapping":
        """Create DiagnosticStorageConditionPortMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticStorageConditionPortMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticStorageConditionPortMapping since parent returns ARObject
        return cast("DiagnosticStorageConditionPortMapping", obj)


class DiagnosticStorageConditionPortMappingBuilder:
    """Builder for DiagnosticStorageConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionPortMapping = DiagnosticStorageConditionPortMapping()

    def build(self) -> DiagnosticStorageConditionPortMapping:
        """Build and return DiagnosticStorageConditionPortMapping object.

        Returns:
            DiagnosticStorageConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
