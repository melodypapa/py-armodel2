"""EcucDestinationUriDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class EcucDestinationUriDef(Identifiable):
    """AUTOSAR EcucDestinationUriDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_uri", None, False, False, any (EcucDestinationUri)),  # destinationUri
    ]

    def __init__(self) -> None:
        """Initialize EcucDestinationUriDef."""
        super().__init__()
        self.destination_uri: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucDestinationUriDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriDef":
        """Create EcucDestinationUriDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucDestinationUriDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucDestinationUriDef since parent returns ARObject
        return cast("EcucDestinationUriDef", obj)


class EcucDestinationUriDefBuilder:
    """Builder for EcucDestinationUriDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriDef = EcucDestinationUriDef()

    def build(self) -> EcucDestinationUriDef:
        """Build and return EcucDestinationUriDef object.

        Returns:
            EcucDestinationUriDef instance
        """
        # TODO: Add validation
        return self._obj
