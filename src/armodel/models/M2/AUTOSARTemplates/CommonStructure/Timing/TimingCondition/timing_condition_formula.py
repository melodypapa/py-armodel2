"""TimingConditionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timing_argument_argument_instance: Optional[AutosarOperationArgumentInstance]
    timing_condition: Optional[TimingCondition]
    timing_event: Optional[TimingDescriptionEvent]
    timing_mode: Optional[TimingModeInstance]
    timing_variable_instance: Optional[Any]
    def __init__(self) -> None:
        """Initialize TimingConditionFormula."""
        super().__init__()
        self.timing_argument_argument_instance: Optional[AutosarOperationArgumentInstance] = None
        self.timing_condition: Optional[TimingCondition] = None
        self.timing_event: Optional[TimingDescriptionEvent] = None
        self.timing_mode: Optional[TimingModeInstance] = None
        self.timing_variable_instance: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize TimingConditionFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize timing_argument_argument_instance
        if self.timing_argument_argument_instance is not None:
            serialized = ARObject._serialize_item(self.timing_argument_argument_instance, "AutosarOperationArgumentInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-ARGUMENT-ARGUMENT-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_condition
        if self.timing_condition is not None:
            serialized = ARObject._serialize_item(self.timing_condition, "TimingCondition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-CONDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_event
        if self.timing_event is not None:
            serialized = ARObject._serialize_item(self.timing_event, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_mode
        if self.timing_mode is not None:
            serialized = ARObject._serialize_item(self.timing_mode, "TimingModeInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_variable_instance
        if self.timing_variable_instance is not None:
            serialized = ARObject._serialize_item(self.timing_variable_instance, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-VARIABLE-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingConditionFormula":
        """Deserialize XML element to TimingConditionFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingConditionFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse timing_argument_argument_instance
        child = ARObject._find_child_element(element, "TIMING-ARGUMENT-ARGUMENT-INSTANCE")
        if child is not None:
            timing_argument_argument_instance_value = ARObject._deserialize_by_tag(child, "AutosarOperationArgumentInstance")
            obj.timing_argument_argument_instance = timing_argument_argument_instance_value

        # Parse timing_condition
        child = ARObject._find_child_element(element, "TIMING-CONDITION")
        if child is not None:
            timing_condition_value = ARObject._deserialize_by_tag(child, "TimingCondition")
            obj.timing_condition = timing_condition_value

        # Parse timing_event
        child = ARObject._find_child_element(element, "TIMING-EVENT")
        if child is not None:
            timing_event_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.timing_event = timing_event_value

        # Parse timing_mode
        child = ARObject._find_child_element(element, "TIMING-MODE")
        if child is not None:
            timing_mode_value = ARObject._deserialize_by_tag(child, "TimingModeInstance")
            obj.timing_mode = timing_mode_value

        # Parse timing_variable_instance
        child = ARObject._find_child_element(element, "TIMING-VARIABLE-INSTANCE")
        if child is not None:
            timing_variable_instance_value = child.text
            obj.timing_variable_instance = timing_variable_instance_value

        return obj



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
