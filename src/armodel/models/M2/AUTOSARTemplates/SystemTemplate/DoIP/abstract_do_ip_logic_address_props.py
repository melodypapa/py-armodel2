"""AbstractDoIpLogicAddressProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class AbstractDoIpLogicAddressProps(Identifiable):
    """AUTOSAR AbstractDoIpLogicAddressProps."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize AbstractDoIpLogicAddressProps."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractDoIpLogicAddressProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractDoIpLogicAddressProps":
        """Create AbstractDoIpLogicAddressProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractDoIpLogicAddressProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractDoIpLogicAddressProps since parent returns ARObject
        return cast("AbstractDoIpLogicAddressProps", obj)


class AbstractDoIpLogicAddressPropsBuilder:
    """Builder for AbstractDoIpLogicAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractDoIpLogicAddressProps = AbstractDoIpLogicAddressProps()

    def build(self) -> AbstractDoIpLogicAddressProps:
        """Build and return AbstractDoIpLogicAddressProps object.

        Returns:
            AbstractDoIpLogicAddressProps instance
        """
        # TODO: Add validation
        return self._obj
