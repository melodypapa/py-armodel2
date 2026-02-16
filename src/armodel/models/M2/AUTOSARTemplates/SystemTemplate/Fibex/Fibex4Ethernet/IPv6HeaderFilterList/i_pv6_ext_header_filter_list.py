"""IPv6ExtHeaderFilterList AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class IPv6ExtHeaderFilterList(Identifiable):
    """AUTOSAR IPv6ExtHeaderFilterList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("allowed_i_pv6_exts", None, False, True, None),  # allowedIPv6Exts
    ]

    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterList."""
        super().__init__()
        self.allowed_i_pv6_exts: list[PositiveInteger] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IPv6ExtHeaderFilterList to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPv6ExtHeaderFilterList":
        """Create IPv6ExtHeaderFilterList from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IPv6ExtHeaderFilterList instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IPv6ExtHeaderFilterList since parent returns ARObject
        return cast("IPv6ExtHeaderFilterList", obj)


class IPv6ExtHeaderFilterListBuilder:
    """Builder for IPv6ExtHeaderFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPv6ExtHeaderFilterList = IPv6ExtHeaderFilterList()

    def build(self) -> IPv6ExtHeaderFilterList:
        """Build and return IPv6ExtHeaderFilterList object.

        Returns:
            IPv6ExtHeaderFilterList instance
        """
        # TODO: Add validation
        return self._obj
