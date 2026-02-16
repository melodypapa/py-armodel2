"""ModeSwitchReceiverComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchReceiverComSpec(RPortComSpec):
    """AUTOSAR ModeSwitchReceiverComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("enhanced_mode", None, True, False, None),  # enhancedMode
        ("mode_group", None, False, False, ModeDeclarationGroup),  # modeGroup
        ("supports", None, True, False, None),  # supports
    ]

    def __init__(self) -> None:
        """Initialize ModeSwitchReceiverComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group: Optional[ModeDeclarationGroup] = None
        self.supports: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeSwitchReceiverComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchReceiverComSpec":
        """Create ModeSwitchReceiverComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeSwitchReceiverComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeSwitchReceiverComSpec since parent returns ARObject
        return cast("ModeSwitchReceiverComSpec", obj)


class ModeSwitchReceiverComSpecBuilder:
    """Builder for ModeSwitchReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchReceiverComSpec = ModeSwitchReceiverComSpec()

    def build(self) -> ModeSwitchReceiverComSpec:
        """Build and return ModeSwitchReceiverComSpec object.

        Returns:
            ModeSwitchReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
