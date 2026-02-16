"""J1939NmEcu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)


class J1939NmEcu(BusspecificNmEcu):
    """AUTOSAR J1939NmEcu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize J1939NmEcu."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939NmEcu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NmEcu":
        """Create J1939NmEcu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939NmEcu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939NmEcu since parent returns ARObject
        return cast("J1939NmEcu", obj)


class J1939NmEcuBuilder:
    """Builder for J1939NmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmEcu = J1939NmEcu()

    def build(self) -> J1939NmEcu:
        """Build and return J1939NmEcu object.

        Returns:
            J1939NmEcu instance
        """
        # TODO: Add validation
        return self._obj
