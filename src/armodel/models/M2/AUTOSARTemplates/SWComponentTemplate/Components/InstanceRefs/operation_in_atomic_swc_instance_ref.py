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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "OperationInAtomicSwcInstanceRef":
        """Deserialize XML element to OperationInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OperationInAtomicSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "AtomicSwComponentType")
            obj.base = base_value

        # Parse context_port_ref
        child = ARObject._find_child_element(element, "CONTEXT-PORT")
        if child is not None:
            context_port_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.context_port_ref = context_port_ref_value

        # Parse target_operation
        child = ARObject._find_child_element(element, "TARGET-OPERATION")
        if child is not None:
            target_operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.target_operation = target_operation_value

        return obj



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
