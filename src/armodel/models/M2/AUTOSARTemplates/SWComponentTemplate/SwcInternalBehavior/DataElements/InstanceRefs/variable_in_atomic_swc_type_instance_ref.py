"""VariableInAtomicSWCTypeInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 953)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class VariableInAtomicSWCTypeInstanceRef(ARObject):
    """AUTOSAR VariableInAtomicSWCTypeInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[AtomicSwComponentType]
    context_datas: list[Any]
    port_prototype_ref: Optional[ARRef]
    root_variable_data_prototype_ref: Optional[ARRef]
    target_data_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize VariableInAtomicSWCTypeInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_datas: list[Any] = []
        self.port_prototype_ref: Optional[ARRef] = None
        self.root_variable_data_prototype_ref: Optional[ARRef] = None
        self.target_data_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableInAtomicSWCTypeInstanceRef":
        """Deserialize XML element to VariableInAtomicSWCTypeInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableInAtomicSWCTypeInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "AtomicSwComponentType")
            obj.base = base_value

        # Parse context_datas (list from container "CONTEXT-DATAS")
        obj.context_datas = []
        container = ARObject._find_child_element(element, "CONTEXT-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_datas.append(child_value)

        # Parse port_prototype_ref
        child = ARObject._find_child_element(element, "PORT-PROTOTYPE")
        if child is not None:
            port_prototype_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.port_prototype_ref = port_prototype_ref_value

        # Parse root_variable_data_prototype_ref
        child = ARObject._find_child_element(element, "ROOT-VARIABLE-DATA-PROTOTYPE")
        if child is not None:
            root_variable_data_prototype_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.root_variable_data_prototype_ref = root_variable_data_prototype_ref_value

        # Parse target_data_ref
        child = ARObject._find_child_element(element, "TARGET-DATA")
        if child is not None:
            target_data_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.target_data_ref = target_data_ref_value

        return obj



class VariableInAtomicSWCTypeInstanceRefBuilder:
    """Builder for VariableInAtomicSWCTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableInAtomicSWCTypeInstanceRef = VariableInAtomicSWCTypeInstanceRef()

    def build(self) -> VariableInAtomicSWCTypeInstanceRef:
        """Build and return VariableInAtomicSWCTypeInstanceRef object.

        Returns:
            VariableInAtomicSWCTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
