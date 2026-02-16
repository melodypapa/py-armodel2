"""ModeSwitchInterface AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchInterface(PortInterface):
    """AUTOSAR ModeSwitchInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode_group", None, False, False, ModeDeclarationGroup),  # modeGroup
    ]

    def __init__(self) -> None:
        """Initialize ModeSwitchInterface."""
        super().__init__()
        self.mode_group: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeSwitchInterface to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchInterface":
        """Create ModeSwitchInterface from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeSwitchInterface instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeSwitchInterface since parent returns ARObject
        return cast("ModeSwitchInterface", obj)


class ModeSwitchInterfaceBuilder:
    """Builder for ModeSwitchInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchInterface = ModeSwitchInterface()

    def build(self) -> ModeSwitchInterface:
        """Build and return ModeSwitchInterface object.

        Returns:
            ModeSwitchInterface instance
        """
        # TODO: Add validation
        return self._obj
