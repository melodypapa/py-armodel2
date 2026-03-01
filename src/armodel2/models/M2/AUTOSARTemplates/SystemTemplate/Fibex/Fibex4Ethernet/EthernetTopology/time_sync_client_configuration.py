"""TimeSyncClientConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncTechnologyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ordered_master import (
    OrderedMaster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TimeSyncClientConfiguration(ARObject):
    """AUTOSAR TimeSyncClientConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TIME-SYNC-CLIENT-CONFIGURATION"


    ordered_masters: list[OrderedMaster]
    time_sync: Optional[TimeSyncTechnologyEnum]
    _DESERIALIZE_DISPATCH = {
        "ORDERED-MASTERS": lambda obj, elem: obj.ordered_masters.append(SerializationHelper.deserialize_by_tag(elem, "OrderedMaster")),
        "TIME-SYNC": lambda obj, elem: setattr(obj, "time_sync", TimeSyncTechnologyEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TimeSyncClientConfiguration."""
        super().__init__()
        self.ordered_masters: list[OrderedMaster] = []
        self.time_sync: Optional[TimeSyncTechnologyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TimeSyncClientConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimeSyncClientConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ordered_masters (list to container "ORDERED-MASTERS")
        if self.ordered_masters:
            wrapper = ET.Element("ORDERED-MASTERS")
            for item in self.ordered_masters:
                serialized = SerializationHelper.serialize_item(item, "OrderedMaster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize time_sync
        if self.time_sync is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync, "TimeSyncTechnologyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSyncClientConfiguration":
        """Deserialize XML element to TimeSyncClientConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeSyncClientConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimeSyncClientConfiguration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ORDERED-MASTERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ordered_masters.append(SerializationHelper.deserialize_by_tag(item_elem, "OrderedMaster"))
            elif tag == "TIME-SYNC":
                setattr(obj, "time_sync", TimeSyncTechnologyEnum.deserialize(child))

        return obj



class TimeSyncClientConfigurationBuilder(BuilderBase):
    """Builder for TimeSyncClientConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimeSyncClientConfiguration = TimeSyncClientConfiguration()


    def with_ordered_masters(self, items: list[OrderedMaster]) -> "TimeSyncClientConfigurationBuilder":
        """Set ordered_masters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ordered_masters = list(items) if items else []
        return self

    def with_time_sync(self, value: Optional[TimeSyncTechnologyEnum]) -> "TimeSyncClientConfigurationBuilder":
        """Set time_sync attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_sync = value
        return self


    def add_ordered_master(self, item: OrderedMaster) -> "TimeSyncClientConfigurationBuilder":
        """Add a single item to ordered_masters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ordered_masters.append(item)
        return self

    def clear_ordered_masters(self) -> "TimeSyncClientConfigurationBuilder":
        """Clear all items from ordered_masters list.

        Returns:
            self for method chaining
        """
        self._obj.ordered_masters = []
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


    def build(self) -> TimeSyncClientConfiguration:
        """Build and return the TimeSyncClientConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj