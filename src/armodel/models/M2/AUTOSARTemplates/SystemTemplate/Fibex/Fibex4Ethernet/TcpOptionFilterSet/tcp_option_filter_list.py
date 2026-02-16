"""TcpOptionFilterList AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class TcpOptionFilterList(Identifiable):
    """AUTOSAR TcpOptionFilterList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("allowed_tcp_options", None, False, True, None),  # allowedTcpOptions
    ]

    def __init__(self) -> None:
        """Initialize TcpOptionFilterList."""
        super().__init__()
        self.allowed_tcp_options: list[PositiveInteger] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TcpOptionFilterList to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpOptionFilterList":
        """Create TcpOptionFilterList from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TcpOptionFilterList instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TcpOptionFilterList since parent returns ARObject
        return cast("TcpOptionFilterList", obj)


class TcpOptionFilterListBuilder:
    """Builder for TcpOptionFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpOptionFilterList = TcpOptionFilterList()

    def build(self) -> TcpOptionFilterList:
        """Build and return TcpOptionFilterList object.

        Returns:
            TcpOptionFilterList instance
        """
        # TODO: Add validation
        return self._obj
