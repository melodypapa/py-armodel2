"""OperationInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 946)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from abc import ABC, abstractmethod


class OperationInAtomicSwcInstanceRef(ARObject, ABC):
    """AUTOSAR OperationInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    base: Optional[AtomicSwComponentType]
    context_port_ref: Optional[ARRef]
    target_operation: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize OperationInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_port_ref: Optional[ARRef] = None
        self.target_operation: Optional[ClientServerOperation] = None


class OperationInAtomicSwcInstanceRefBuilder:
    """Builder for OperationInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInAtomicSwcInstanceRef = OperationInAtomicSwcInstanceRef()

    def build(self) -> OperationInAtomicSwcInstanceRef:
        """Build and return OperationInAtomicSwcInstanceRef object.

        Returns:
            OperationInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
