"""DdsResourceLimits AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsResourceLimits(ARObject):
    """AUTOSAR DdsResourceLimits."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-RESOURCE-LIMITS"


    max_instances: Optional[PositiveInteger]
    max_samples: Optional[PositiveInteger]
    max_samples_per_instance: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "MAX-INSTANCES": lambda obj, elem: setattr(obj, "max_instances", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MAX-SAMPLES": lambda obj, elem: setattr(obj, "max_samples", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MAX-SAMPLES-PER-INSTANCE": lambda obj, elem: setattr(obj, "max_samples_per_instance", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DdsResourceLimits."""
        super().__init__()
        self.max_instances: Optional[PositiveInteger] = None
        self.max_samples: Optional[PositiveInteger] = None
        self.max_samples_per_instance: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsResourceLimits to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsResourceLimits, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_instances
        if self.max_instances is not None:
            serialized = SerializationHelper.serialize_item(self.max_instances, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-INSTANCES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_samples
        if self.max_samples is not None:
            serialized = SerializationHelper.serialize_item(self.max_samples, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SAMPLES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_samples_per_instance
        if self.max_samples_per_instance is not None:
            serialized = SerializationHelper.serialize_item(self.max_samples_per_instance, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SAMPLES-PER-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsResourceLimits":
        """Deserialize XML element to DdsResourceLimits object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsResourceLimits object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsResourceLimits, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAX-INSTANCES":
                setattr(obj, "max_instances", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MAX-SAMPLES":
                setattr(obj, "max_samples", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MAX-SAMPLES-PER-INSTANCE":
                setattr(obj, "max_samples_per_instance", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DdsResourceLimitsBuilder(BuilderBase):
    """Builder for DdsResourceLimits with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsResourceLimits = DdsResourceLimits()


    def with_max_instances(self, value: Optional[PositiveInteger]) -> "DdsResourceLimitsBuilder":
        """Set max_instances attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_instances' is required and cannot be None")
        self._obj.max_instances = value
        return self

    def with_max_samples(self, value: Optional[PositiveInteger]) -> "DdsResourceLimitsBuilder":
        """Set max_samples attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_samples' is required and cannot be None")
        self._obj.max_samples = value
        return self

    def with_max_samples_per_instance(self, value: Optional[PositiveInteger]) -> "DdsResourceLimitsBuilder":
        """Set max_samples_per_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_samples_per_instance' is required and cannot be None")
        self._obj.max_samples_per_instance = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "maxInstances",
        "maxSamples",
        "maxSamplesPerInstance",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsResourceLimits:
        """Build and return the DdsResourceLimits instance with validation."""
        self._validate_instance()
        return self._obj