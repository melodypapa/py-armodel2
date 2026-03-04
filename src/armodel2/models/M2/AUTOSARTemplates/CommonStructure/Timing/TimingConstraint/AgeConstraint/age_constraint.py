"""AgeConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_AgeConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import TimingConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AgeConstraint(TimingConstraint):
    """AUTOSAR AgeConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "AGE-CONSTRAINT"


    maximum: Optional[MultidimensionalTime]
    minimum: Optional[MultidimensionalTime]
    scope_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MAXIMUM": lambda obj, elem: setattr(obj, "maximum", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "MINIMUM": lambda obj, elem: setattr(obj, "minimum", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "SCOPE-REF": ("_POLYMORPHIC", "scope_ref", ["TDEventBsw", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventCom", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLET", "TDEventSLLETPort", "TDEventSwc", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfb", "TDEventVfbReference"]),
    }


    def __init__(self) -> None:
        """Initialize AgeConstraint."""
        super().__init__()
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.scope_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize AgeConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AgeConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum
        if self.minimum is not None:
            serialized = SerializationHelper.serialize_item(self.minimum, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scope_ref
        if self.scope_ref is not None:
            serialized = SerializationHelper.serialize_item(self.scope_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCOPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AgeConstraint":
        """Deserialize XML element to AgeConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AgeConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AgeConstraint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAXIMUM":
                setattr(obj, "maximum", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "MINIMUM":
                setattr(obj, "minimum", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "SCOPE-REF":
                setattr(obj, "scope_ref", ARRef.deserialize(child))

        return obj



class AgeConstraintBuilder(TimingConstraintBuilder):
    """Builder for AgeConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AgeConstraint = AgeConstraint()


    def with_maximum(self, value: Optional[MultidimensionalTime]) -> "AgeConstraintBuilder":
        """Set maximum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum = value
        return self

    def with_minimum(self, value: Optional[MultidimensionalTime]) -> "AgeConstraintBuilder":
        """Set minimum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum = value
        return self

    def with_scope(self, value: Optional[TimingDescriptionEvent]) -> "AgeConstraintBuilder":
        """Set scope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.scope = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "maximum",
        "minimum",
        "scope",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AgeConstraint:
        """Build and return the AgeConstraint instance with validation."""
        self._validate_instance()
        return self._obj