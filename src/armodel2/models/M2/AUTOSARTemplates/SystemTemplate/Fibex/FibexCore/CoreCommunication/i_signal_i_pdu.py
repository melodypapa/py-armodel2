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

    _XML_TAG = "I-SIGNAL-I-PDU"


    i_pdu_timing_specifications: list[IPduTiming]
    i_signal_to_pdu_mappings: list[ISignalToIPduMapping]
    unused_bit_pattern: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "I-PDU-TIMING-SPECIFICATIONS": lambda obj, elem: obj.i_pdu_timing_specifications.append(SerializationHelper.deserialize_by_tag(elem, "IPduTiming")),
        "I-SIGNAL-TO-PDU-MAPPINGS": lambda obj, elem: obj.i_signal_to_pdu_mappings.append(SerializationHelper.deserialize_by_tag(elem, "ISignalToIPduMapping")),
        "UNUSED-BIT-PATTERN": lambda obj, elem: setattr(obj, "unused_bit_pattern", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize ISignalIPdu."""
        super().__init__()
        self.i_pdu_timing_specifications: list[IPduTiming] = []
        self.i_signal_to_pdu_mappings: list[ISignalToIPduMapping] = []
        self.unused_bit_pattern: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize ISignalIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize i_pdu_timing_specifications (list to container "I-PDU-TIMING-SPECIFICATIONS")
        if self.i_pdu_timing_specifications:
            wrapper = ET.Element("I-PDU-TIMING-SPECIFICATIONS")
            for item in self.i_pdu_timing_specifications:
                serialized = SerializationHelper.serialize_item(item, "IPduTiming")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_signal_to_pdu_mappings (list to container "I-SIGNAL-TO-PDU-MAPPINGS")
        if self.i_signal_to_pdu_mappings:
            wrapper = ET.Element("I-SIGNAL-TO-PDU-MAPPINGS")
            for item in self.i_signal_to_pdu_mappings:
                serialized = SerializationHelper.serialize_item(item, "ISignalToIPduMapping")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "I-PDU-TIMING-SPECIFICATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_pdu_timing_specifications.append(SerializationHelper.deserialize_by_tag(item_elem, "IPduTiming"))
            elif tag == "I-SIGNAL-TO-PDU-MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_signal_to_pdu_mappings.append(SerializationHelper.deserialize_by_tag(item_elem, "ISignalToIPduMapping"))
            elif tag == "UNUSED-BIT-PATTERN":
                setattr(obj, "unused_bit_pattern", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class ISignalIPduBuilder(IPduBuilder):
    """Builder for ISignalIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ISignalIPdu = ISignalIPdu()


    def with_i_pdu_timing_specifications(self, items: list[IPduTiming]) -> "ISignalIPduBuilder":
        """Set i_pdu_timing_specifications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_timing_specifications = list(items) if items else []
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


    def add_i_pdu_timing_specification(self, item: IPduTiming) -> "ISignalIPduBuilder":
        """Add a single item to i_pdu_timing_specifications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_timing_specifications.append(item)
        return self

    def clear_i_pdu_timing_specifications(self) -> "ISignalIPduBuilder":
        """Clear all items from i_pdu_timing_specifications list.

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_timing_specifications = []
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