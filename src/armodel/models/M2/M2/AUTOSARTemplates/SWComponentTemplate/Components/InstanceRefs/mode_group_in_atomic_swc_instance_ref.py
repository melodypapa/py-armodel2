"""ModeGroupInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 961)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class ModeGroupInAtomicSwcInstanceRef(ARObject):
    """AUTOSAR ModeGroupInAtomicSwcInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize ModeGroupInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_port: Optional[PortPrototype] = None
        self.target: Optional[ModeDeclarationGroup] = None


class ModeGroupInAtomicSwcInstanceRefBuilder:
    """Builder for ModeGroupInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeGroupInAtomicSwcInstanceRef = ModeGroupInAtomicSwcInstanceRef()

    def build(self) -> ModeGroupInAtomicSwcInstanceRef:
        """Build and return ModeGroupInAtomicSwcInstanceRef object.

        Returns:
            ModeGroupInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
