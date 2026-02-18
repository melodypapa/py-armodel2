"""ModeInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR ModeInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_mapping: Optional[ModeDeclarationGroup]
    def __init__(self) -> None:
        """Initialize ModeInterfaceMapping."""
        super().__init__()
        self.mode_mapping: Optional[ModeDeclarationGroup] = None


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
