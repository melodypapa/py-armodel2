"""DiagnosticClearResetEmissionRelatedInfo AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticClearResetEmissionRelatedInfo(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticClearResetEmissionRelatedInfo."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("clear_reset", None, False, False, any (DiagnosticClearReset)),  # clearReset
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticClearResetEmissionRelatedInfo."""
        super().__init__()
        self.clear_reset: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticClearResetEmissionRelatedInfo to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticClearResetEmissionRelatedInfo":
        """Create DiagnosticClearResetEmissionRelatedInfo from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticClearResetEmissionRelatedInfo instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticClearResetEmissionRelatedInfo since parent returns ARObject
        return cast("DiagnosticClearResetEmissionRelatedInfo", obj)


class DiagnosticClearResetEmissionRelatedInfoBuilder:
    """Builder for DiagnosticClearResetEmissionRelatedInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticClearResetEmissionRelatedInfo = DiagnosticClearResetEmissionRelatedInfo()

    def build(self) -> DiagnosticClearResetEmissionRelatedInfo:
        """Build and return DiagnosticClearResetEmissionRelatedInfo object.

        Returns:
            DiagnosticClearResetEmissionRelatedInfo instance
        """
        # TODO: Add validation
        return self._obj
