"""VariableInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 941)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from abc import ABC, abstractmethod


class VariableInAtomicSwcInstanceRef(ARObject, ABC):
    """AUTOSAR VariableInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    abstract_target_ref: Optional[ARRef]
    base: Optional[AtomicSwComponentType]
    context_port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize VariableInAtomicSwcInstanceRef."""
        super().__init__()
        self.abstract_target_ref: Optional[ARRef] = None
        self.base: Optional[AtomicSwComponentType] = None
        self.context_port_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableInAtomicSwcInstanceRef":
        """Deserialize XML element to VariableInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableInAtomicSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse abstract_target_ref
        child = ARObject._find_child_element(element, "ABSTRACT-TARGET")
        if child is not None:
            abstract_target_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.abstract_target_ref = abstract_target_ref_value

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

        return obj



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
