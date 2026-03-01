"""FlexrayTpConnectionControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 593)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    FrArTpAckType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayTpConnectionControl(Identifiable):
    """AUTOSAR FlexrayTpConnectionControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-TP-CONNECTION-CONTROL"


    ack_type: Optional[FrArTpAckType]
    max_fc_wait: Optional[Integer]
    max_number_of: Optional[Integer]
    max_retries: Optional[Integer]
    separation_cycle: Optional[Integer]
    time_br: Optional[TimeValue]
    time_buffer: Optional[TimeValue]
    time_cs: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "ACK-TYPE": lambda obj, elem: setattr(obj, "ack_type", FrArTpAckType.deserialize(elem)),
        "MAX-FC-WAIT": lambda obj, elem: setattr(obj, "max_fc_wait", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MAX-NUMBER-OF": lambda obj, elem: setattr(obj, "max_number_of", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MAX-RETRIES": lambda obj, elem: setattr(obj, "max_retries", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SEPARATION-CYCLE": lambda obj, elem: setattr(obj, "separation_cycle", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "TIME-BR": lambda obj, elem: setattr(obj, "time_br", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIME-BUFFER": lambda obj, elem: setattr(obj, "time_buffer", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIME-CS": lambda obj, elem: setattr(obj, "time_cs", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-AR": lambda obj, elem: setattr(obj, "timeout_ar", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-AS": lambda obj, elem: setattr(obj, "timeout_as", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-BS": lambda obj, elem: setattr(obj, "timeout_bs", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-CR": lambda obj, elem: setattr(obj, "timeout_cr", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize FlexrayTpConnectionControl."""
        super().__init__()
        self.ack_type: Optional[FrArTpAckType] = None
        self.max_fc_wait: Optional[Integer] = None
        self.max_number_of: Optional[Integer] = None
        self.max_retries: Optional[Integer] = None
        self.separation_cycle: Optional[Integer] = None
        self.time_br: Optional[TimeValue] = None
        self.time_buffer: Optional[TimeValue] = None
        self.time_cs: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpConnectionControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpConnectionControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ack_type
        if self.ack_type is not None:
            serialized = SerializationHelper.serialize_item(self.ack_type, "FrArTpAckType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACK-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_fc_wait
        if self.max_fc_wait is not None:
            serialized = SerializationHelper.serialize_item(self.max_fc_wait, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-FC-WAIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_retries
        if self.max_retries is not None:
            serialized = SerializationHelper.serialize_item(self.max_retries, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-RETRIES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize separation_cycle
        if self.separation_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.separation_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEPARATION-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_br
        if self.time_br is not None:
            serialized = SerializationHelper.serialize_item(self.time_br, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_buffer
        if self.time_buffer is not None:
            serialized = SerializationHelper.serialize_item(self.time_buffer, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BUFFER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_cs
        if self.time_cs is not None:
            serialized = SerializationHelper.serialize_item(self.time_cs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-CS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_ar
        if self.timeout_ar is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_ar, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_as
        if self.timeout_as is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_as, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_bs
        if self.timeout_bs is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_bs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_cr
        if self.timeout_cr is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_cr, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-CR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConnectionControl":
        """Deserialize XML element to FlexrayTpConnectionControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpConnectionControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpConnectionControl, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACK-TYPE":
                setattr(obj, "ack_type", FrArTpAckType.deserialize(child))
            elif tag == "MAX-FC-WAIT":
                setattr(obj, "max_fc_wait", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "MAX-NUMBER-OF":
                setattr(obj, "max_number_of", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "MAX-RETRIES":
                setattr(obj, "max_retries", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "SEPARATION-CYCLE":
                setattr(obj, "separation_cycle", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "TIME-BR":
                setattr(obj, "time_br", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIME-BUFFER":
                setattr(obj, "time_buffer", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIME-CS":
                setattr(obj, "time_cs", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-AR":
                setattr(obj, "timeout_ar", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-AS":
                setattr(obj, "timeout_as", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-BS":
                setattr(obj, "timeout_bs", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-CR":
                setattr(obj, "timeout_cr", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class FlexrayTpConnectionControlBuilder(IdentifiableBuilder):
    """Builder for FlexrayTpConnectionControl with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayTpConnectionControl = FlexrayTpConnectionControl()


    def with_ack_type(self, value: Optional[FrArTpAckType]) -> "FlexrayTpConnectionControlBuilder":
        """Set ack_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ack_type = value
        return self

    def with_max_fc_wait(self, value: Optional[Integer]) -> "FlexrayTpConnectionControlBuilder":
        """Set max_fc_wait attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_fc_wait = value
        return self

    def with_max_number_of(self, value: Optional[Integer]) -> "FlexrayTpConnectionControlBuilder":
        """Set max_number_of attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_number_of = value
        return self

    def with_max_retries(self, value: Optional[Integer]) -> "FlexrayTpConnectionControlBuilder":
        """Set max_retries attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_retries = value
        return self

    def with_separation_cycle(self, value: Optional[Integer]) -> "FlexrayTpConnectionControlBuilder":
        """Set separation_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.separation_cycle = value
        return self

    def with_time_br(self, value: Optional[TimeValue]) -> "FlexrayTpConnectionControlBuilder":
        """Set time_br attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_br = value
        return self

    def with_time_buffer(self, value: Optional[TimeValue]) -> "FlexrayTpConnectionControlBuilder":
        """Set time_buffer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_buffer = value
        return self

    def with_time_cs(self, value: Optional[TimeValue]) -> "FlexrayTpConnectionControlBuilder":
        """Set time_cs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_cs = value
        return self

    def with_timeout_ar(self, value: Optional[TimeValue]) -> "FlexrayTpConnectionControlBuilder":
        """Set timeout_ar attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_ar = value
        return self

    def with_timeout_as(self, value: Optional[TimeValue]) -> "FlexrayTpConnectionControlBuilder":
        """Set timeout_as attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_as = value
        return self

    def with_timeout_bs(self, value: Optional[TimeValue]) -> "FlexrayTpConnectionControlBuilder":
        """Set timeout_bs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_bs = value
        return self

    def with_timeout_cr(self, value: Optional[TimeValue]) -> "FlexrayTpConnectionControlBuilder":
        """Set timeout_cr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_cr = value
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


    def build(self) -> FlexrayTpConnectionControl:
        """Build and return the FlexrayTpConnectionControl instance with validation."""
        self._validate_instance()
        pass
        return self._obj