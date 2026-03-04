"""DiagnosticFreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 192)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticFreezeFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame import (
    DiagnosticRecordTriggerEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFreezeFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-FREEZE-FRAME"


    custom_trigger: Optional[String]
    record_number: Optional[PositiveInteger]
    trigger: Optional[DiagnosticRecordTriggerEnum]
    update: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "CUSTOM-TRIGGER": lambda obj, elem: setattr(obj, "custom_trigger", SerializationHelper.deserialize_by_tag(elem, "String")),
        "RECORD-NUMBER": lambda obj, elem: setattr(obj, "record_number", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TRIGGER": lambda obj, elem: setattr(obj, "trigger", DiagnosticRecordTriggerEnum.deserialize(elem)),
        "UPDATE": lambda obj, elem: setattr(obj, "update", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticFreezeFrame."""
        super().__init__()
        self.custom_trigger: Optional[String] = None
        self.record_number: Optional[PositiveInteger] = None
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None
        self.update: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFreezeFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFreezeFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_trigger
        if self.custom_trigger is not None:
            serialized = SerializationHelper.serialize_item(self.custom_trigger, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-TRIGGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize record_number
        if self.record_number is not None:
            serialized = SerializationHelper.serialize_item(self.record_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RECORD-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger
        if self.trigger is not None:
            serialized = SerializationHelper.serialize_item(self.trigger, "DiagnosticRecordTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update
        if self.update is not None:
            serialized = SerializationHelper.serialize_item(self.update, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFreezeFrame":
        """Deserialize XML element to DiagnosticFreezeFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFreezeFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFreezeFrame, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CUSTOM-TRIGGER":
                setattr(obj, "custom_trigger", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "RECORD-NUMBER":
                setattr(obj, "record_number", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TRIGGER":
                setattr(obj, "trigger", DiagnosticRecordTriggerEnum.deserialize(child))
            elif tag == "UPDATE":
                setattr(obj, "update", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class DiagnosticFreezeFrameBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticFreezeFrame with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticFreezeFrame = DiagnosticFreezeFrame()


    def with_custom_trigger(self, value: Optional[String]) -> "DiagnosticFreezeFrameBuilder":
        """Set custom_trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.custom_trigger = value
        return self

    def with_record_number(self, value: Optional[PositiveInteger]) -> "DiagnosticFreezeFrameBuilder":
        """Set record_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.record_number = value
        return self

    def with_trigger(self, value: Optional[DiagnosticRecordTriggerEnum]) -> "DiagnosticFreezeFrameBuilder":
        """Set trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.trigger = value
        return self

    def with_update(self, value: Optional[Boolean]) -> "DiagnosticFreezeFrameBuilder":
        """Set update attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.update = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "customTrigger",
        "recordNumber",
        "trigger",
        "update",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticFreezeFrame:
        """Build and return the DiagnosticFreezeFrame instance with validation."""
        self._validate_instance()
        return self._obj