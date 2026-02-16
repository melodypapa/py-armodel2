"""FunctionInhibitionAvailabilityNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):
    """AUTOSAR FunctionInhibitionAvailabilityNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("controlled_fid", None, False, False, FunctionInhibitionNeeds),  # controlledFid
    ]

    def __init__(self) -> None:
        """Initialize FunctionInhibitionAvailabilityNeeds."""
        super().__init__()
        self.controlled_fid: Optional[FunctionInhibitionNeeds] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FunctionInhibitionAvailabilityNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FunctionInhibitionAvailabilityNeeds":
        """Create FunctionInhibitionAvailabilityNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FunctionInhibitionAvailabilityNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FunctionInhibitionAvailabilityNeeds since parent returns ARObject
        return cast("FunctionInhibitionAvailabilityNeeds", obj)


class FunctionInhibitionAvailabilityNeedsBuilder:
    """Builder for FunctionInhibitionAvailabilityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FunctionInhibitionAvailabilityNeeds = FunctionInhibitionAvailabilityNeeds()

    def build(self) -> FunctionInhibitionAvailabilityNeeds:
        """Build and return FunctionInhibitionAvailabilityNeeds object.

        Returns:
            FunctionInhibitionAvailabilityNeeds instance
        """
        # TODO: Add validation
        return self._obj
