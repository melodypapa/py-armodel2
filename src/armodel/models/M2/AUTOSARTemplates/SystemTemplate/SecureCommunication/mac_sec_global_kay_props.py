"""MacSecGlobalKayProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class MacSecGlobalKayProps(ARElement):
    """AUTOSAR MacSecGlobalKayProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bypass_ether", None, True, False, None),  # bypassEther
        ("bypass_vlan", None, True, False, None),  # bypassVlan
    ]

    def __init__(self) -> None:
        """Initialize MacSecGlobalKayProps."""
        super().__init__()
        self.bypass_ether: PositiveInteger = None
        self.bypass_vlan: PositiveInteger = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacSecGlobalKayProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecGlobalKayProps":
        """Create MacSecGlobalKayProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacSecGlobalKayProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacSecGlobalKayProps since parent returns ARObject
        return cast("MacSecGlobalKayProps", obj)


class MacSecGlobalKayPropsBuilder:
    """Builder for MacSecGlobalKayProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecGlobalKayProps = MacSecGlobalKayProps()

    def build(self) -> MacSecGlobalKayProps:
        """Build and return MacSecGlobalKayProps object.

        Returns:
            MacSecGlobalKayProps instance
        """
        # TODO: Add validation
        return self._obj
