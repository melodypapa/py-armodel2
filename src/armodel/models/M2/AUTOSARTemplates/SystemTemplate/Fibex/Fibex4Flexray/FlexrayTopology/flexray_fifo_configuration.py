"""FlexrayFifoConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_fifo_range import (
    FlexrayFifoRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_physical_channel import (
    FlexrayPhysicalChannel,
)


class FlexrayFifoConfiguration(ARObject):
    """AUTOSAR FlexrayFifoConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    admit_without: Optional[Boolean]
    base_cycle: Optional[Integer]
    channel_ref: Optional[ARRef]
    cycle_repetition: Optional[Integer]
    fifo_depth: Optional[Integer]
    fifo_ranges: list[FlexrayFifoRange]
    msg_id_mask: Optional[Integer]
    msg_id_match: Optional[Integer]
    def __init__(self) -> None:
        """Initialize FlexrayFifoConfiguration."""
        super().__init__()
        self.admit_without: Optional[Boolean] = None
        self.base_cycle: Optional[Integer] = None
        self.channel_ref: Optional[ARRef] = None
        self.cycle_repetition: Optional[Integer] = None
        self.fifo_depth: Optional[Integer] = None
        self.fifo_ranges: list[FlexrayFifoRange] = []
        self.msg_id_mask: Optional[Integer] = None
        self.msg_id_match: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayFifoConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayFifoConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize admit_without
        if self.admit_without is not None:
            serialized = SerializationHelper.serialize_item(self.admit_without, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADMIT-WITHOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize base_cycle
        if self.base_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.base_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize channel_ref
        if self.channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.channel_ref, "FlexrayPhysicalChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cycle_repetition
        if self.cycle_repetition is not None:
            serialized = SerializationHelper.serialize_item(self.cycle_repetition, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE-REPETITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fifo_depth
        if self.fifo_depth is not None:
            serialized = SerializationHelper.serialize_item(self.fifo_depth, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIFO-DEPTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fifo_ranges (list to container "FIFO-RANGES")
        if self.fifo_ranges:
            wrapper = ET.Element("FIFO-RANGES")
            for item in self.fifo_ranges:
                serialized = SerializationHelper.serialize_item(item, "FlexrayFifoRange")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize msg_id_mask
        if self.msg_id_mask is not None:
            serialized = SerializationHelper.serialize_item(self.msg_id_mask, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSG-ID-MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msg_id_match
        if self.msg_id_match is not None:
            serialized = SerializationHelper.serialize_item(self.msg_id_match, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSG-ID-MATCH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFifoConfiguration":
        """Deserialize XML element to FlexrayFifoConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayFifoConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayFifoConfiguration, cls).deserialize(element)

        # Parse admit_without
        child = SerializationHelper.find_child_element(element, "ADMIT-WITHOUT")
        if child is not None:
            admit_without_value = child.text
            obj.admit_without = admit_without_value

        # Parse base_cycle
        child = SerializationHelper.find_child_element(element, "BASE-CYCLE")
        if child is not None:
            base_cycle_value = child.text
            obj.base_cycle = base_cycle_value

        # Parse channel_ref
        child = SerializationHelper.find_child_element(element, "CHANNEL-REF")
        if child is not None:
            channel_ref_value = ARRef.deserialize(child)
            obj.channel_ref = channel_ref_value

        # Parse cycle_repetition
        child = SerializationHelper.find_child_element(element, "CYCLE-REPETITION")
        if child is not None:
            cycle_repetition_value = child.text
            obj.cycle_repetition = cycle_repetition_value

        # Parse fifo_depth
        child = SerializationHelper.find_child_element(element, "FIFO-DEPTH")
        if child is not None:
            fifo_depth_value = child.text
            obj.fifo_depth = fifo_depth_value

        # Parse fifo_ranges (list from container "FIFO-RANGES")
        obj.fifo_ranges = []
        container = SerializationHelper.find_child_element(element, "FIFO-RANGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.fifo_ranges.append(child_value)

        # Parse msg_id_mask
        child = SerializationHelper.find_child_element(element, "MSG-ID-MASK")
        if child is not None:
            msg_id_mask_value = child.text
            obj.msg_id_mask = msg_id_mask_value

        # Parse msg_id_match
        child = SerializationHelper.find_child_element(element, "MSG-ID-MATCH")
        if child is not None:
            msg_id_match_value = child.text
            obj.msg_id_match = msg_id_match_value

        return obj



class FlexrayFifoConfigurationBuilder(BuilderBase):
    """Builder for FlexrayFifoConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayFifoConfiguration = FlexrayFifoConfiguration()


    def with_admit_without(self, value: Optional[Boolean]) -> "FlexrayFifoConfigurationBuilder":
        """Set admit_without attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admit_without = value
        return self

    def with_base_cycle(self, value: Optional[Integer]) -> "FlexrayFifoConfigurationBuilder":
        """Set base_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_cycle = value
        return self

    def with_channel(self, value: Optional[FlexrayPhysicalChannel]) -> "FlexrayFifoConfigurationBuilder":
        """Set channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.channel = value
        return self

    def with_cycle_repetition(self, value: Optional[Integer]) -> "FlexrayFifoConfigurationBuilder":
        """Set cycle_repetition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cycle_repetition = value
        return self

    def with_fifo_depth(self, value: Optional[Integer]) -> "FlexrayFifoConfigurationBuilder":
        """Set fifo_depth attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fifo_depth = value
        return self

    def with_fifo_ranges(self, items: list[FlexrayFifoRange]) -> "FlexrayFifoConfigurationBuilder":
        """Set fifo_ranges list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.fifo_ranges = list(items) if items else []
        return self

    def with_msg_id_mask(self, value: Optional[Integer]) -> "FlexrayFifoConfigurationBuilder":
        """Set msg_id_mask attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msg_id_mask = value
        return self

    def with_msg_id_match(self, value: Optional[Integer]) -> "FlexrayFifoConfigurationBuilder":
        """Set msg_id_match attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msg_id_match = value
        return self


    def add_fifo_range(self, item: FlexrayFifoRange) -> "FlexrayFifoConfigurationBuilder":
        """Add a single item to fifo_ranges list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.fifo_ranges.append(item)
        return self

    def clear_fifo_ranges(self) -> "FlexrayFifoConfigurationBuilder":
        """Clear all items from fifo_ranges list.

        Returns:
            self for method chaining
        """
        self._obj.fifo_ranges = []
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


    def build(self) -> FlexrayFifoConfiguration:
        """Build and return the FlexrayFifoConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj