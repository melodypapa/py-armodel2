"""IEEE1722TpAcfCanPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 661)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import IEEE1722TpAcfBusPartBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameTxBehaviorEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.rx_identifier_range import (
    RxIdentifierRange,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpAcfCanPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfCanPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-E-E-E1722-TP-ACF-CAN-PART"


    can_addressing: Optional[CanAddressingModeType]
    can_bit_rate_switch: Optional[Boolean]
    can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum]
    can_identifier: Optional[RxIdentifierRange]
    sdu_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CAN-ADDRESSING": lambda obj, elem: setattr(obj, "can_addressing", CanAddressingModeType.deserialize(elem)),
        "CAN-BIT-RATE-SWITCH": lambda obj, elem: setattr(obj, "can_bit_rate_switch", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "CAN-FRAME-TX-BEHAVIOR": lambda obj, elem: setattr(obj, "can_frame_tx_behavior", CanFrameTxBehaviorEnum.deserialize(elem)),
        "CAN-IDENTIFIER": lambda obj, elem: setattr(obj, "can_identifier", SerializationHelper.deserialize_by_tag(elem, "RxIdentifierRange")),
        "SDU-REF": lambda obj, elem: setattr(obj, "sdu_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCanPart."""
        super().__init__()
        self.can_addressing: Optional[CanAddressingModeType] = None
        self.can_bit_rate_switch: Optional[Boolean] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_identifier: Optional[RxIdentifierRange] = None
        self.sdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfCanPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfCanPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize can_addressing
        if self.can_addressing is not None:
            serialized = SerializationHelper.serialize_item(self.can_addressing, "CanAddressingModeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-ADDRESSING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_bit_rate_switch
        if self.can_bit_rate_switch is not None:
            serialized = SerializationHelper.serialize_item(self.can_bit_rate_switch, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-BIT-RATE-SWITCH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_frame_tx_behavior
        if self.can_frame_tx_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.can_frame_tx_behavior, "CanFrameTxBehaviorEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-FRAME-TX-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_identifier
        if self.can_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.can_identifier, "RxIdentifierRange")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_ref
        if self.sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfCanPart":
        """Deserialize XML element to IEEE1722TpAcfCanPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfCanPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfCanPart, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CAN-ADDRESSING":
                setattr(obj, "can_addressing", CanAddressingModeType.deserialize(child))
            elif tag == "CAN-BIT-RATE-SWITCH":
                setattr(obj, "can_bit_rate_switch", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "CAN-FRAME-TX-BEHAVIOR":
                setattr(obj, "can_frame_tx_behavior", CanFrameTxBehaviorEnum.deserialize(child))
            elif tag == "CAN-IDENTIFIER":
                setattr(obj, "can_identifier", SerializationHelper.deserialize_by_tag(child, "RxIdentifierRange"))
            elif tag == "SDU-REF":
                setattr(obj, "sdu_ref", ARRef.deserialize(child))

        return obj



class IEEE1722TpAcfCanPartBuilder(IEEE1722TpAcfBusPartBuilder):
    """Builder for IEEE1722TpAcfCanPart with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpAcfCanPart = IEEE1722TpAcfCanPart()


    def with_can_addressing(self, value: Optional[CanAddressingModeType]) -> "IEEE1722TpAcfCanPartBuilder":
        """Set can_addressing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_addressing = value
        return self

    def with_can_bit_rate_switch(self, value: Optional[Boolean]) -> "IEEE1722TpAcfCanPartBuilder":
        """Set can_bit_rate_switch attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_bit_rate_switch = value
        return self

    def with_can_frame_tx_behavior(self, value: Optional[CanFrameTxBehaviorEnum]) -> "IEEE1722TpAcfCanPartBuilder":
        """Set can_frame_tx_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_frame_tx_behavior = value
        return self

    def with_can_identifier(self, value: Optional[RxIdentifierRange]) -> "IEEE1722TpAcfCanPartBuilder":
        """Set can_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_identifier = value
        return self

    def with_sdu(self, value: Optional[PduTriggering]) -> "IEEE1722TpAcfCanPartBuilder":
        """Set sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdu = value
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


    def build(self) -> IEEE1722TpAcfCanPart:
        """Build and return the IEEE1722TpAcfCanPart instance with validation."""
        self._validate_instance()
        pass
        return self._obj