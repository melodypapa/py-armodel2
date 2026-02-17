"""VariableInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 941)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class VariableInAtomicSwcInstanceRef(ARObject):
    """AUTOSAR VariableInAtomicSwcInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize VariableInAtomicSwcInstanceRef."""
        super().__init__()
        self.abstract_target: Optional[VariableDataPrototype] = None
        self.base: Optional[AtomicSwComponentType] = None
        self.context_port: Optional[PortPrototype] = None


class VariableInAtomicSwcInstanceRefBuilder:
    """Builder for VariableInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableInAtomicSwcInstanceRef = VariableInAtomicSwcInstanceRef()

    def build(self) -> VariableInAtomicSwcInstanceRef:
        """Build and return VariableInAtomicSwcInstanceRef object.

        Returns:
            VariableInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
