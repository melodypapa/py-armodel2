"""BusMirrorChannelMappingCan AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 700)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import BusMirrorChannelMappingBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_can_id_range_mapping import (
    BusMirrorCanIdRangeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_can_id_to_can_id_mapping import (
    BusMirrorCanIdToCanIdMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_lin_pid_to_can_id_mapping import (
    BusMirrorLinPidToCanIdMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class BusMirrorChannelMappingCan(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingCan."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    can_id_ranges: list[BusMirrorCanIdRangeMapping]
    can_id_to_can_ids: list[BusMirrorCanIdToCanIdMapping]
    lin_pid_to_can_ids: list[BusMirrorLinPidToCanIdMapping]
    mirror_source_lin: Optional[PositiveInteger]
    mirror_status: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingCan."""
        super().__init__()
        self.can_id_ranges: list[BusMirrorCanIdRangeMapping] = []
        self.can_id_to_can_ids: list[BusMirrorCanIdToCanIdMapping] = []
        self.lin_pid_to_can_ids: list[BusMirrorLinPidToCanIdMapping] = []
        self.mirror_source_lin: Optional[PositiveInteger] = None
        self.mirror_status: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorChannelMappingCan to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorChannelMappingCan, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize can_id_ranges (list to container "CAN-ID-RANGES")
        if self.can_id_ranges:
            wrapper = ET.Element("CAN-ID-RANGES")
            for item in self.can_id_ranges:
                serialized = SerializationHelper.serialize_item(item, "BusMirrorCanIdRangeMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_id_to_can_ids (list to container "CAN-ID-TO-CAN-IDS")
        if self.can_id_to_can_ids:
            wrapper = ET.Element("CAN-ID-TO-CAN-IDS")
            for item in self.can_id_to_can_ids:
                serialized = SerializationHelper.serialize_item(item, "BusMirrorCanIdToCanIdMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize lin_pid_to_can_ids (list to container "LIN-PID-TO-CAN-IDS")
        if self.lin_pid_to_can_ids:
            wrapper = ET.Element("LIN-PID-TO-CAN-IDS")
            for item in self.lin_pid_to_can_ids:
                serialized = SerializationHelper.serialize_item(item, "BusMirrorLinPidToCanIdMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mirror_source_lin
        if self.mirror_source_lin is not None:
            serialized = SerializationHelper.serialize_item(self.mirror_source_lin, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIRROR-SOURCE-LIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mirror_status
        if self.mirror_status is not None:
            serialized = SerializationHelper.serialize_item(self.mirror_status, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIRROR-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMappingCan":
        """Deserialize XML element to BusMirrorChannelMappingCan object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannelMappingCan object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorChannelMappingCan, cls).deserialize(element)

        # Parse can_id_ranges (list from container "CAN-ID-RANGES")
        obj.can_id_ranges = []
        container = SerializationHelper.find_child_element(element, "CAN-ID-RANGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.can_id_ranges.append(child_value)

        # Parse can_id_to_can_ids (list from container "CAN-ID-TO-CAN-IDS")
        obj.can_id_to_can_ids = []
        container = SerializationHelper.find_child_element(element, "CAN-ID-TO-CAN-IDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.can_id_to_can_ids.append(child_value)

        # Parse lin_pid_to_can_ids (list from container "LIN-PID-TO-CAN-IDS")
        obj.lin_pid_to_can_ids = []
        container = SerializationHelper.find_child_element(element, "LIN-PID-TO-CAN-IDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_pid_to_can_ids.append(child_value)

        # Parse mirror_source_lin
        child = SerializationHelper.find_child_element(element, "MIRROR-SOURCE-LIN")
        if child is not None:
            mirror_source_lin_value = child.text
            obj.mirror_source_lin = mirror_source_lin_value

        # Parse mirror_status
        child = SerializationHelper.find_child_element(element, "MIRROR-STATUS")
        if child is not None:
            mirror_status_value = child.text
            obj.mirror_status = mirror_status_value

        return obj



class BusMirrorChannelMappingCanBuilder(BusMirrorChannelMappingBuilder):
    """Builder for BusMirrorChannelMappingCan with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BusMirrorChannelMappingCan = BusMirrorChannelMappingCan()


    def with_can_id_ranges(self, items: list[BusMirrorCanIdRangeMapping]) -> "BusMirrorChannelMappingCanBuilder":
        """Set can_id_ranges list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.can_id_ranges = list(items) if items else []
        return self

    def with_can_id_to_can_ids(self, items: list[BusMirrorCanIdToCanIdMapping]) -> "BusMirrorChannelMappingCanBuilder":
        """Set can_id_to_can_ids list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.can_id_to_can_ids = list(items) if items else []
        return self

    def with_lin_pid_to_can_ids(self, items: list[BusMirrorLinPidToCanIdMapping]) -> "BusMirrorChannelMappingCanBuilder":
        """Set lin_pid_to_can_ids list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.lin_pid_to_can_ids = list(items) if items else []
        return self

    def with_mirror_source_lin(self, value: Optional[PositiveInteger]) -> "BusMirrorChannelMappingCanBuilder":
        """Set mirror_source_lin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mirror_source_lin = value
        return self

    def with_mirror_status(self, value: Optional[PositiveInteger]) -> "BusMirrorChannelMappingCanBuilder":
        """Set mirror_status attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mirror_status = value
        return self


    def add_can_id_range(self, item: BusMirrorCanIdRangeMapping) -> "BusMirrorChannelMappingCanBuilder":
        """Add a single item to can_id_ranges list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.can_id_ranges.append(item)
        return self

    def clear_can_id_ranges(self) -> "BusMirrorChannelMappingCanBuilder":
        """Clear all items from can_id_ranges list.

        Returns:
            self for method chaining
        """
        self._obj.can_id_ranges = []
        return self

    def add_can_id_to_can_id(self, item: BusMirrorCanIdToCanIdMapping) -> "BusMirrorChannelMappingCanBuilder":
        """Add a single item to can_id_to_can_ids list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.can_id_to_can_ids.append(item)
        return self

    def clear_can_id_to_can_ids(self) -> "BusMirrorChannelMappingCanBuilder":
        """Clear all items from can_id_to_can_ids list.

        Returns:
            self for method chaining
        """
        self._obj.can_id_to_can_ids = []
        return self

    def add_lin_pid_to_can_id(self, item: BusMirrorLinPidToCanIdMapping) -> "BusMirrorChannelMappingCanBuilder":
        """Add a single item to lin_pid_to_can_ids list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.lin_pid_to_can_ids.append(item)
        return self

    def clear_lin_pid_to_can_ids(self) -> "BusMirrorChannelMappingCanBuilder":
        """Clear all items from lin_pid_to_can_ids list.

        Returns:
            self for method chaining
        """
        self._obj.lin_pid_to_can_ids = []
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


    def build(self) -> BusMirrorChannelMappingCan:
        """Build and return the BusMirrorChannelMappingCan instance with validation."""
        self._validate_instance()
        pass
        return self._obj