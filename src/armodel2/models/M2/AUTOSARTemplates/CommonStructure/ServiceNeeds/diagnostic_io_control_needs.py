"""DiagnosticIoControlNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 248)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 119)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 781)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import DiagnosticCapabilityElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_value_needs import (
    DiagnosticValueNeeds,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticIoControlNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-IO-CONTROL-NEEDS"


    current_value_ref: Optional[ARRef]
    freeze_current: Optional[Boolean]
    reset_to_default: Optional[Boolean]
    short_term: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "CURRENT-VALUE-REF": lambda obj, elem: setattr(obj, "current_value_ref", ARRef.deserialize(elem)),
        "FREEZE-CURRENT": lambda obj, elem: setattr(obj, "freeze_current", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RESET-TO-DEFAULT": lambda obj, elem: setattr(obj, "reset_to_default", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SHORT-TERM": lambda obj, elem: setattr(obj, "short_term", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticIoControlNeeds."""
        super().__init__()
        self.current_value_ref: Optional[ARRef] = None
        self.freeze_current: Optional[Boolean] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIoControlNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIoControlNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize current_value_ref
        if self.current_value_ref is not None:
            serialized = SerializationHelper.serialize_item(self.current_value_ref, "DiagnosticValueNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CURRENT-VALUE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize freeze_current
        if self.freeze_current is not None:
            serialized = SerializationHelper.serialize_item(self.freeze_current, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FREEZE-CURRENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reset_to_default
        if self.reset_to_default is not None:
            serialized = SerializationHelper.serialize_item(self.reset_to_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESET-TO-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_term
        if self.short_term is not None:
            serialized = SerializationHelper.serialize_item(self.short_term, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-TERM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIoControlNeeds":
        """Deserialize XML element to DiagnosticIoControlNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIoControlNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIoControlNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CURRENT-VALUE-REF":
                setattr(obj, "current_value_ref", ARRef.deserialize(child))
            elif tag == "FREEZE-CURRENT":
                setattr(obj, "freeze_current", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RESET-TO-DEFAULT":
                setattr(obj, "reset_to_default", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SHORT-TERM":
                setattr(obj, "short_term", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class DiagnosticIoControlNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for DiagnosticIoControlNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticIoControlNeeds = DiagnosticIoControlNeeds()


    def with_current_value(self, value: Optional[DiagnosticValueNeeds]) -> "DiagnosticIoControlNeedsBuilder":
        """Set current_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.current_value = value
        return self

    def with_freeze_current(self, value: Optional[Boolean]) -> "DiagnosticIoControlNeedsBuilder":
        """Set freeze_current attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.freeze_current = value
        return self

    def with_reset_to_default(self, value: Optional[Boolean]) -> "DiagnosticIoControlNeedsBuilder":
        """Set reset_to_default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reset_to_default = value
        return self

    def with_short_term(self, value: Optional[Boolean]) -> "DiagnosticIoControlNeedsBuilder":
        """Set short_term attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_term = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "currentValue",
        "freezeCurrent",
        "resetToDefault",
        "shortTerm",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticIoControlNeeds:
        """Build and return the DiagnosticIoControlNeeds instance with validation."""
        self._validate_instance()
        return self._obj