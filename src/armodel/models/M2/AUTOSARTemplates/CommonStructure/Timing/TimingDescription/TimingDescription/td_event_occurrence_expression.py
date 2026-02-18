"""TDEventOccurrenceExpression AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TDEventOccurrenceExpression(ARObject):
    """AUTOSAR TDEventOccurrenceExpression."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: list[AutosarOperationArgumentInstance]
    formula: Optional[Any]
    modes: list[TimingModeInstance]
    variables: list[Any]
    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpression."""
        super().__init__()
        self.arguments: list[AutosarOperationArgumentInstance] = []
        self.formula: Optional[Any] = None
        self.modes: list[TimingModeInstance] = []
        self.variables: list[Any] = []


class TDEventOccurrenceExpressionBuilder:
    """Builder for TDEventOccurrenceExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOccurrenceExpression = TDEventOccurrenceExpression()

    def build(self) -> TDEventOccurrenceExpression:
        """Build and return TDEventOccurrenceExpression object.

        Returns:
            TDEventOccurrenceExpression instance
        """
        # TODO: Add validation
        return self._obj
