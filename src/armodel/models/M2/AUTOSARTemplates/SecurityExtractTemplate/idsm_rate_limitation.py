"""IdsmRateLimitation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)


class IdsmRateLimitation(Identifiable):
    """AUTOSAR IdsmRateLimitation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_events_in", None, True, False, None),  # maxEventsIn
        ("time_interval", None, True, False, None),  # timeInterval
    ]

    def __init__(self) -> None:
        """Initialize IdsmRateLimitation."""
        super().__init__()
        self.max_events_in: PositiveInteger = None
        self.time_interval: Float = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsmRateLimitation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmRateLimitation":
        """Create IdsmRateLimitation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsmRateLimitation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsmRateLimitation since parent returns ARObject
        return cast("IdsmRateLimitation", obj)


class IdsmRateLimitationBuilder:
    """Builder for IdsmRateLimitation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmRateLimitation = IdsmRateLimitation()

    def build(self) -> IdsmRateLimitation:
        """Build and return IdsmRateLimitation object.

        Returns:
            IdsmRateLimitation instance
        """
        # TODO: Add validation
        return self._obj
