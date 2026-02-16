"""ModeInterfaceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR ModeInterfaceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode_mapping", None, False, False, ModeDeclarationGroup),  # modeMapping
    ]

    def __init__(self) -> None:
        """Initialize ModeInterfaceMapping."""
        super().__init__()
        self.mode_mapping: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeInterfaceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInterfaceMapping":
        """Create ModeInterfaceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeInterfaceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeInterfaceMapping since parent returns ARObject
        return cast("ModeInterfaceMapping", obj)


class ModeInterfaceMappingBuilder:
    """Builder for ModeInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInterfaceMapping = ModeInterfaceMapping()

    def build(self) -> ModeInterfaceMapping:
        """Build and return ModeInterfaceMapping object.

        Returns:
            ModeInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
