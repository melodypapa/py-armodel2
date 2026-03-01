"""CanFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import FrameTriggeringBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameRxBehaviorEnum,
    CanFrameTxBehaviorEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_xl_frame_triggering_props import (
    CanXlFrameTriggeringProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.rx_identifier_range import (
    RxIdentifierRange,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication.ttcan_absolutely_scheduled_timing import (
    TtcanAbsolutelyScheduledTiming,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanFrameTriggering(FrameTriggering):
    """AUTOSAR CanFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-FRAME-TRIGGERING"


    absolutely_can_frame_triggerings: list[TtcanAbsolutelyScheduledTiming]
    can_addressing_mode: Optional[CanAddressingModeType]
    can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum]
    can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum]
    can_xl_frame_triggering_props: Optional[CanXlFrameTriggeringProps]
    identifier: Optional[Integer]
    j1939requestable: Optional[Boolean]
    rx_identifier_range: Optional[RxIdentifierRange]
    rx_mask: Optional[PositiveInteger]
    tx_mask: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ABSOLUTELY-CAN-FRAME-TRIGGERINGS": lambda obj, elem: obj.absolutely_can_frame_triggerings.append(SerializationHelper.deserialize_by_tag(elem, "TtcanAbsolutelyScheduledTiming")),
        "CAN-ADDRESSING-MODE": lambda obj, elem: setattr(obj, "can_addressing_mode", CanAddressingModeType.deserialize(elem)),
        "CAN-FRAME-RX-BEHAVIOR": lambda obj, elem: setattr(obj, "can_frame_rx_behavior", CanFrameRxBehaviorEnum.deserialize(elem)),
        "CAN-FRAME-TX-BEHAVIOR": lambda obj, elem: setattr(obj, "can_frame_tx_behavior", CanFrameTxBehaviorEnum.deserialize(elem)),
        "CAN-XL-FRAME-TRIGGERING-PROPS": lambda obj, elem: setattr(obj, "can_xl_frame_triggering_props", SerializationHelper.deserialize_by_tag(elem, "CanXlFrameTriggeringProps")),
        "IDENTIFIER": lambda obj, elem: setattr(obj, "identifier", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "J1939REQUESTABLE": lambda obj, elem: setattr(obj, "j1939requestable", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RX-IDENTIFIER-RANGE": lambda obj, elem: setattr(obj, "rx_identifier_range", SerializationHelper.deserialize_by_tag(elem, "RxIdentifierRange")),
        "RX-MASK": lambda obj, elem: setattr(obj, "rx_mask", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TX-MASK": lambda obj, elem: setattr(obj, "tx_mask", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize CanFrameTriggering."""
        super().__init__()
        self.absolutely_can_frame_triggerings: list[TtcanAbsolutelyScheduledTiming] = []
        self.can_addressing_mode: Optional[CanAddressingModeType] = None
        self.can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_xl_frame_triggering_props: Optional[CanXlFrameTriggeringProps] = None
        self.identifier: Optional[Integer] = None
        self.j1939requestable: Optional[Boolean] = None
        self.rx_identifier_range: Optional[RxIdentifierRange] = None
        self.rx_mask: Optional[PositiveInteger] = None
        self.tx_mask: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CanFrameTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanFrameTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize absolutely_can_frame_triggerings (list to container "ABSOLUTELY-CAN-FRAME-TRIGGERINGS")
        if self.absolutely_can_frame_triggerings:
            wrapper = ET.Element("ABSOLUTELY-CAN-FRAME-TRIGGERINGS")
            for item in self.absolutely_can_frame_triggerings:
                serialized = SerializationHelper.serialize_item(item, "TtcanAbsolutelyScheduledTiming")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_addressing_mode
        if self.can_addressing_mode is not None:
            serialized = SerializationHelper.serialize_item(self.can_addressing_mode, "CanAddressingModeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-ADDRESSING-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_frame_rx_behavior
        if self.can_frame_rx_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.can_frame_rx_behavior, "CanFrameRxBehaviorEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-FRAME-RX-BEHAVIOR")
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

        # Serialize can_xl_frame_triggering_props
        if self.can_xl_frame_triggering_props is not None:
            serialized = SerializationHelper.serialize_item(self.can_xl_frame_triggering_props, "CanXlFrameTriggeringProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-XL-FRAME-TRIGGERING-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identifier
        if self.identifier is not None:
            serialized = SerializationHelper.serialize_item(self.identifier, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize j1939requestable
        if self.j1939requestable is not None:
            serialized = SerializationHelper.serialize_item(self.j1939requestable, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("J1939REQUESTABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_identifier_range
        if self.rx_identifier_range is not None:
            serialized = SerializationHelper.serialize_item(self.rx_identifier_range, "RxIdentifierRange")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-IDENTIFIER-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_mask
        if self.rx_mask is not None:
            serialized = SerializationHelper.serialize_item(self.rx_mask, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tx_mask
        if self.tx_mask is not None:
            serialized = SerializationHelper.serialize_item(self.tx_mask, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TX-MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanFrameTriggering":
        """Deserialize XML element to CanFrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanFrameTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanFrameTriggering, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ABSOLUTELY-CAN-FRAME-TRIGGERINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.absolutely_can_frame_triggerings.append(SerializationHelper.deserialize_by_tag(item_elem, "TtcanAbsolutelyScheduledTiming"))
            elif tag == "CAN-ADDRESSING-MODE":
                setattr(obj, "can_addressing_mode", CanAddressingModeType.deserialize(child))
            elif tag == "CAN-FRAME-RX-BEHAVIOR":
                setattr(obj, "can_frame_rx_behavior", CanFrameRxBehaviorEnum.deserialize(child))
            elif tag == "CAN-FRAME-TX-BEHAVIOR":
                setattr(obj, "can_frame_tx_behavior", CanFrameTxBehaviorEnum.deserialize(child))
            elif tag == "CAN-XL-FRAME-TRIGGERING-PROPS":
                setattr(obj, "can_xl_frame_triggering_props", SerializationHelper.deserialize_by_tag(child, "CanXlFrameTriggeringProps"))
            elif tag == "IDENTIFIER":
                setattr(obj, "identifier", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "J1939REQUESTABLE":
                setattr(obj, "j1939requestable", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RX-IDENTIFIER-RANGE":
                setattr(obj, "rx_identifier_range", SerializationHelper.deserialize_by_tag(child, "RxIdentifierRange"))
            elif tag == "RX-MASK":
                setattr(obj, "rx_mask", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TX-MASK":
                setattr(obj, "tx_mask", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class CanFrameTriggeringBuilder(FrameTriggeringBuilder):
    """Builder for CanFrameTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanFrameTriggering = CanFrameTriggering()


    def with_absolutely_can_frame_triggerings(self, items: list[TtcanAbsolutelyScheduledTiming]) -> "CanFrameTriggeringBuilder":
        """Set absolutely_can_frame_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.absolutely_can_frame_triggerings = list(items) if items else []
        return self

    def with_can_addressing_mode(self, value: Optional[CanAddressingModeType]) -> "CanFrameTriggeringBuilder":
        """Set can_addressing_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_addressing_mode = value
        return self

    def with_can_frame_rx_behavior(self, value: Optional[CanFrameRxBehaviorEnum]) -> "CanFrameTriggeringBuilder":
        """Set can_frame_rx_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_frame_rx_behavior = value
        return self

    def with_can_frame_tx_behavior(self, value: Optional[CanFrameTxBehaviorEnum]) -> "CanFrameTriggeringBuilder":
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

    def with_can_xl_frame_triggering_props(self, value: Optional[CanXlFrameTriggeringProps]) -> "CanFrameTriggeringBuilder":
        """Set can_xl_frame_triggering_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_xl_frame_triggering_props = value
        return self

    def with_identifier(self, value: Optional[Integer]) -> "CanFrameTriggeringBuilder":
        """Set identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.identifier = value
        return self

    def with_j1939requestable(self, value: Optional[Boolean]) -> "CanFrameTriggeringBuilder":
        """Set j1939requestable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.j1939requestable = value
        return self

    def with_rx_identifier_range(self, value: Optional[RxIdentifierRange]) -> "CanFrameTriggeringBuilder":
        """Set rx_identifier_range attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rx_identifier_range = value
        return self

    def with_rx_mask(self, value: Optional[PositiveInteger]) -> "CanFrameTriggeringBuilder":
        """Set rx_mask attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rx_mask = value
        return self

    def with_tx_mask(self, value: Optional[PositiveInteger]) -> "CanFrameTriggeringBuilder":
        """Set tx_mask attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tx_mask = value
        return self


    def add_absolutely_can_frame_triggering(self, item: TtcanAbsolutelyScheduledTiming) -> "CanFrameTriggeringBuilder":
        """Add a single item to absolutely_can_frame_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.absolutely_can_frame_triggerings.append(item)
        return self

    def clear_absolutely_can_frame_triggerings(self) -> "CanFrameTriggeringBuilder":
        """Clear all items from absolutely_can_frame_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.absolutely_can_frame_triggerings = []
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


    def build(self) -> CanFrameTriggering:
        """Build and return the CanFrameTriggering instance with validation."""
        self._validate_instance()
        pass
        return self._obj