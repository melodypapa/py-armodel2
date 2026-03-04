"""MemorySectionLocation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 162)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.memory_section import (
    MemorySection,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MemorySectionLocation(ARObject):
    """AUTOSAR MemorySectionLocation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MEMORY-SECTION-LOCATION"


    provided_memory_ref: Optional[ARRef]
    software_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PROVIDED-MEMORY-REF": lambda obj, elem: setattr(obj, "provided_memory_ref", ARRef.deserialize(elem)),
        "SOFTWARE-REF": lambda obj, elem: setattr(obj, "software_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize MemorySectionLocation."""
        super().__init__()
        self.provided_memory_ref: Optional[ARRef] = None
        self.software_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize MemorySectionLocation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MemorySectionLocation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided_memory_ref
        if self.provided_memory_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provided_memory_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-MEMORY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize software_ref
        if self.software_ref is not None:
            serialized = SerializationHelper.serialize_item(self.software_ref, "MemorySection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MemorySectionLocation":
        """Deserialize XML element to MemorySectionLocation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MemorySectionLocation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MemorySectionLocation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROVIDED-MEMORY-REF":
                setattr(obj, "provided_memory_ref", ARRef.deserialize(child))
            elif tag == "SOFTWARE-REF":
                setattr(obj, "software_ref", ARRef.deserialize(child))

        return obj



class MemorySectionLocationBuilder(BuilderBase):
    """Builder for MemorySectionLocation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MemorySectionLocation = MemorySectionLocation()


    def with_provided_memory(self, value: Optional[HwElement]) -> "MemorySectionLocationBuilder":
        """Set provided_memory attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.provided_memory = value
        return self

    def with_software(self, value: Optional[MemorySection]) -> "MemorySectionLocationBuilder":
        """Set software attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.software = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "providedMemory",
        "software",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MemorySectionLocation:
        """Build and return the MemorySectionLocation instance with validation."""
        self._validate_instance()
        return self._obj