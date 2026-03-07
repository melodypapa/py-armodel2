"""HeapUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 152)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2026)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_HeapUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class HeapUsage(Identifiable, ABC):
    """AUTOSAR HeapUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    hardware: Optional[HardwareConfiguration]
    hw_element_ref: Optional[ARRef]
    software_context: Optional[SoftwareContext]
    _DESERIALIZE_DISPATCH = {
        "HARDWARE": lambda obj, elem: setattr(obj, "hardware", SerializationHelper.deserialize_by_tag(elem, "HardwareConfiguration")),
        "HW-ELEMENT-REF": lambda obj, elem: setattr(obj, "hw_element_ref", ARRef.deserialize(elem)),
        "SOFTWARE-CONTEXT": lambda obj, elem: setattr(obj, "software_context", SerializationHelper.deserialize_by_tag(elem, "SoftwareContext")),
    }


    def __init__(self) -> None:
        """Initialize HeapUsage."""
        super().__init__()
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element_ref: Optional[ARRef] = None
        self.software_context: Optional[SoftwareContext] = None

    def serialize(self) -> ET.Element:
        """Serialize HeapUsage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HeapUsage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hardware
        if self.hardware is not None:
            serialized = SerializationHelper.serialize_item(self.hardware, "HardwareConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HARDWARE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw_element_ref
        if self.hw_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_element_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize software_context
        if self.software_context is not None:
            serialized = SerializationHelper.serialize_item(self.software_context, "SoftwareContext")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HeapUsage":
        """Deserialize XML element to HeapUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HeapUsage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HeapUsage, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HARDWARE":
                setattr(obj, "hardware", SerializationHelper.deserialize_by_tag(child, "HardwareConfiguration"))
            elif tag == "HW-ELEMENT-REF":
                setattr(obj, "hw_element_ref", ARRef.deserialize(child))
            elif tag == "SOFTWARE-CONTEXT":
                setattr(obj, "software_context", SerializationHelper.deserialize_by_tag(child, "SoftwareContext"))

        return obj



class HeapUsageBuilder(IdentifiableBuilder):
    """Builder for HeapUsage with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HeapUsage = HeapUsage()


    def with_hardware(self, value: Optional[HardwareConfiguration]) -> "HeapUsageBuilder":
        """Set hardware attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'hardware' is required and cannot be None")
        self._obj.hardware = value
        return self

    def with_hw_element(self, value: Optional[HwElement]) -> "HeapUsageBuilder":
        """Set hw_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'hw_element' is required and cannot be None")
        self._obj.hw_element = value
        return self

    def with_software_context(self, value: Optional[SoftwareContext]) -> "HeapUsageBuilder":
        """Set software_context attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'software_context' is required and cannot be None")
        self._obj.software_context = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "hardware",
        "hwElement",
        "softwareContext",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> HeapUsage:
        """Build and return the HeapUsage instance (abstract)."""
        raise NotImplementedError