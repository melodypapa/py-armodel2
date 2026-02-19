"""TDEventOccurrenceExpressionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TDEventOccurrenceExpressionFormula(ARObject):
    """AUTOSAR TDEventOccurrenceExpressionFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    argument: Optional[AutosarOperationArgumentInstance]
    event: Optional[TimingDescriptionEvent]
    mode: Optional[TimingModeInstance]
    variable: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpressionFormula."""
        super().__init__()
        self.argument: Optional[AutosarOperationArgumentInstance] = None
        self.event: Optional[TimingDescriptionEvent] = None
        self.mode: Optional[TimingModeInstance] = None
        self.variable: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOccurrenceExpressionFormula":
        """Deserialize XML element to TDEventOccurrenceExpressionFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventOccurrenceExpressionFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse argument
        child = ARObject._find_child_element(element, "ARGUMENT")
        if child is not None:
            argument_value = ARObject._deserialize_by_tag(child, "AutosarOperationArgumentInstance")
            obj.argument = argument_value

        # Parse event
        child = ARObject._find_child_element(element, "EVENT")
        if child is not None:
            event_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.event = event_value

        # Parse mode
        child = ARObject._find_child_element(element, "MODE")
        if child is not None:
            mode_value = ARObject._deserialize_by_tag(child, "TimingModeInstance")
            obj.mode = mode_value

        # Parse variable
        child = ARObject._find_child_element(element, "VARIABLE")
        if child is not None:
            variable_value = child.text
            obj.variable = variable_value

        return obj



class TDEventOccurrenceExpressionFormulaBuilder:
    """Builder for TDEventOccurrenceExpressionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOccurrenceExpressionFormula = TDEventOccurrenceExpressionFormula()

    def build(self) -> TDEventOccurrenceExpressionFormula:
        """Build and return TDEventOccurrenceExpressionFormula object.

        Returns:
            TDEventOccurrenceExpressionFormula instance
        """
        # TODO: Add validation
        return self._obj
