"""MacMulticastGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)


class MacMulticastGroup(Identifiable):
    """AUTOSAR MacMulticastGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mac_multicast", None, True, False, None),  # macMulticast
    ]

    def __init__(self) -> None:
        """Initialize MacMulticastGroup."""
        super().__init__()
        self.mac_multicast: Optional[MacAddressString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacMulticastGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacMulticastGroup":
        """Create MacMulticastGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacMulticastGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacMulticastGroup since parent returns ARObject
        return cast("MacMulticastGroup", obj)


class MacMulticastGroupBuilder:
    """Builder for MacMulticastGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacMulticastGroup = MacMulticastGroup()

    def build(self) -> MacMulticastGroup:
        """Build and return MacMulticastGroup object.

        Returns:
            MacMulticastGroup instance
        """
        # TODO: Add validation
        return self._obj
