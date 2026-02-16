"""IPv6ExtHeaderFilterSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_list import (
    IPv6ExtHeaderFilterList,
)


class IPv6ExtHeaderFilterSet(ARElement):
    """AUTOSAR IPv6ExtHeaderFilterSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ext_header_filters", None, False, True, IPv6ExtHeaderFilterList),  # extHeaderFilters
    ]

    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterSet."""
        super().__init__()
        self.ext_header_filters: list[IPv6ExtHeaderFilterList] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IPv6ExtHeaderFilterSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPv6ExtHeaderFilterSet":
        """Create IPv6ExtHeaderFilterSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IPv6ExtHeaderFilterSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IPv6ExtHeaderFilterSet since parent returns ARObject
        return cast("IPv6ExtHeaderFilterSet", obj)


class IPv6ExtHeaderFilterSetBuilder:
    """Builder for IPv6ExtHeaderFilterSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPv6ExtHeaderFilterSet = IPv6ExtHeaderFilterSet()

    def build(self) -> IPv6ExtHeaderFilterSet:
        """Build and return IPv6ExtHeaderFilterSet object.

        Returns:
            IPv6ExtHeaderFilterSet instance
        """
        # TODO: Add validation
        return self._obj
