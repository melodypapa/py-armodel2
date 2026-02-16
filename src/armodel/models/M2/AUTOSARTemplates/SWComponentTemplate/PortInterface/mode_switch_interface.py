"""ModeSwitchInterface AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchInterface(PortInterface):
    """AUTOSAR ModeSwitchInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mode_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # modeGroup
    }

    def __init__(self) -> None:
        """Initialize ModeSwitchInterface."""
        super().__init__()
        self.mode_group: Optional[ModeDeclarationGroup] = None


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
