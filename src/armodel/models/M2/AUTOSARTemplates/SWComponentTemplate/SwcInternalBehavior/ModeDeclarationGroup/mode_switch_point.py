"""ModeSwitchPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchPoint(AbstractAccessPoint):
    """AUTOSAR ModeSwitchPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode_group_swc_instance_ref", None, False, False, ModeDeclarationGroup),  # modeGroupSwcInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize ModeSwitchPoint."""
        super().__init__()
        self.mode_group_swc_instance_ref: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeSwitchPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchPoint":
        """Create ModeSwitchPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeSwitchPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeSwitchPoint since parent returns ARObject
        return cast("ModeSwitchPoint", obj)


class ModeSwitchPointBuilder:
    """Builder for ModeSwitchPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchPoint = ModeSwitchPoint()

    def build(self) -> ModeSwitchPoint:
        """Build and return ModeSwitchPoint object.

        Returns:
            ModeSwitchPoint instance
        """
        # TODO: Add validation
        return self._obj
