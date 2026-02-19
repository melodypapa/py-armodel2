"""ExecutionOrderConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class ExecutionOrderConstraint(TimingConstraint):
    """AUTOSAR ExecutionOrderConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    execution_order: Optional[Any]
    ignore_order: Optional[Boolean]
    is_event: Optional[Boolean]
    ordered_elements: list[Any]
    permit_multiple: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ExecutionOrderConstraint."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.execution_order: Optional[Any] = None
        self.ignore_order: Optional[Boolean] = None
        self.is_event: Optional[Boolean] = None
        self.ordered_elements: list[Any] = []
        self.permit_multiple: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionOrderConstraint":
        """Deserialize XML element to ExecutionOrderConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutionOrderConstraint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse execution_order
        child = ARObject._find_child_element(element, "EXECUTION-ORDER")
        if child is not None:
            execution_order_value = child.text
            obj.execution_order = execution_order_value

        # Parse ignore_order
        child = ARObject._find_child_element(element, "IGNORE-ORDER")
        if child is not None:
            ignore_order_value = child.text
            obj.ignore_order = ignore_order_value

        # Parse is_event
        child = ARObject._find_child_element(element, "IS-EVENT")
        if child is not None:
            is_event_value = child.text
            obj.is_event = is_event_value

        # Parse ordered_elements (list)
        obj.ordered_elements = []
        for child in ARObject._find_all_child_elements(element, "ORDERED-ELEMENTS"):
            ordered_elements_value = child.text
            obj.ordered_elements.append(ordered_elements_value)

        # Parse permit_multiple
        child = ARObject._find_child_element(element, "PERMIT-MULTIPLE")
        if child is not None:
            permit_multiple_value = child.text
            obj.permit_multiple = permit_multiple_value

        return obj



class ExecutionOrderConstraintBuilder:
    """Builder for ExecutionOrderConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutionOrderConstraint = ExecutionOrderConstraint()

    def build(self) -> ExecutionOrderConstraint:
        """Build and return ExecutionOrderConstraint object.

        Returns:
            ExecutionOrderConstraint instance
        """
        # TODO: Add validation
        return self._obj
