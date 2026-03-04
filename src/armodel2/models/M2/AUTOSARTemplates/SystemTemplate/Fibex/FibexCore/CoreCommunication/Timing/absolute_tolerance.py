"""AbsoluteTolerance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbsoluteTolerance(ARObject):
    """AUTOSAR AbsoluteTolerance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ABSOLUTE-TOLERANCE"


    absolute: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "ABSOLUTE": lambda obj, elem: setattr(obj, "absolute", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize AbsoluteTolerance."""
        super().__init__()
        self.absolute: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize AbsoluteTolerance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbsoluteTolerance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize absolute
        if self.absolute is not None:
            serialized = SerializationHelper.serialize_item(self.absolute, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ABSOLUTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbsoluteTolerance":
        """Deserialize XML element to AbsoluteTolerance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbsoluteTolerance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbsoluteTolerance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ABSOLUTE":
                setattr(obj, "absolute", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class AbsoluteToleranceBuilder(BuilderBase):
    """Builder for AbsoluteTolerance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbsoluteTolerance = AbsoluteTolerance()


    def with_absolute(self, value: Optional[TimeValue]) -> "AbsoluteToleranceBuilder":
        """Set absolute attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.absolute = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "absolute",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AbsoluteTolerance:
        """Build and return the AbsoluteTolerance instance with validation."""
        self._validate_instance()
        return self._obj