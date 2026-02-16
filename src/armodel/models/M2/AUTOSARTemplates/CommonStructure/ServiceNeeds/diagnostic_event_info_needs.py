"""DiagnosticEventInfoNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventInfoNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("obd_dtc_number", None, True, False, None),  # obdDtcNumber
        ("uds_dtc_number", None, True, False, None),  # udsDtcNumber
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventInfoNeeds."""
        super().__init__()
        self.obd_dtc_number: Optional[PositiveInteger] = None
        self.uds_dtc_number: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventInfoNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventInfoNeeds":
        """Create DiagnosticEventInfoNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventInfoNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventInfoNeeds since parent returns ARObject
        return cast("DiagnosticEventInfoNeeds", obj)


class DiagnosticEventInfoNeedsBuilder:
    """Builder for DiagnosticEventInfoNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventInfoNeeds = DiagnosticEventInfoNeeds()

    def build(self) -> DiagnosticEventInfoNeeds:
        """Build and return DiagnosticEventInfoNeeds object.

        Returns:
            DiagnosticEventInfoNeeds instance
        """
        # TODO: Add validation
        return self._obj
