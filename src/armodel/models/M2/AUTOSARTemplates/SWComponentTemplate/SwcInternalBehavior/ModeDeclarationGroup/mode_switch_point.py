"""ModeSwitchPoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchPoint(AbstractAccessPoint):
    """AUTOSAR ModeSwitchPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mode_group_swc_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # modeGroupSwcInstanceRef
    }

    def __init__(self) -> None:
        """Initialize ModeSwitchPoint."""
        super().__init__()
        self.mode_group_swc_instance_ref: Optional[ModeDeclarationGroup] = None


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
