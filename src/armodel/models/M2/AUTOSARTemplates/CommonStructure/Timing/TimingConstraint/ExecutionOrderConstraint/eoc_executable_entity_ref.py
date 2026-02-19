"""EOCExecutableEntityRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 120)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)


class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCExecutableEntityRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module: Optional[BswImplementation]
    component: Optional[Any]
    executable_entity: Optional[ExecutableEntity]
    successors: list[Any]
    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRef."""
        super().__init__()
        self.bsw_module: Optional[BswImplementation] = None
        self.component: Optional[Any] = None
        self.executable_entity: Optional[ExecutableEntity] = None
        self.successors: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRef":
        """Deserialize XML element to EOCExecutableEntityRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCExecutableEntityRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_module
        child = ARObject._find_child_element(element, "BSW-MODULE")
        if child is not None:
            bsw_module_value = ARObject._deserialize_by_tag(child, "BswImplementation")
            obj.bsw_module = bsw_module_value

        # Parse component
        child = ARObject._find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = child.text
            obj.component = component_value

        # Parse executable_entity
        child = ARObject._find_child_element(element, "EXECUTABLE-ENTITY")
        if child is not None:
            executable_entity_value = ARObject._deserialize_by_tag(child, "ExecutableEntity")
            obj.executable_entity = executable_entity_value

        # Parse successors (list)
        obj.successors = []
        for child in ARObject._find_all_child_elements(element, "SUCCESSORS"):
            successors_value = child.text
            obj.successors.append(successors_value)

        return obj



class EOCExecutableEntityRefBuilder:
    """Builder for EOCExecutableEntityRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRef = EOCExecutableEntityRef()

    def build(self) -> EOCExecutableEntityRef:
        """Build and return EOCExecutableEntityRef object.

        Returns:
            EOCExecutableEntityRef instance
        """
        # TODO: Add validation
        return self._obj
