"""ISignalIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 994)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import IPduBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_timing import (
    IPduTiming,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ISignalIPdu(IPdu):
    """AUTOSAR ISignalIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_timing_specification: Optional[IPduTiming]
    i_signal_to_pdu_mapping_refs: list[ARRef]
    unused_bit_pattern: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ISignalIPdu."""
        super().__init__()
        self.i_pdu_timing_specification: Optional[IPduTiming] = None
        self.i_signal_to_pdu_mapping_refs: list[ARRef] = []
        self.unused_bit_pattern: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize ISignalIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_timing_specification
        if self.i_pdu_timing_specification is not None:
            serialized = SerializationHelper.serialize_item(self.i_pdu_timing_specification, "IPduTiming")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-TIMING-SPECIFICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_to_pdu_mapping_refs (list to container "I-SIGNAL-TO-PDU-MAPPING-REFS")
        if self.i_signal_to_pdu_mapping_refs:
            wrapper = ET.Element("I-SIGNAL-TO-PDU-MAPPING-REFS")
            for item in self.i_signal_to_pdu_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalToIPduMapping")
                if serialized is not None:
                    child_elem = ET.Element("I-SIGNAL-TO-PDU-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize unused_bit_pattern
        if self.unused_bit_pattern is not None:
            serialized = SerializationHelper.serialize_item(self.unused_bit_pattern, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNUSED-BIT-PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalIPdu":
        """Deserialize XML element to ISignalIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalIPdu, cls).deserialize(element)

        # Parse i_pdu_timing_specification
        child = SerializationHelper.find_child_element(element, "I-PDU-TIMING-SPECIFICATION")
        if child is not None:
            i_pdu_timing_specification_value = SerializationHelper.deserialize_by_tag(child, "IPduTiming")
            obj.i_pdu_timing_specification = i_pdu_timing_specification_value

        # Parse i_signal_to_pdu_mapping_refs (list from container "I-SIGNAL-TO-PDU-MAPPING-REFS")
        obj.i_signal_to_pdu_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "I-SIGNAL-TO-PDU-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_to_pdu_mapping_refs.append(child_value)

        # Parse unused_bit_pattern
        child = SerializationHelper.find_child_element(element, "UNUSED-BIT-PATTERN")
        if child is not None:
            unused_bit_pattern_value = child.text
            obj.unused_bit_pattern = unused_bit_pattern_value

        return obj



class ISignalIPduBuilder(IPduBuilder):
    """Builder for ISignalIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ISignalIPdu = ISignalIPdu()


    def with_i_pdu_timing_specification(self, value: Optional[IPduTiming]) -> "ISignalIPduBuilder":
        """Set i_pdu_timing_specification attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_pdu_timing_specification = value
        return self

    def with_i_signal_to_pdu_mappings(self, items: list[ISignalToIPduMapping]) -> "ISignalIPduBuilder":
        """Set i_signal_to_pdu_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_signal_to_pdu_mappings = list(items) if items else []
        return self

    def with_unused_bit_pattern(self, value: Optional[Integer]) -> "ISignalIPduBuilder":
        """Set unused_bit_pattern attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unused_bit_pattern = value
        return self


    def add_i_signal_to_pdu_mapping(self, item: ISignalToIPduMapping) -> "ISignalIPduBuilder":
        """Add a single item to i_signal_to_pdu_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_signal_to_pdu_mappings.append(item)
        return self

    def clear_i_signal_to_pdu_mappings(self) -> "ISignalIPduBuilder":
        """Clear all items from i_signal_to_pdu_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.i_signal_to_pdu_mappings = []
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


    def build(self) -> ISignalIPdu:
        """Build and return the ISignalIPdu instance with validation."""
        self._validate_instance()
        pass
        return self._obj