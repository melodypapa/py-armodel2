"""CommConnectorPort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class CommConnectorPort(Identifiable):
    """AUTOSAR CommConnectorPort."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication", None, False, False, any (Communication)),  # communication
    ]

    def __init__(self) -> None:
        """Initialize CommConnectorPort."""
        super().__init__()
        self.communication: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CommConnectorPort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommConnectorPort":
        """Create CommConnectorPort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CommConnectorPort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CommConnectorPort since parent returns ARObject
        return cast("CommConnectorPort", obj)


class CommConnectorPortBuilder:
    """Builder for CommConnectorPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommConnectorPort = CommConnectorPort()

    def build(self) -> CommConnectorPort:
        """Build and return CommConnectorPort object.

        Returns:
            CommConnectorPort instance
        """
        # TODO: Add validation
        return self._obj
