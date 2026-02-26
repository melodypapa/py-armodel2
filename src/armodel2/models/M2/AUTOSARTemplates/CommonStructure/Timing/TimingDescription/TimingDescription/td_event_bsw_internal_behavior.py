"""TDEventBswInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import TimingDescriptionEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventBswInternalBehavior(TimingDescriptionEvent):
    """AUTOSAR TDEventBswInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_entity_entity_ref: Optional[ARRef]
    td_event_bsw_behavior_type: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventBswInternalBehavior."""
        super().__init__()
        self.bsw_module_entity_entity_ref: Optional[ARRef] = None
        self.td_event_bsw_behavior_type: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventBswInternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventBswInternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_entity_entity_ref
        if self.bsw_module_entity_entity_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_module_entity_entity_ref, "BswModuleEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-ENTITY-ENTITY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_bsw_behavior_type
        if self.td_event_bsw_behavior_type is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_bsw_behavior_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-BSW-BEHAVIOR-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswInternalBehavior":
        """Deserialize XML element to TDEventBswInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBswInternalBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventBswInternalBehavior, cls).deserialize(element)

        # Parse bsw_module_entity_entity_ref
        child = SerializationHelper.find_child_element(element, "BSW-MODULE-ENTITY-ENTITY-REF")
        if child is not None:
            bsw_module_entity_entity_ref_value = ARRef.deserialize(child)
            obj.bsw_module_entity_entity_ref = bsw_module_entity_entity_ref_value

        # Parse td_event_bsw_behavior_type
        child = SerializationHelper.find_child_element(element, "TD-EVENT-BSW-BEHAVIOR-TYPE")
        if child is not None:
            td_event_bsw_behavior_type_value = child.text
            obj.td_event_bsw_behavior_type = td_event_bsw_behavior_type_value

        return obj



class TDEventBswInternalBehaviorBuilder(TimingDescriptionEventBuilder):
    """Builder for TDEventBswInternalBehavior with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventBswInternalBehavior = TDEventBswInternalBehavior()


    def with_bsw_module_entity_entity(self, value: Optional[BswModuleEntity]) -> "TDEventBswInternalBehaviorBuilder":
        """Set bsw_module_entity_entity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_module_entity_entity = value
        return self

    def with_td_event_bsw_behavior_type(self, value: Optional[any (TDEventBswInternal)]) -> "TDEventBswInternalBehaviorBuilder":
        """Set td_event_bsw_behavior_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.td_event_bsw_behavior_type = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> TDEventBswInternalBehavior:
        """Build and return the TDEventBswInternalBehavior instance with validation."""
        self._validate_instance()
        pass
        return self._obj