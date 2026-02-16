"""ModeSwitchSenderComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchSenderComSpec(PPortComSpec):
    """AUTOSAR ModeSwitchSenderComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("enhanced_mode", None, True, False, None),  # enhancedMode
        ("mode_group", None, False, False, ModeDeclarationGroup),  # modeGroup
        ("mode_switched_ack", None, False, False, any (ModeSwitchedAck)),  # modeSwitchedAck
        ("queue_length", None, True, False, None),  # queueLength
    ]

    def __init__(self) -> None:
        """Initialize ModeSwitchSenderComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group: Optional[ModeDeclarationGroup] = None
        self.mode_switched_ack: Optional[Any] = None
        self.queue_length: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeSwitchSenderComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchSenderComSpec":
        """Create ModeSwitchSenderComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeSwitchSenderComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeSwitchSenderComSpec since parent returns ARObject
        return cast("ModeSwitchSenderComSpec", obj)


class ModeSwitchSenderComSpecBuilder:
    """Builder for ModeSwitchSenderComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchSenderComSpec = ModeSwitchSenderComSpec()

    def build(self) -> ModeSwitchSenderComSpec:
        """Build and return ModeSwitchSenderComSpec object.

        Returns:
            ModeSwitchSenderComSpec instance
        """
        # TODO: Add validation
        return self._obj
