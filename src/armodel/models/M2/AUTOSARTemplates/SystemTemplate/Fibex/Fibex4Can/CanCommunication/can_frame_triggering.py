"""CanFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameRxBehaviorEnum,
    CanFrameTxBehaviorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_xl_frame_triggering_props import (
    CanXlFrameTriggeringProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.rx_identifier_range import (
    RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication.ttcan_absolutely_scheduled_timing import (
    TtcanAbsolutelyScheduledTiming,
)


class CanFrameTriggering(FrameTriggering):
    """AUTOSAR CanFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _absolutelies: list[TtcanAbsolutelyScheduledTiming]
    can_addressing: Optional[CanAddressingModeType]
    can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum]
    can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum]
    can_xl_frame_ref: Optional[ARRef]
    identifier: Optional[Integer]
    j1939requestable: Optional[Boolean]
    rx_identifier_range_range: Optional[RxIdentifierRange]
    rx_mask: Optional[PositiveInteger]
    tx_mask: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanFrameTriggering."""
        super().__init__()
        self._absolutelies: list[TtcanAbsolutelyScheduledTiming] = []
        self.can_addressing: Optional[CanAddressingModeType] = None
        self.can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_xl_frame_ref: Optional[ARRef] = None
        self.identifier: Optional[Integer] = None
        self.j1939requestable: Optional[Boolean] = None
        self.rx_identifier_range_range: Optional[RxIdentifierRange] = None
        self.rx_mask: Optional[PositiveInteger] = None
        self.tx_mask: Optional[PositiveInteger] = None
    @property
    @xml_element_name("ABSOLUTELYS")
    def absolutelies(self) -> list[TtcanAbsolutelyScheduledTiming]:
        """Get absolutelies with custom XML element name."""
        return self._absolutelies

    @absolutelies.setter
    def absolutelies(self, value: list[TtcanAbsolutelyScheduledTiming]) -> None:
        """Set absolutelies with custom XML element name."""
        self._absolutelies = value


    def serialize(self) -> ET.Element:
        """Serialize CanFrameTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Serialize absolutelies (list to container "ABSOLUTELYS")
        if self.absolutelies:
            wrapper = ET.Element("ABSOLUTELYS")
            for item in self.absolutelies:
                serialized = SerializationHelper.serialize_item(item, "TtcanAbsolutelyScheduledTiming")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize can_xl_frame_ref
        if self.can_xl_frame_ref is not None:
            serialized = SerializationHelper.serialize_item(self.can_xl_frame_ref, "CanXlFrameTriggeringProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-XL-FRAME-REF")
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

        # Serialize rx_identifier_range_range
        if self.rx_identifier_range_range is not None:
            serialized = SerializationHelper.serialize_item(self.rx_identifier_range_range, "RxIdentifierRange")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-IDENTIFIER-RANGE-RANGE")
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

        # Parse absolutelies (list from container "ABSOLUTELYS")
        obj.absolutelies = []
        container = SerializationHelper.find_child_element(element, "ABSOLUTELYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.absolutelies.append(child_value)

        # Parse can_addressing
        child = SerializationHelper.find_child_element(element, "CAN-ADDRESSING")
        if child is not None:
            can_addressing_value = CanAddressingModeType.deserialize(child)
            obj.can_addressing = can_addressing_value

        # Parse can_frame_rx_behavior
        child = SerializationHelper.find_child_element(element, "CAN-FRAME-RX-BEHAVIOR")
        if child is not None:
            can_frame_rx_behavior_value = CanFrameRxBehaviorEnum.deserialize(child)
            obj.can_frame_rx_behavior = can_frame_rx_behavior_value

        # Parse can_frame_tx_behavior
        child = SerializationHelper.find_child_element(element, "CAN-FRAME-TX-BEHAVIOR")
        if child is not None:
            can_frame_tx_behavior_value = CanFrameTxBehaviorEnum.deserialize(child)
            obj.can_frame_tx_behavior = can_frame_tx_behavior_value

        # Parse can_xl_frame_ref
        child = SerializationHelper.find_child_element(element, "CAN-XL-FRAME-REF")
        if child is not None:
            can_xl_frame_ref_value = ARRef.deserialize(child)
            obj.can_xl_frame_ref = can_xl_frame_ref_value

        # Parse identifier
        child = SerializationHelper.find_child_element(element, "IDENTIFIER")
        if child is not None:
            identifier_value = child.text
            obj.identifier = identifier_value

        # Parse j1939requestable
        child = SerializationHelper.find_child_element(element, "J1939REQUESTABLE")
        if child is not None:
            j1939requestable_value = child.text
            obj.j1939requestable = j1939requestable_value

        # Parse rx_identifier_range_range
        child = SerializationHelper.find_child_element(element, "RX-IDENTIFIER-RANGE-RANGE")
        if child is not None:
            rx_identifier_range_range_value = SerializationHelper.deserialize_by_tag(child, "RxIdentifierRange")
            obj.rx_identifier_range_range = rx_identifier_range_range_value

        # Parse rx_mask
        child = SerializationHelper.find_child_element(element, "RX-MASK")
        if child is not None:
            rx_mask_value = child.text
            obj.rx_mask = rx_mask_value

        # Parse tx_mask
        child = SerializationHelper.find_child_element(element, "TX-MASK")
        if child is not None:
            tx_mask_value = child.text
            obj.tx_mask = tx_mask_value

        return obj



class CanFrameTriggeringBuilder:
    """Builder for CanFrameTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: CanFrameTriggering = CanFrameTriggering()


    def with_short_name(self, value: Identifier) -> "CanFrameTriggeringBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "CanFrameTriggeringBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "CanFrameTriggeringBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "CanFrameTriggeringBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "CanFrameTriggeringBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "CanFrameTriggeringBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "CanFrameTriggeringBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "CanFrameTriggeringBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "CanFrameTriggeringBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_frame(self, value: Optional[Frame]) -> "CanFrameTriggeringBuilder":
        """Set frame attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.frame = value
        return self

    def with_frame_ports(self, items: list[FramePort]) -> "CanFrameTriggeringBuilder":
        """Set frame_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.frame_ports = list(items) if items else []
        return self

    def with_pdu_triggerings(self, items: list[PduTriggering]) -> "CanFrameTriggeringBuilder":
        """Set pdu_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings = list(items) if items else []
        return self

    def with_absolutelies(self, items: list[TtcanAbsolutelyScheduledTiming]) -> "CanFrameTriggeringBuilder":
        """Set absolutelies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.absolutelies = list(items) if items else []
        return self

    def with_can_addressing(self, value: Optional[CanAddressingModeType]) -> "CanFrameTriggeringBuilder":
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

    def with_can_xl_frame(self, value: Optional[CanXlFrameTriggeringProps]) -> "CanFrameTriggeringBuilder":
        """Set can_xl_frame attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_xl_frame = value
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

    def with_rx_identifier_range_range(self, value: Optional[RxIdentifierRange]) -> "CanFrameTriggeringBuilder":
        """Set rx_identifier_range_range attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rx_identifier_range_range = value
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


    def add_short_name_fragment(self, item: ShortNameFragment) -> "CanFrameTriggeringBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "CanFrameTriggeringBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "CanFrameTriggeringBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "CanFrameTriggeringBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_frame_port(self, item: FramePort) -> "CanFrameTriggeringBuilder":
        """Add a single item to frame_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.frame_ports.append(item)
        return self

    def clear_frame_ports(self) -> "CanFrameTriggeringBuilder":
        """Clear all items from frame_ports list.

        Returns:
            self for method chaining
        """
        self._obj.frame_ports = []
        return self

    def add_pdu_triggering(self, item: PduTriggering) -> "CanFrameTriggeringBuilder":
        """Add a single item to pdu_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings.append(item)
        return self

    def clear_pdu_triggerings(self) -> "CanFrameTriggeringBuilder":
        """Clear all items from pdu_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings = []
        return self

    def add_absolutelie(self, item: TtcanAbsolutelyScheduledTiming) -> "CanFrameTriggeringBuilder":
        """Add a single item to absolutelies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.absolutelies.append(item)
        return self

    def clear_absolutelies(self) -> "CanFrameTriggeringBuilder":
        """Clear all items from absolutelies list.

        Returns:
            self for method chaining
        """
        self._obj.absolutelies = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> CanFrameTriggering:
        """Build and return the CanFrameTriggering instance with validation."""
        self._validate_instance()
        pass
        return self._obj