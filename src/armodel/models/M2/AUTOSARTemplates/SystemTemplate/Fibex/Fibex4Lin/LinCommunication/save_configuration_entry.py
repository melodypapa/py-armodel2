"""SaveConfigurationEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)


class SaveConfigurationEntry(LinConfigurationEntry):
    """AUTOSAR SaveConfigurationEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SaveConfigurationEntry."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SaveConfigurationEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SaveConfigurationEntry":
        """Create SaveConfigurationEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SaveConfigurationEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SaveConfigurationEntry since parent returns ARObject
        return cast("SaveConfigurationEntry", obj)


class SaveConfigurationEntryBuilder:
    """Builder for SaveConfigurationEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SaveConfigurationEntry = SaveConfigurationEntry()

    def build(self) -> SaveConfigurationEntry:
        """Build and return SaveConfigurationEntry object.

        Returns:
            SaveConfigurationEntry instance
        """
        # TODO: Add validation
        return self._obj
