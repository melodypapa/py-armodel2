"""TcpOptionFilterSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)


class TcpOptionFilterSet(ARElement):
    """AUTOSAR TcpOptionFilterSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_option_filter_lists", None, False, True, TcpOptionFilterList),  # tcpOptionFilterLists
    ]

    def __init__(self) -> None:
        """Initialize TcpOptionFilterSet."""
        super().__init__()
        self.tcp_option_filter_lists: list[TcpOptionFilterList] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TcpOptionFilterSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpOptionFilterSet":
        """Create TcpOptionFilterSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TcpOptionFilterSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TcpOptionFilterSet since parent returns ARObject
        return cast("TcpOptionFilterSet", obj)


class TcpOptionFilterSetBuilder:
    """Builder for TcpOptionFilterSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpOptionFilterSet = TcpOptionFilterSet()

    def build(self) -> TcpOptionFilterSet:
        """Build and return TcpOptionFilterSet object.

        Returns:
            TcpOptionFilterSet instance
        """
        # TODO: Add validation
        return self._obj
