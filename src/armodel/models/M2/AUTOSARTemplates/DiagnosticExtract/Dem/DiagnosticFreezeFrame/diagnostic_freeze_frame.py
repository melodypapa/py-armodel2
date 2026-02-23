"""DiagnosticFreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 192)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticFreezeFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame import (
    DiagnosticRecordTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)


class DiagnosticFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFreezeFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_trigger: Optional[String]
    record_number: Optional[PositiveInteger]
    trigger: Optional[DiagnosticRecordTriggerEnum]
    update: Optional[Boolean]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse custom_trigger
        child = SerializationHelper.find_child_element(element, "CUSTOM-TRIGGER")
        if child is not None:
            custom_trigger_value = child.text
            obj.custom_trigger = custom_trigger_value

        # Parse record_number
        child = SerializationHelper.find_child_element(element, "RECORD-NUMBER")
        if child is not None:
            record_number_value = child.text
            obj.record_number = record_number_value

        # Parse trigger
        child = SerializationHelper.find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_value = DiagnosticRecordTriggerEnum.deserialize(child)
            obj.trigger = trigger_value

        # Parse update
        child = SerializationHelper.find_child_element(element, "UPDATE")
        if child is not None:
            update_value = child.text
            obj.update = update_value

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




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> DiagnosticFreezeFrame:
        """Build and return the DiagnosticFreezeFrame instance with validation."""
        self._validate_instance()
        pass
        return self._obj