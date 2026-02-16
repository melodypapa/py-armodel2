"""SwcBswSynchronizedModeGroupPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class SwcBswSynchronizedModeGroupPrototype(ARObject):
    """AUTOSAR SwcBswSynchronizedModeGroupPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_mode_group_prototype", None, False, False, ModeDeclarationGroup),  # bswModeGroupPrototype
        ("swc_mode_group_swc_instance_ref", None, False, False, ModeDeclarationGroup),  # swcModeGroupSwcInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize SwcBswSynchronizedModeGroupPrototype."""
        super().__init__()
        self.bsw_mode_group_prototype: Optional[ModeDeclarationGroup] = None
        self.swc_mode_group_swc_instance_ref: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcBswSynchronizedModeGroupPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswSynchronizedModeGroupPrototype":
        """Create SwcBswSynchronizedModeGroupPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcBswSynchronizedModeGroupPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcBswSynchronizedModeGroupPrototype since parent returns ARObject
        return cast("SwcBswSynchronizedModeGroupPrototype", obj)


class SwcBswSynchronizedModeGroupPrototypeBuilder:
    """Builder for SwcBswSynchronizedModeGroupPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswSynchronizedModeGroupPrototype = SwcBswSynchronizedModeGroupPrototype()

    def build(self) -> SwcBswSynchronizedModeGroupPrototype:
        """Build and return SwcBswSynchronizedModeGroupPrototype object.

        Returns:
            SwcBswSynchronizedModeGroupPrototype instance
        """
        # TODO: Add validation
        return self._obj
