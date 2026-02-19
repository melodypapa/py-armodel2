"""TimingExtensionResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TimingExtensionResource(Identifiable):
    """AUTOSAR TimingExtensionResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timing_arguments: list[AutosarOperationArgumentInstance]
    timing_modes: list[TimingModeInstance]
    timing_variables: list[Any]
    def __init__(self) -> None:
        """Initialize TimingExtensionResource."""
        super().__init__()
        self.timing_arguments: list[AutosarOperationArgumentInstance] = []
        self.timing_modes: list[TimingModeInstance] = []
        self.timing_variables: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingExtensionResource":
        """Deserialize XML element to TimingExtensionResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingExtensionResource object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse timing_arguments (list)
        obj.timing_arguments = []
        for child in ARObject._find_all_child_elements(element, "TIMING-ARGUMENTS"):
            timing_arguments_value = ARObject._deserialize_by_tag(child, "AutosarOperationArgumentInstance")
            obj.timing_arguments.append(timing_arguments_value)

        # Parse timing_modes (list)
        obj.timing_modes = []
        for child in ARObject._find_all_child_elements(element, "TIMING-MODES"):
            timing_modes_value = ARObject._deserialize_by_tag(child, "TimingModeInstance")
            obj.timing_modes.append(timing_modes_value)

        # Parse timing_variables (list)
        obj.timing_variables = []
        for child in ARObject._find_all_child_elements(element, "TIMING-VARIABLES"):
            timing_variables_value = child.text
            obj.timing_variables.append(timing_variables_value)

        return obj



class TimingExtensionResourceBuilder:
    """Builder for TimingExtensionResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingExtensionResource = TimingExtensionResource()

    def build(self) -> TimingExtensionResource:
        """Build and return TimingExtensionResource object.

        Returns:
            TimingExtensionResource instance
        """
        # TODO: Add validation
        return self._obj
