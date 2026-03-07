"""TriggerMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_TriggerDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TriggerMapping(ARObject):
    """AUTOSAR TriggerMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRIGGER-MAPPING"


    first_trigger_ref: Optional[ARRef]
    second_trigger_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "FIRST-TRIGGER-REF": lambda obj, elem: setattr(obj, "first_trigger_ref", ARRef.deserialize(elem)),
        "SECOND-TRIGGER-REF": lambda obj, elem: setattr(obj, "second_trigger_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TriggerMapping."""
        super().__init__()
        self.first_trigger_ref: Optional[ARRef] = None
        self.second_trigger_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TriggerMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TriggerMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_trigger_ref
        if self.first_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_trigger_ref
        if self.second_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerMapping":
        """Deserialize XML element to TriggerMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TriggerMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FIRST-TRIGGER-REF":
                setattr(obj, "first_trigger_ref", ARRef.deserialize(child))
            elif tag == "SECOND-TRIGGER-REF":
                setattr(obj, "second_trigger_ref", ARRef.deserialize(child))

        return obj



class TriggerMappingBuilder(BuilderBase):
    """Builder for TriggerMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TriggerMapping = TriggerMapping()


    def with_first_trigger(self, value: Optional[Trigger]) -> "TriggerMappingBuilder":
        """Set first_trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'first_trigger' is required and cannot be None")
        self._obj.first_trigger = value
        return self

    def with_second_trigger(self, value: Optional[Trigger]) -> "TriggerMappingBuilder":
        """Set second_trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'second_trigger' is required and cannot be None")
        self._obj.second_trigger = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "firstTrigger",
        "secondTrigger",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TriggerMapping:
        """Build and return the TriggerMapping instance with validation."""
        self._validate_instance()
        return self._obj