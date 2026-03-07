"""TDEventSwcInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 61)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import (
    TDEventSwc,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import TDEventSwcBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventSwcInternalBehavior(TDEventSwc):
    """AUTOSAR TDEventSwcInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-SWC-INTERNAL-BEHAVIOR"


    runnable_ref: Optional[ARRef]
    td_event_swc_behavior_type: Optional[Any]
    variable_access_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "RUNNABLE-REF": lambda obj, elem: setattr(obj, "runnable_ref", ARRef.deserialize(elem)),
        "TD-EVENT-SWC-BEHAVIOR-TYPE": lambda obj, elem: setattr(obj, "td_event_swc_behavior_type", SerializationHelper.deserialize_by_tag(elem, "any (TDEventSwcInternal)")),
        "VARIABLE-ACCESS-REF": lambda obj, elem: setattr(obj, "variable_access_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TDEventSwcInternalBehavior."""
        super().__init__()
        self.runnable_ref: Optional[ARRef] = None
        self.td_event_swc_behavior_type: Optional[Any] = None
        self.variable_access_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventSwcInternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventSwcInternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize runnable_ref
        if self.runnable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.runnable_ref, "RunnableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RUNNABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_swc_behavior_type
        if self.td_event_swc_behavior_type is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_swc_behavior_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-SWC-BEHAVIOR-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_access_ref
        if self.variable_access_ref is not None:
            serialized = SerializationHelper.serialize_item(self.variable_access_ref, "VariableAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-ACCESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSwcInternalBehavior":
        """Deserialize XML element to TDEventSwcInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventSwcInternalBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventSwcInternalBehavior, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RUNNABLE-REF":
                setattr(obj, "runnable_ref", ARRef.deserialize(child))
            elif tag == "TD-EVENT-SWC-BEHAVIOR-TYPE":
                setattr(obj, "td_event_swc_behavior_type", SerializationHelper.deserialize_by_tag(child, "any (TDEventSwcInternal)"))
            elif tag == "VARIABLE-ACCESS-REF":
                setattr(obj, "variable_access_ref", ARRef.deserialize(child))

        return obj



class TDEventSwcInternalBehaviorBuilder(TDEventSwcBuilder):
    """Builder for TDEventSwcInternalBehavior with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventSwcInternalBehavior = TDEventSwcInternalBehavior()


    def with_runnable(self, value: Optional[RunnableEntity]) -> "TDEventSwcInternalBehaviorBuilder":
        """Set runnable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'runnable' is required and cannot be None")
        self._obj.runnable = value
        return self

    def with_td_event_swc_behavior_type(self, value: Optional[Any]) -> "TDEventSwcInternalBehaviorBuilder":
        """Set td_event_swc_behavior_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'td_event_swc_behavior_type' is required and cannot be None")
        self._obj.td_event_swc_behavior_type = value
        return self

    def with_variable_access(self, value: Optional[VariableAccess]) -> "TDEventSwcInternalBehaviorBuilder":
        """Set variable_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'variable_access' is required and cannot be None")
        self._obj.variable_access = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "runnable",
        "tdEventSwcBehaviorType",
        "variableAccess",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDEventSwcInternalBehavior:
        """Build and return the TDEventSwcInternalBehavior instance with validation."""
        self._validate_instance()
        return self._obj