"""FlexrayTpEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayTpEcu(ARObject):
    """AUTOSAR FlexrayTpEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cancellation: Optional[Boolean]
    cycle_time_main: Optional[TimeValue]
    ecu_instance_ref: Optional[ARRef]
    full_duplex: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize FlexrayTpEcu."""
        super().__init__()
        self.cancellation: Optional[Boolean] = None
        self.cycle_time_main: Optional[TimeValue] = None
        self.ecu_instance_ref: Optional[ARRef] = None
        self.full_duplex: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpEcu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cancellation
        if self.cancellation is not None:
            serialized = SerializationHelper.serialize_item(self.cancellation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CANCELLATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cycle_time_main
        if self.cycle_time_main is not None:
            serialized = SerializationHelper.serialize_item(self.cycle_time_main, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE-TIME-MAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize full_duplex
        if self.full_duplex is not None:
            serialized = SerializationHelper.serialize_item(self.full_duplex, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FULL-DUPLEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpEcu":
        """Deserialize XML element to FlexrayTpEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpEcu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpEcu, cls).deserialize(element)

        # Parse cancellation
        child = SerializationHelper.find_child_element(element, "CANCELLATION")
        if child is not None:
            cancellation_value = child.text
            obj.cancellation = cancellation_value

        # Parse cycle_time_main
        child = SerializationHelper.find_child_element(element, "CYCLE-TIME-MAIN")
        if child is not None:
            cycle_time_main_value = child.text
            obj.cycle_time_main = cycle_time_main_value

        # Parse ecu_instance_ref
        child = SerializationHelper.find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse full_duplex
        child = SerializationHelper.find_child_element(element, "FULL-DUPLEX")
        if child is not None:
            full_duplex_value = child.text
            obj.full_duplex = full_duplex_value

        return obj



class FlexrayTpEcuBuilder(BuilderBase):
    """Builder for FlexrayTpEcu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayTpEcu = FlexrayTpEcu()


    def with_cancellation(self, value: Optional[Boolean]) -> "FlexrayTpEcuBuilder":
        """Set cancellation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cancellation = value
        return self

    def with_cycle_time_main(self, value: Optional[TimeValue]) -> "FlexrayTpEcuBuilder":
        """Set cycle_time_main attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cycle_time_main = value
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "FlexrayTpEcuBuilder":
        """Set ecu_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_instance = value
        return self

    def with_full_duplex(self, value: Optional[Boolean]) -> "FlexrayTpEcuBuilder":
        """Set full_duplex attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.full_duplex = value
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


    def build(self) -> FlexrayTpEcu:
        """Build and return the FlexrayTpEcu instance with validation."""
        self._validate_instance()
        pass
        return self._obj