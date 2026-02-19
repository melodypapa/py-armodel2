"""ArVariableInImplementationDataInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 322)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class ArVariableInImplementationDataInstanceRef(ARObject):
    """AUTOSAR ArVariableInImplementationDataInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_datas: list[Any]
    port_prototype_ref: Optional[ARRef]
    root_variable_ref: Optional[ARRef]
    target_data: Optional[Any]
    def __init__(self) -> None:
        """Initialize ArVariableInImplementationDataInstanceRef."""
        super().__init__()
        self.context_datas: list[Any] = []
        self.port_prototype_ref: Optional[ARRef] = None
        self.root_variable_ref: Optional[ARRef] = None
        self.target_data: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArVariableInImplementationDataInstanceRef":
        """Deserialize XML element to ArVariableInImplementationDataInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArVariableInImplementationDataInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_datas (list)
        obj.context_datas = []
        for child in ARObject._find_all_child_elements(element, "CONTEXT-DATAS"):
            context_datas_value = child.text
            obj.context_datas.append(context_datas_value)

        # Parse port_prototype_ref
        child = ARObject._find_child_element(element, "PORT-PROTOTYPE")
        if child is not None:
            port_prototype_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.port_prototype_ref = port_prototype_ref_value

        # Parse root_variable_ref
        child = ARObject._find_child_element(element, "ROOT-VARIABLE")
        if child is not None:
            root_variable_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.root_variable_ref = root_variable_ref_value

        # Parse target_data
        child = ARObject._find_child_element(element, "TARGET-DATA")
        if child is not None:
            target_data_value = child.text
            obj.target_data = target_data_value

        return obj



class ArVariableInImplementationDataInstanceRefBuilder:
    """Builder for ArVariableInImplementationDataInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArVariableInImplementationDataInstanceRef = ArVariableInImplementationDataInstanceRef()

    def build(self) -> ArVariableInImplementationDataInstanceRef:
        """Build and return ArVariableInImplementationDataInstanceRef object.

        Returns:
            ArVariableInImplementationDataInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
