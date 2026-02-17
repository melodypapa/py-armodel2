"""ModeSwitchSenderComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "enhanced_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # enhancedMode
        "mode_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # modeGroup
        "mode_switched_ack": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # modeSwitchedAck
        "queue_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # queueLength
    }

    def __init__(self) -> None:
        """Initialize ModeSwitchSenderComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group: Optional[ModeDeclarationGroup] = None
        self.mode_switched_ack: Optional[Any] = None
        self.queue_length: Optional[PositiveInteger] = None


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
