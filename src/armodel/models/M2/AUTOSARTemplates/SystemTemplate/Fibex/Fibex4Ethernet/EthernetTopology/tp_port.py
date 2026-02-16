"""TpPort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TpPort(ARObject):
    """AUTOSAR TpPort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dynamically", None, True, False, None),  # dynamically
        ("port_number", None, True, False, None),  # portNumber
    ]

    def __init__(self) -> None:
        """Initialize TpPort."""
        super().__init__()
        self.dynamically: Optional[Boolean] = None
        self.port_number: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TpPort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpPort":
        """Create TpPort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TpPort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TpPort since parent returns ARObject
        return cast("TpPort", obj)


class TpPortBuilder:
    """Builder for TpPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpPort = TpPort()

    def build(self) -> TpPort:
        """Build and return TpPort object.

        Returns:
            TpPort instance
        """
        # TODO: Add validation
        return self._obj
