"""RVariableInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 943)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.variable_in_atomic_swc_instance_ref import (
    VariableInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    """AUTOSAR RVariableInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_r_port_prototype: Optional[AbstractRequiredPortPrototype]
    target_data_element_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RVariableInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_data_element_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RVariableInAtomicSwcInstanceRef":
        """Deserialize XML element to RVariableInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RVariableInAtomicSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_r_port_prototype
        child = ARObject._find_child_element(element, "CONTEXT-R-PORT-PROTOTYPE")
        if child is not None:
            context_r_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractRequiredPortPrototype")
            obj.context_r_port_prototype = context_r_port_prototype_value

        # Parse target_data_element_ref
        child = ARObject._find_child_element(element, "TARGET-DATA-ELEMENT")
        if child is not None:
            target_data_element_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.target_data_element_ref = target_data_element_ref_value

        return obj



class RVariableInAtomicSwcInstanceRefBuilder:
    """Builder for RVariableInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RVariableInAtomicSwcInstanceRef = RVariableInAtomicSwcInstanceRef()

    def build(self) -> RVariableInAtomicSwcInstanceRef:
        """Build and return RVariableInAtomicSwcInstanceRef object.

        Returns:
            RVariableInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
