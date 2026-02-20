"""TimingConditionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    timing_argument_argument_instance_ref: Optional[ARRef]
    timing_condition_ref: Optional[ARRef]
    timing_event_ref: Optional[ARRef]
    timing_mode_ref: Optional[ARRef]
    timing_variable_instance_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize TimingConditionFormula."""
        super().__init__()
        self.timing_argument_argument_instance_ref: Optional[ARRef] = None
        self.timing_condition_ref: Optional[ARRef] = None
        self.timing_event_ref: Optional[ARRef] = None
        self.timing_mode_ref: Optional[ARRef] = None
        self.timing_variable_instance_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingConditionFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize timing_argument_argument_instance_ref
        if self.timing_argument_argument_instance_ref is not None:
            serialized = ARObject._serialize_item(self.timing_argument_argument_instance_ref, "AutosarOperationArgumentInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-ARGUMENT-ARGUMENT-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_condition_ref
        if self.timing_condition_ref is not None:
            serialized = ARObject._serialize_item(self.timing_condition_ref, "TimingCondition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-CONDITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_event_ref
        if self.timing_event_ref is not None:
            serialized = ARObject._serialize_item(self.timing_event_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_mode_ref
        if self.timing_mode_ref is not None:
            serialized = ARObject._serialize_item(self.timing_mode_ref, "TimingModeInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_variable_instance_ref
        if self.timing_variable_instance_ref is not None:
            serialized = ARObject._serialize_item(self.timing_variable_instance_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-VARIABLE-INSTANCE-REF")
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

        # Parse timing_argument_argument_instance_ref
        child = ARObject._find_child_element(element, "TIMING-ARGUMENT-ARGUMENT-INSTANCE-REF")
        if child is not None:
            timing_argument_argument_instance_ref_value = ARRef.deserialize(child)
            obj.timing_argument_argument_instance_ref = timing_argument_argument_instance_ref_value

        # Parse timing_condition_ref
        child = ARObject._find_child_element(element, "TIMING-CONDITION-REF")
        if child is not None:
            timing_condition_ref_value = ARRef.deserialize(child)
            obj.timing_condition_ref = timing_condition_ref_value

        # Parse timing_event_ref
        child = ARObject._find_child_element(element, "TIMING-EVENT-REF")
        if child is not None:
            timing_event_ref_value = ARRef.deserialize(child)
            obj.timing_event_ref = timing_event_ref_value

        # Parse timing_mode_ref
        child = ARObject._find_child_element(element, "TIMING-MODE-REF")
        if child is not None:
            timing_mode_ref_value = ARRef.deserialize(child)
            obj.timing_mode_ref = timing_mode_ref_value

        # Parse timing_variable_instance_ref
        child = ARObject._find_child_element(element, "TIMING-VARIABLE-INSTANCE-REF")
        if child is not None:
            timing_variable_instance_ref_value = ARRef.deserialize(child)
            obj.timing_variable_instance_ref = timing_variable_instance_ref_value

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
