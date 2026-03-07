"""InitialSdDelayConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 514)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InitialSdDelayConfig(ARObject):
    """AUTOSAR InitialSdDelayConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INITIAL-SD-DELAY-CONFIG"


    initial_delay_max: Optional[TimeValue]
    initial_delay_min: Optional[TimeValue]
    initial: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "INITIAL-DELAY-MAX": lambda obj, elem: setattr(obj, "initial_delay_max", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "INITIAL-DELAY-MIN": lambda obj, elem: setattr(obj, "initial_delay_min", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "INITIAL": lambda obj, elem: setattr(obj, "initial", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize InitialSdDelayConfig."""
        super().__init__()
        self.initial_delay_max: Optional[TimeValue] = None
        self.initial_delay_min: Optional[TimeValue] = None
        self.initial: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize InitialSdDelayConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InitialSdDelayConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_delay_max
        if self.initial_delay_max is not None:
            serialized = SerializationHelper.serialize_item(self.initial_delay_max, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DELAY-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial_delay_min
        if self.initial_delay_min is not None:
            serialized = SerializationHelper.serialize_item(self.initial_delay_min, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DELAY-MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial
        if self.initial is not None:
            serialized = SerializationHelper.serialize_item(self.initial, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InitialSdDelayConfig":
        """Deserialize XML element to InitialSdDelayConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InitialSdDelayConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InitialSdDelayConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INITIAL-DELAY-MAX":
                setattr(obj, "initial_delay_max", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "INITIAL-DELAY-MIN":
                setattr(obj, "initial_delay_min", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "INITIAL":
                setattr(obj, "initial", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class InitialSdDelayConfigBuilder(BuilderBase):
    """Builder for InitialSdDelayConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InitialSdDelayConfig = InitialSdDelayConfig()


    def with_initial_delay_max(self, value: Optional[TimeValue]) -> "InitialSdDelayConfigBuilder":
        """Set initial_delay_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'initial_delay_max' is required and cannot be None")
        self._obj.initial_delay_max = value
        return self

    def with_initial_delay_min(self, value: Optional[TimeValue]) -> "InitialSdDelayConfigBuilder":
        """Set initial_delay_min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'initial_delay_min' is required and cannot be None")
        self._obj.initial_delay_min = value
        return self

    def with_initial(self, value: Optional[PositiveInteger]) -> "InitialSdDelayConfigBuilder":
        """Set initial attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'initial' is required and cannot be None")
        self._obj.initial = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "initial",
        "initialDelayMax",
        "initialDelayMin",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> InitialSdDelayConfig:
        """Build and return the InitialSdDelayConfig instance with validation."""
        self._validate_instance()
        return self._obj