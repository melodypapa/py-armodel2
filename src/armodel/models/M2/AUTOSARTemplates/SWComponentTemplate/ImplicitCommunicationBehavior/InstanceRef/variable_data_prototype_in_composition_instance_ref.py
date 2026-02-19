"""VariableDataPrototypeInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 959)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class VariableDataPrototypeInCompositionInstanceRef(ARObject):
    """AUTOSAR VariableDataPrototypeInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    context_port_ref: Optional[ARRef]
    context_sws: list[Any]
    target_variable_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize VariableDataPrototypeInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_port_ref: Optional[ARRef] = None
        self.context_sws: list[Any] = []
        self.target_variable_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableDataPrototypeInCompositionInstanceRef":
        """Deserialize XML element to VariableDataPrototypeInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableDataPrototypeInCompositionInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse context_port_ref
        child = ARObject._find_child_element(element, "CONTEXT-PORT")
        if child is not None:
            context_port_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.context_port_ref = context_port_ref_value

        # Parse context_sws (list)
        obj.context_sws = []
        for child in ARObject._find_all_child_elements(element, "CONTEXT-SWS"):
            context_sws_value = child.text
            obj.context_sws.append(context_sws_value)

        # Parse target_variable_ref
        child = ARObject._find_child_element(element, "TARGET-VARIABLE")
        if child is not None:
            target_variable_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.target_variable_ref = target_variable_ref_value

        return obj



class VariableDataPrototypeInCompositionInstanceRefBuilder:
    """Builder for VariableDataPrototypeInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableDataPrototypeInCompositionInstanceRef = VariableDataPrototypeInCompositionInstanceRef()

    def build(self) -> VariableDataPrototypeInCompositionInstanceRef:
        """Build and return VariableDataPrototypeInCompositionInstanceRef object.

        Returns:
            VariableDataPrototypeInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
