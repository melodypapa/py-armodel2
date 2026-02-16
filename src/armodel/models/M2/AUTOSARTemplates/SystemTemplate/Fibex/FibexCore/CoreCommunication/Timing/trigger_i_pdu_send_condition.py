"""TriggerIPduSendCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class TriggerIPduSendCondition(ARObject):
    """AUTOSAR TriggerIPduSendCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("modes", None, False, True, ModeDeclaration),  # modes
    ]

    def __init__(self) -> None:
        """Initialize TriggerIPduSendCondition."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TriggerIPduSendCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerIPduSendCondition":
        """Create TriggerIPduSendCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TriggerIPduSendCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TriggerIPduSendCondition since parent returns ARObject
        return cast("TriggerIPduSendCondition", obj)


class TriggerIPduSendConditionBuilder:
    """Builder for TriggerIPduSendCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerIPduSendCondition = TriggerIPduSendCondition()

    def build(self) -> TriggerIPduSendCondition:
        """Build and return TriggerIPduSendCondition object.

        Returns:
            TriggerIPduSendCondition instance
        """
        # TODO: Add validation
        return self._obj
