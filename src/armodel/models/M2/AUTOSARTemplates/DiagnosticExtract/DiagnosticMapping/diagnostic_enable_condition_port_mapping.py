"""DiagnosticEnableConditionPortMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticEnableConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticEnableConditionPortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("enable_condition", None, False, False, any (DiagnosticEnable)),  # enableCondition
        ("swc_flat_service", None, False, False, any (SwcService)),  # swcFlatService
        ("swc_service", None, False, False, any (SwcService)),  # swcService
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionPortMapping."""
        super().__init__()
        self.enable_condition: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnableConditionPortMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnableConditionPortMapping":
        """Create DiagnosticEnableConditionPortMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnableConditionPortMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnableConditionPortMapping since parent returns ARObject
        return cast("DiagnosticEnableConditionPortMapping", obj)


class DiagnosticEnableConditionPortMappingBuilder:
    """Builder for DiagnosticEnableConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionPortMapping = DiagnosticEnableConditionPortMapping()

    def build(self) -> DiagnosticEnableConditionPortMapping:
        """Build and return DiagnosticEnableConditionPortMapping object.

        Returns:
            DiagnosticEnableConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
