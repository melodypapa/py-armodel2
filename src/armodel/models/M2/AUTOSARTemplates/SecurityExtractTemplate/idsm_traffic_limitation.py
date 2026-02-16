"""IdsmTrafficLimitation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)


class IdsmTrafficLimitation(Identifiable):
    """AUTOSAR IdsmTrafficLimitation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_bytes_in", None, True, False, None),  # maxBytesIn
        ("time_interval", None, True, False, None),  # timeInterval
    ]

    def __init__(self) -> None:
        """Initialize IdsmTrafficLimitation."""
        super().__init__()
        self.max_bytes_in: Optional[PositiveInteger] = None
        self.time_interval: Optional[Float] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsmTrafficLimitation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmTrafficLimitation":
        """Create IdsmTrafficLimitation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsmTrafficLimitation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsmTrafficLimitation since parent returns ARObject
        return cast("IdsmTrafficLimitation", obj)


class IdsmTrafficLimitationBuilder:
    """Builder for IdsmTrafficLimitation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmTrafficLimitation = IdsmTrafficLimitation()

    def build(self) -> IdsmTrafficLimitation:
        """Build and return IdsmTrafficLimitation object.

        Returns:
            IdsmTrafficLimitation instance
        """
        # TODO: Add validation
        return self._obj
