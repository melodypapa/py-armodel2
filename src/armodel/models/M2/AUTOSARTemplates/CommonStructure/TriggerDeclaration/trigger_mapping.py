"""TriggerMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerMapping(ARObject):
    """AUTOSAR TriggerMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_trigger", None, False, False, Trigger),  # firstTrigger
        ("second_trigger", None, False, False, Trigger),  # secondTrigger
    ]

    def __init__(self) -> None:
        """Initialize TriggerMapping."""
        super().__init__()
        self.first_trigger: Optional[Trigger] = None
        self.second_trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TriggerMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerMapping":
        """Create TriggerMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TriggerMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TriggerMapping since parent returns ARObject
        return cast("TriggerMapping", obj)


class TriggerMappingBuilder:
    """Builder for TriggerMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerMapping = TriggerMapping()

    def build(self) -> TriggerMapping:
        """Build and return TriggerMapping object.

        Returns:
            TriggerMapping instance
        """
        # TODO: Add validation
        return self._obj
