"""GeneralPurposePdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)


class GeneralPurposePdu(Pdu):
    """AUTOSAR GeneralPurposePdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize GeneralPurposePdu."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GeneralPurposePdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GeneralPurposePdu":
        """Create GeneralPurposePdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GeneralPurposePdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GeneralPurposePdu since parent returns ARObject
        return cast("GeneralPurposePdu", obj)


class GeneralPurposePduBuilder:
    """Builder for GeneralPurposePdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralPurposePdu = GeneralPurposePdu()

    def build(self) -> GeneralPurposePdu:
        """Build and return GeneralPurposePdu object.

        Returns:
            GeneralPurposePdu instance
        """
        # TODO: Add validation
        return self._obj
