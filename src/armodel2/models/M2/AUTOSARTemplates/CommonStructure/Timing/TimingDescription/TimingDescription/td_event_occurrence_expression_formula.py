"""TDEventOccurrenceExpressionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventOccurrenceExpressionFormula(ARObject):
    """AUTOSAR TDEventOccurrenceExpressionFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-OCCURRENCE-EXPRESSION-FORMULA"


    argument_ref: Optional[ARRef]
    event_ref: Optional[ARRef]
    mode_ref: Optional[ARRef]
    variable_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "ARGUMENT-REF": lambda obj, elem: setattr(obj, "argument_ref", ARRef.deserialize(elem)),
        "EVENT-REF": ("_POLYMORPHIC", "event_ref", ["TDEventBsw", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventCom", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLET", "TDEventSLLETPort", "TDEventSwc", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfb", "TDEventVfbReference"]),
        "MODE-REF": lambda obj, elem: setattr(obj, "mode_ref", ARRef.deserialize(elem)),
        "VARIABLE-REF": lambda obj, elem: setattr(obj, "variable_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpressionFormula."""
        super().__init__()
        self.argument_ref: Optional[ARRef] = None
        self.event_ref: Optional[ARRef] = None
        self.mode_ref: Optional[ARRef] = None
        self.variable_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventOccurrenceExpressionFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventOccurrenceExpressionFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize argument_ref
        if self.argument_ref is not None:
            serialized = SerializationHelper.serialize_item(self.argument_ref, "AutosarOperationArgumentInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARGUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_ref
        if self.event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_ref
        if self.mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_ref, "TimingModeInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_ref
        if self.variable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.variable_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOccurrenceExpressionFormula":
        """Deserialize XML element to TDEventOccurrenceExpressionFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventOccurrenceExpressionFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventOccurrenceExpressionFormula, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARGUMENT-REF":
                setattr(obj, "argument_ref", ARRef.deserialize(child))
            elif tag == "EVENT-REF":
                setattr(obj, "event_ref", ARRef.deserialize(child))
            elif tag == "MODE-REF":
                setattr(obj, "mode_ref", ARRef.deserialize(child))
            elif tag == "VARIABLE-REF":
                setattr(obj, "variable_ref", ARRef.deserialize(child))

        return obj



class TDEventOccurrenceExpressionFormulaBuilder(BuilderBase):
    """Builder for TDEventOccurrenceExpressionFormula with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventOccurrenceExpressionFormula = TDEventOccurrenceExpressionFormula()


    def with_argument(self, value: Optional[AutosarOperationArgumentInstance]) -> "TDEventOccurrenceExpressionFormulaBuilder":
        """Set argument attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.argument = value
        return self

    def with_event(self, value: Optional[TimingDescriptionEvent]) -> "TDEventOccurrenceExpressionFormulaBuilder":
        """Set event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event = value
        return self

    def with_mode(self, value: Optional[TimingModeInstance]) -> "TDEventOccurrenceExpressionFormulaBuilder":
        """Set mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode = value
        return self

    def with_variable(self, value: Optional[any (AutosarVariable)]) -> "TDEventOccurrenceExpressionFormulaBuilder":
        """Set variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variable = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "argument",
        "event",
        "mode",
        "variable",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDEventOccurrenceExpressionFormula:
        """Build and return the TDEventOccurrenceExpressionFormula instance with validation."""
        self._validate_instance()
        return self._obj