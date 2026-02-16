"""PortInterfaceMappingSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)


class PortInterfaceMappingSet(ARElement):
    """AUTOSAR PortInterfaceMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("port_interfaces", None, False, True, PortInterfaceMapping),  # portInterfaces
    ]

    def __init__(self) -> None:
        """Initialize PortInterfaceMappingSet."""
        super().__init__()
        self.port_interfaces: list[PortInterfaceMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortInterfaceMappingSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInterfaceMappingSet":
        """Create PortInterfaceMappingSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortInterfaceMappingSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortInterfaceMappingSet since parent returns ARObject
        return cast("PortInterfaceMappingSet", obj)


class PortInterfaceMappingSetBuilder:
    """Builder for PortInterfaceMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInterfaceMappingSet = PortInterfaceMappingSet()

    def build(self) -> PortInterfaceMappingSet:
        """Build and return PortInterfaceMappingSet object.

        Returns:
            PortInterfaceMappingSet instance
        """
        # TODO: Add validation
        return self._obj
