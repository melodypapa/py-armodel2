"""TriggerInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 944)

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
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from abc import ABC, abstractmethod


class TriggerInAtomicSwcInstanceRef(ARObject, ABC):
    """AUTOSAR TriggerInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    base: Optional[AtomicSwComponentType]
    context_port: Optional[PortPrototype]
    target: Optional[Trigger]
    def __init__(self) -> None:
        """Initialize TriggerInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_port: Optional[PortPrototype] = None
        self.target: Optional[Trigger] = None


class TriggerInAtomicSwcInstanceRefBuilder:
    """Builder for TriggerInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerInAtomicSwcInstanceRef = TriggerInAtomicSwcInstanceRef()

    def build(self) -> TriggerInAtomicSwcInstanceRef:
        """Build and return TriggerInAtomicSwcInstanceRef object.

        Returns:
            TriggerInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
