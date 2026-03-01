"""FlexrayNmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 678)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import NmClusterBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayNmCluster(NmCluster):
    """AUTOSAR FlexrayNmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-NM-CLUSTER"


    nm_car_wake_up: Optional[Boolean]
    nm_data_cycle: Optional[Integer]
    nm_main: Optional[TimeValue]
    nm_remote: Optional[TimeValue]
    nm_repeat: Optional[TimeValue]
    nm_repetition: Optional[Integer]
    nm_voting_cycle: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "NM-CAR-WAKE-UP": lambda obj, elem: setattr(obj, "nm_car_wake_up", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "NM-DATA-CYCLE": lambda obj, elem: setattr(obj, "nm_data_cycle", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NM-MAIN": lambda obj, elem: setattr(obj, "nm_main", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "NM-REMOTE": lambda obj, elem: setattr(obj, "nm_remote", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "NM-REPEAT": lambda obj, elem: setattr(obj, "nm_repeat", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "NM-REPETITION": lambda obj, elem: setattr(obj, "nm_repetition", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NM-VOTING-CYCLE": lambda obj, elem: setattr(obj, "nm_voting_cycle", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize FlexrayNmCluster."""
        super().__init__()
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_data_cycle: Optional[Integer] = None
        self.nm_main: Optional[TimeValue] = None
        self.nm_remote: Optional[TimeValue] = None
        self.nm_repeat: Optional[TimeValue] = None
        self.nm_repetition: Optional[Integer] = None
        self.nm_voting_cycle: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayNmCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayNmCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_car_wake_up
        if self.nm_car_wake_up is not None:
            serialized = SerializationHelper.serialize_item(self.nm_car_wake_up, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CAR-WAKE-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_data_cycle
        if self.nm_data_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.nm_data_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-DATA-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_main
        if self.nm_main is not None:
            serialized = SerializationHelper.serialize_item(self.nm_main, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_remote
        if self.nm_remote is not None:
            serialized = SerializationHelper.serialize_item(self.nm_remote, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REMOTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_repeat
        if self.nm_repeat is not None:
            serialized = SerializationHelper.serialize_item(self.nm_repeat, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REPEAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_repetition
        if self.nm_repetition is not None:
            serialized = SerializationHelper.serialize_item(self.nm_repetition, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REPETITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_voting_cycle
        if self.nm_voting_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.nm_voting_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-VOTING-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmCluster":
        """Deserialize XML element to FlexrayNmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayNmCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayNmCluster, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "NM-CAR-WAKE-UP":
                setattr(obj, "nm_car_wake_up", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "NM-DATA-CYCLE":
                setattr(obj, "nm_data_cycle", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "NM-MAIN":
                setattr(obj, "nm_main", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "NM-REMOTE":
                setattr(obj, "nm_remote", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "NM-REPEAT":
                setattr(obj, "nm_repeat", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "NM-REPETITION":
                setattr(obj, "nm_repetition", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "NM-VOTING-CYCLE":
                setattr(obj, "nm_voting_cycle", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class FlexrayNmClusterBuilder(NmClusterBuilder):
    """Builder for FlexrayNmCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayNmCluster = FlexrayNmCluster()


    def with_nm_car_wake_up(self, value: Optional[Boolean]) -> "FlexrayNmClusterBuilder":
        """Set nm_car_wake_up attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_car_wake_up = value
        return self

    def with_nm_data_cycle(self, value: Optional[Integer]) -> "FlexrayNmClusterBuilder":
        """Set nm_data_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_data_cycle = value
        return self

    def with_nm_main(self, value: Optional[TimeValue]) -> "FlexrayNmClusterBuilder":
        """Set nm_main attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_main = value
        return self

    def with_nm_remote(self, value: Optional[TimeValue]) -> "FlexrayNmClusterBuilder":
        """Set nm_remote attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_remote = value
        return self

    def with_nm_repeat(self, value: Optional[TimeValue]) -> "FlexrayNmClusterBuilder":
        """Set nm_repeat attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_repeat = value
        return self

    def with_nm_repetition(self, value: Optional[Integer]) -> "FlexrayNmClusterBuilder":
        """Set nm_repetition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_repetition = value
        return self

    def with_nm_voting_cycle(self, value: Optional[Integer]) -> "FlexrayNmClusterBuilder":
        """Set nm_voting_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_voting_cycle = value
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


    def build(self) -> FlexrayNmCluster:
        """Build and return the FlexrayNmCluster instance with validation."""
        self._validate_instance()
        pass
        return self._obj