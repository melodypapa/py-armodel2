"""ClientIdRange AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
)


class ClientIdRange(ARObject):
    """AUTOSAR ClientIdRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lower_limit", None, True, False, None),  # lowerLimit
        ("upper_limit", None, True, False, None),  # upperLimit
    ]

    def __init__(self) -> None:
        """Initialize ClientIdRange."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.upper_limit: Optional[Limit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientIdRange to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdRange":
        """Create ClientIdRange from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientIdRange instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientIdRange since parent returns ARObject
        return cast("ClientIdRange", obj)


class ClientIdRangeBuilder:
    """Builder for ClientIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdRange = ClientIdRange()

    def build(self) -> ClientIdRange:
        """Build and return ClientIdRange object.

        Returns:
            ClientIdRange instance
        """
        # TODO: Add validation
        return self._obj
