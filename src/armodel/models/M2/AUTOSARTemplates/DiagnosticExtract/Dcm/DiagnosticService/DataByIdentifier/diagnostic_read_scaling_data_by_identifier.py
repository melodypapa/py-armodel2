"""DiagnosticReadScalingDataByIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)


class DiagnosticReadScalingDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticReadScalingDataByIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("read_scaling", None, False, False, any (DiagnosticReadScaling)),  # readScaling
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticReadScalingDataByIdentifier."""
        super().__init__()
        self.read_scaling: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticReadScalingDataByIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadScalingDataByIdentifier":
        """Create DiagnosticReadScalingDataByIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticReadScalingDataByIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticReadScalingDataByIdentifier since parent returns ARObject
        return cast("DiagnosticReadScalingDataByIdentifier", obj)


class DiagnosticReadScalingDataByIdentifierBuilder:
    """Builder for DiagnosticReadScalingDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadScalingDataByIdentifier = DiagnosticReadScalingDataByIdentifier()

    def build(self) -> DiagnosticReadScalingDataByIdentifier:
        """Build and return DiagnosticReadScalingDataByIdentifier object.

        Returns:
            DiagnosticReadScalingDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
