"""LinEventTriggeredFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 430)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import LinFrameBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinEventTriggeredFrame(LinFrame):
    """AUTOSAR LinEventTriggeredFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-EVENT-TRIGGERED-FRAME"


    collision_schedule_ref: Optional[ARRef]
    lin_unconditional_frame_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COLLISION-SCHEDULE-REF": lambda obj, elem: setattr(obj, "collision_schedule_ref", ARRef.deserialize(elem)),
        "LIN-UNCONDITIONAL-FRAME-REFS": lambda obj, elem: [obj.lin_unconditional_frame_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize LinEventTriggeredFrame."""
        super().__init__()
        self.collision_schedule_ref: Optional[ARRef] = None
        self.lin_unconditional_frame_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize LinEventTriggeredFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinEventTriggeredFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize collision_schedule_ref
        if self.collision_schedule_ref is not None:
            serialized = SerializationHelper.serialize_item(self.collision_schedule_ref, "LinScheduleTable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLISION-SCHEDULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_unconditional_frame_refs (list to container "LIN-UNCONDITIONAL-FRAME-REFS")
        if self.lin_unconditional_frame_refs:
            wrapper = ET.Element("LIN-UNCONDITIONAL-FRAME-REFS")
            for item in self.lin_unconditional_frame_refs:
                serialized = SerializationHelper.serialize_item(item, "LinUnconditionalFrame")
                if serialized is not None:
                    child_elem = ET.Element("LIN-UNCONDITIONAL-FRAME-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinEventTriggeredFrame":
        """Deserialize XML element to LinEventTriggeredFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinEventTriggeredFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinEventTriggeredFrame, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COLLISION-SCHEDULE-REF":
                setattr(obj, "collision_schedule_ref", ARRef.deserialize(child))
            elif tag == "LIN-UNCONDITIONAL-FRAME-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.lin_unconditional_frame_refs.append(ARRef.deserialize(item_elem))

        return obj



class LinEventTriggeredFrameBuilder(LinFrameBuilder):
    """Builder for LinEventTriggeredFrame with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinEventTriggeredFrame = LinEventTriggeredFrame()


    def with_collision_schedule(self, value: Optional[LinScheduleTable]) -> "LinEventTriggeredFrameBuilder":
        """Set collision_schedule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.collision_schedule = value
        return self

    def with_lin_unconditional_frames(self, items: list[LinUnconditionalFrame]) -> "LinEventTriggeredFrameBuilder":
        """Set lin_unconditional_frames list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.lin_unconditional_frames = list(items) if items else []
        return self


    def add_lin_unconditional_frame(self, item: LinUnconditionalFrame) -> "LinEventTriggeredFrameBuilder":
        """Add a single item to lin_unconditional_frames list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.lin_unconditional_frames.append(item)
        return self

    def clear_lin_unconditional_frames(self) -> "LinEventTriggeredFrameBuilder":
        """Clear all items from lin_unconditional_frames list.

        Returns:
            self for method chaining
        """
        self._obj.lin_unconditional_frames = []
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


    def build(self) -> LinEventTriggeredFrame:
        """Build and return the LinEventTriggeredFrame instance with validation."""
        self._validate_instance()
        pass
        return self._obj