"""RModeInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 943)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class RModeInAtomicSwcInstanceRef(ARObject):
    """AUTOSAR RModeInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize RModeInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_mode_group_prototype: Optional[ModeDeclarationGroup] = None
        self.context_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_mode_declaration: Optional[ModeDeclaration] = None


class RModeInAtomicSwcInstanceRefBuilder:
    """Builder for RModeInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RModeInAtomicSwcInstanceRef = RModeInAtomicSwcInstanceRef()

    def build(self) -> RModeInAtomicSwcInstanceRef:
        """Build and return RModeInAtomicSwcInstanceRef object.

        Returns:
            RModeInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
