"""ObdRatioServiceNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioServiceNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("connection_type", None, False, False, ObdRatioConnectionKindEnum),  # connectionType
        ("rate_based_monitored_event", None, False, False, DiagnosticEventNeeds),  # rateBasedMonitoredEvent
        ("used_fid", None, False, False, FunctionInhibitionNeeds),  # usedFid
    ]

    def __init__(self) -> None:
        """Initialize ObdRatioServiceNeeds."""
        super().__init__()
        self.connection_type: Optional[ObdRatioConnectionKindEnum] = None
        self.rate_based_monitored_event: Optional[DiagnosticEventNeeds] = None
        self.used_fid: Optional[FunctionInhibitionNeeds] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ObdRatioServiceNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdRatioServiceNeeds":
        """Create ObdRatioServiceNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ObdRatioServiceNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ObdRatioServiceNeeds since parent returns ARObject
        return cast("ObdRatioServiceNeeds", obj)


class ObdRatioServiceNeedsBuilder:
    """Builder for ObdRatioServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdRatioServiceNeeds = ObdRatioServiceNeeds()

    def build(self) -> ObdRatioServiceNeeds:
        """Build and return ObdRatioServiceNeeds object.

        Returns:
            ObdRatioServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
