"""TimingConditionFormula AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TimingConditionFormula(ARObject):
    """AUTOSAR TimingConditionFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "timing_argument_argument_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarOperationArgumentInstance,
        ),  # timingArgumentArgumentInstance
        "timing_condition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingCondition,
        ),  # timingCondition
        "timing_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingDescriptionEvent,
        ),  # timingEvent
        "timing_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingModeInstance,
        ),  # timingMode
        "timing_variable_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (AutosarVariable),
        ),  # timingVariableInstance
    }

    def __init__(self) -> None:
        """Initialize TimingConditionFormula."""
        super().__init__()
        self.timing_argument_argument_instance: Optional[AutosarOperationArgumentInstance] = None
        self.timing_condition: Optional[TimingCondition] = None
        self.timing_event: Optional[TimingDescriptionEvent] = None
        self.timing_mode: Optional[TimingModeInstance] = None
        self.timing_variable_instance: Optional[Any] = None


class TimingConditionFormulaBuilder:
    """Builder for TimingConditionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingConditionFormula = TimingConditionFormula()

    def build(self) -> TimingConditionFormula:
        """Build and return TimingConditionFormula object.

        Returns:
            TimingConditionFormula instance
        """
        # TODO: Add validation
        return self._obj
