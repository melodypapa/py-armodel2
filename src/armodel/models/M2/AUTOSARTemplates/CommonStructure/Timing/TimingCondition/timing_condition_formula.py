"""TimingConditionFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("timing_argument_argument_instance", None, False, False, AutosarOperationArgumentInstance),  # timingArgumentArgumentInstance
        ("timing_condition", None, False, False, TimingCondition),  # timingCondition
        ("timing_event", None, False, False, TimingDescriptionEvent),  # timingEvent
        ("timing_mode", None, False, False, TimingModeInstance),  # timingMode
        ("timing_variable_instance", None, False, False, any (AutosarVariable)),  # timingVariableInstance
    ]

    def __init__(self) -> None:
        """Initialize TimingConditionFormula."""
        super().__init__()
        self.timing_argument_argument_instance: Optional[AutosarOperationArgumentInstance] = None
        self.timing_condition: Optional[TimingCondition] = None
        self.timing_event: Optional[TimingDescriptionEvent] = None
        self.timing_mode: Optional[TimingModeInstance] = None
        self.timing_variable_instance: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingConditionFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingConditionFormula":
        """Create TimingConditionFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingConditionFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingConditionFormula since parent returns ARObject
        return cast("TimingConditionFormula", obj)


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
