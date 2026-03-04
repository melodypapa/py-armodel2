"""PerInstanceMemorySize AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 623)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PerInstanceMemorySize(ARObject):
    """AUTOSAR PerInstanceMemorySize."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PER-INSTANCE-MEMORY-SIZE"


    alignment: Optional[PositiveInteger]
    per_instance_memory_memory_ref: Optional[ARRef]
    size: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ALIGNMENT": lambda obj, elem: setattr(obj, "alignment", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PER-INSTANCE-MEMORY-MEMORY-REF": lambda obj, elem: setattr(obj, "per_instance_memory_memory_ref", ARRef.deserialize(elem)),
        "SIZE": lambda obj, elem: setattr(obj, "size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize PerInstanceMemorySize."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.per_instance_memory_memory_ref: Optional[ARRef] = None
        self.size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize PerInstanceMemorySize to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PerInstanceMemorySize, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alignment
        if self.alignment is not None:
            serialized = SerializationHelper.serialize_item(self.alignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize per_instance_memory_memory_ref
        if self.per_instance_memory_memory_ref is not None:
            serialized = SerializationHelper.serialize_item(self.per_instance_memory_memory_ref, "PerInstanceMemory")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PER-INSTANCE-MEMORY-MEMORY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size
        if self.size is not None:
            serialized = SerializationHelper.serialize_item(self.size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PerInstanceMemorySize":
        """Deserialize XML element to PerInstanceMemorySize object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PerInstanceMemorySize object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PerInstanceMemorySize, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALIGNMENT":
                setattr(obj, "alignment", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PER-INSTANCE-MEMORY-MEMORY-REF":
                setattr(obj, "per_instance_memory_memory_ref", ARRef.deserialize(child))
            elif tag == "SIZE":
                setattr(obj, "size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class PerInstanceMemorySizeBuilder(BuilderBase):
    """Builder for PerInstanceMemorySize with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PerInstanceMemorySize = PerInstanceMemorySize()


    def with_alignment(self, value: Optional[PositiveInteger]) -> "PerInstanceMemorySizeBuilder":
        """Set alignment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alignment = value
        return self

    def with_per_instance_memory_memory(self, value: Optional[PerInstanceMemory]) -> "PerInstanceMemorySizeBuilder":
        """Set per_instance_memory_memory attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.per_instance_memory_memory = value
        return self

    def with_size(self, value: Optional[PositiveInteger]) -> "PerInstanceMemorySizeBuilder":
        """Set size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "alignment",
        "perInstanceMemoryMemory",
        "size",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PerInstanceMemorySize:
        """Build and return the PerInstanceMemorySize instance with validation."""
        self._validate_instance()
        return self._obj