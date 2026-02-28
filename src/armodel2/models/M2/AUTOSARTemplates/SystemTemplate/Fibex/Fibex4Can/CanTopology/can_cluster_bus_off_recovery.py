"""CanClusterBusOffRecovery AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanClusterBusOffRecovery(ARObject):
    """AUTOSAR CanClusterBusOffRecovery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-CLUSTER-BUS-OFF-RECOVERY"


    bor_counter_l1_to: Optional[PositiveInteger]
    bor_time_l1: Optional[TimeValue]
    bor_time_l2: Optional[TimeValue]
    bor_time_tx: Optional[TimeValue]
    main_function: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "BOR-COUNTER-L1-TO": lambda obj, elem: setattr(obj, "bor_counter_l1_to", elem.text),
        "BOR-TIME-L1": lambda obj, elem: setattr(obj, "bor_time_l1", elem.text),
        "BOR-TIME-L2": lambda obj, elem: setattr(obj, "bor_time_l2", elem.text),
        "BOR-TIME-TX": lambda obj, elem: setattr(obj, "bor_time_tx", elem.text),
        "MAIN-FUNCTION": lambda obj, elem: setattr(obj, "main_function", elem.text),
    }


    def __init__(self) -> None:
        """Initialize CanClusterBusOffRecovery."""
        super().__init__()
        self.bor_counter_l1_to: Optional[PositiveInteger] = None
        self.bor_time_l1: Optional[TimeValue] = None
        self.bor_time_l2: Optional[TimeValue] = None
        self.bor_time_tx: Optional[TimeValue] = None
        self.main_function: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize CanClusterBusOffRecovery to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanClusterBusOffRecovery, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bor_counter_l1_to
        if self.bor_counter_l1_to is not None:
            serialized = SerializationHelper.serialize_item(self.bor_counter_l1_to, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BOR-COUNTER-L1-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bor_time_l1
        if self.bor_time_l1 is not None:
            serialized = SerializationHelper.serialize_item(self.bor_time_l1, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BOR-TIME-L1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bor_time_l2
        if self.bor_time_l2 is not None:
            serialized = SerializationHelper.serialize_item(self.bor_time_l2, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BOR-TIME-L2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bor_time_tx
        if self.bor_time_tx is not None:
            serialized = SerializationHelper.serialize_item(self.bor_time_tx, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BOR-TIME-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize main_function
        if self.main_function is not None:
            serialized = SerializationHelper.serialize_item(self.main_function, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAIN-FUNCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanClusterBusOffRecovery":
        """Deserialize XML element to CanClusterBusOffRecovery object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanClusterBusOffRecovery object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanClusterBusOffRecovery, cls).deserialize(element)

        # Parse bor_counter_l1_to
        child = SerializationHelper.find_child_element(element, "BOR-COUNTER-L1-TO")
        if child is not None:
            bor_counter_l1_to_value = child.text
            obj.bor_counter_l1_to = bor_counter_l1_to_value

        # Parse bor_time_l1
        child = SerializationHelper.find_child_element(element, "BOR-TIME-L1")
        if child is not None:
            bor_time_l1_value = child.text
            obj.bor_time_l1 = bor_time_l1_value

        # Parse bor_time_l2
        child = SerializationHelper.find_child_element(element, "BOR-TIME-L2")
        if child is not None:
            bor_time_l2_value = child.text
            obj.bor_time_l2 = bor_time_l2_value

        # Parse bor_time_tx
        child = SerializationHelper.find_child_element(element, "BOR-TIME-TX")
        if child is not None:
            bor_time_tx_value = child.text
            obj.bor_time_tx = bor_time_tx_value

        # Parse main_function
        child = SerializationHelper.find_child_element(element, "MAIN-FUNCTION")
        if child is not None:
            main_function_value = child.text
            obj.main_function = main_function_value

        return obj



class CanClusterBusOffRecoveryBuilder(BuilderBase):
    """Builder for CanClusterBusOffRecovery with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanClusterBusOffRecovery = CanClusterBusOffRecovery()


    def with_bor_counter_l1_to(self, value: Optional[PositiveInteger]) -> "CanClusterBusOffRecoveryBuilder":
        """Set bor_counter_l1_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bor_counter_l1_to = value
        return self

    def with_bor_time_l1(self, value: Optional[TimeValue]) -> "CanClusterBusOffRecoveryBuilder":
        """Set bor_time_l1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bor_time_l1 = value
        return self

    def with_bor_time_l2(self, value: Optional[TimeValue]) -> "CanClusterBusOffRecoveryBuilder":
        """Set bor_time_l2 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bor_time_l2 = value
        return self

    def with_bor_time_tx(self, value: Optional[TimeValue]) -> "CanClusterBusOffRecoveryBuilder":
        """Set bor_time_tx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bor_time_tx = value
        return self

    def with_main_function(self, value: Optional[TimeValue]) -> "CanClusterBusOffRecoveryBuilder":
        """Set main_function attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.main_function = value
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


    def build(self) -> CanClusterBusOffRecovery:
        """Build and return the CanClusterBusOffRecovery instance with validation."""
        self._validate_instance()
        pass
        return self._obj