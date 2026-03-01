"""ContainerIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 353)

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
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainerIPduHeaderTypeEnum,
    ContainerIPduTriggerEnum,
    RxAcceptContainedIPduEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ContainerIPdu(IPdu):
    """AUTOSAR ContainerIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONTAINER-I-PDU"


    contained_i_pdu_propses: list[ContainedIPduProps]
    contained_pdu_refs: list[ARRef]
    container: Optional[TimeValue]
    container_trigger_ref: Optional[ContainerIPduTriggerEnum]
    header_type: Optional[ContainerIPduHeaderTypeEnum]
    minimum_rx: Optional[PositiveInteger]
    minimum_tx: Optional[PositiveInteger]
    rx_accept: Optional[RxAcceptContainedIPduEnum]
    threshold_size: Optional[PositiveInteger]
    unused_bit: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CONTAINED-I-PDU-PROPSES": lambda obj, elem: obj.contained_i_pdu_propses.append(SerializationHelper.deserialize_by_tag(elem, "ContainedIPduProps")),
        "CONTAINED-PDUS": lambda obj, elem: obj.contained_pdu_refs.append(ARRef.deserialize(elem)),
        "CONTAINER": lambda obj, elem: setattr(obj, "container", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "CONTAINER-TRIGGER-REF": lambda obj, elem: setattr(obj, "container_trigger_ref", ContainerIPduTriggerEnum.deserialize(elem)),
        "HEADER-TYPE": lambda obj, elem: setattr(obj, "header_type", ContainerIPduHeaderTypeEnum.deserialize(elem)),
        "MINIMUM-RX": lambda obj, elem: setattr(obj, "minimum_rx", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MINIMUM-TX": lambda obj, elem: setattr(obj, "minimum_tx", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RX-ACCEPT": lambda obj, elem: setattr(obj, "rx_accept", RxAcceptContainedIPduEnum.deserialize(elem)),
        "THRESHOLD-SIZE": lambda obj, elem: setattr(obj, "threshold_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "UNUSED-BIT": lambda obj, elem: setattr(obj, "unused_bit", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize ContainerIPdu."""
        super().__init__()
        self.contained_i_pdu_propses: list[ContainedIPduProps] = []
        self.contained_pdu_refs: list[ARRef] = []
        self.container: Optional[TimeValue] = None
        self.container_trigger_ref: Optional[ContainerIPduTriggerEnum] = None
        self.header_type: Optional[ContainerIPduHeaderTypeEnum] = None
        self.minimum_rx: Optional[PositiveInteger] = None
        self.minimum_tx: Optional[PositiveInteger] = None
        self.rx_accept: Optional[RxAcceptContainedIPduEnum] = None
        self.threshold_size: Optional[PositiveInteger] = None
        self.unused_bit: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ContainerIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ContainerIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize contained_i_pdu_propses (list to container "CONTAINED-I-PDU-PROPSES")
        if self.contained_i_pdu_propses:
            wrapper = ET.Element("CONTAINED-I-PDU-PROPSES")
            for item in self.contained_i_pdu_propses:
                serialized = SerializationHelper.serialize_item(item, "ContainedIPduProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize contained_pdu_refs (list to container "CONTAINED-PDU-REFS")
        if self.contained_pdu_refs:
            wrapper = ET.Element("CONTAINED-PDU-REFS")
            for item in self.contained_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("CONTAINED-PDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize container
        if self.container is not None:
            serialized = SerializationHelper.serialize_item(self.container, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize container_trigger_ref
        if self.container_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.container_trigger_ref, "ContainerIPduTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINER-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize header_type
        if self.header_type is not None:
            serialized = SerializationHelper.serialize_item(self.header_type, "ContainerIPduHeaderTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_rx
        if self.minimum_rx is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_rx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-RX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_tx
        if self.minimum_tx is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_tx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_accept
        if self.rx_accept is not None:
            serialized = SerializationHelper.serialize_item(self.rx_accept, "RxAcceptContainedIPduEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-ACCEPT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize threshold_size
        if self.threshold_size is not None:
            serialized = SerializationHelper.serialize_item(self.threshold_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("THRESHOLD-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unused_bit
        if self.unused_bit is not None:
            serialized = SerializationHelper.serialize_item(self.unused_bit, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNUSED-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ContainerIPdu":
        """Deserialize XML element to ContainerIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ContainerIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ContainerIPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTAINED-I-PDU-PROPSES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.contained_i_pdu_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "ContainedIPduProps"))
            elif tag == "CONTAINED-PDUS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.contained_pdu_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "PduTriggering"))
            elif tag == "CONTAINER":
                setattr(obj, "container", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "CONTAINER-TRIGGER-REF":
                setattr(obj, "container_trigger_ref", ContainerIPduTriggerEnum.deserialize(child))
            elif tag == "HEADER-TYPE":
                setattr(obj, "header_type", ContainerIPduHeaderTypeEnum.deserialize(child))
            elif tag == "MINIMUM-RX":
                setattr(obj, "minimum_rx", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MINIMUM-TX":
                setattr(obj, "minimum_tx", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RX-ACCEPT":
                setattr(obj, "rx_accept", RxAcceptContainedIPduEnum.deserialize(child))
            elif tag == "THRESHOLD-SIZE":
                setattr(obj, "threshold_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "UNUSED-BIT":
                setattr(obj, "unused_bit", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class ContainerIPduBuilder(IPduBuilder):
    """Builder for ContainerIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ContainerIPdu = ContainerIPdu()


    def with_contained_i_pdu_propses(self, items: list[ContainedIPduProps]) -> "ContainerIPduBuilder":
        """Set contained_i_pdu_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.contained_i_pdu_propses = list(items) if items else []
        return self

    def with_contained_pdus(self, items: list[PduTriggering]) -> "ContainerIPduBuilder":
        """Set contained_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.contained_pdus = list(items) if items else []
        return self

    def with_container(self, value: Optional[TimeValue]) -> "ContainerIPduBuilder":
        """Set container attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.container = value
        return self

    def with_container_trigger(self, value: Optional[ContainerIPduTriggerEnum]) -> "ContainerIPduBuilder":
        """Set container_trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.container_trigger = value
        return self

    def with_header_type(self, value: Optional[ContainerIPduHeaderTypeEnum]) -> "ContainerIPduBuilder":
        """Set header_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.header_type = value
        return self

    def with_minimum_rx(self, value: Optional[PositiveInteger]) -> "ContainerIPduBuilder":
        """Set minimum_rx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum_rx = value
        return self

    def with_minimum_tx(self, value: Optional[PositiveInteger]) -> "ContainerIPduBuilder":
        """Set minimum_tx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum_tx = value
        return self

    def with_rx_accept(self, value: Optional[RxAcceptContainedIPduEnum]) -> "ContainerIPduBuilder":
        """Set rx_accept attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rx_accept = value
        return self

    def with_threshold_size(self, value: Optional[PositiveInteger]) -> "ContainerIPduBuilder":
        """Set threshold_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.threshold_size = value
        return self

    def with_unused_bit(self, value: Optional[PositiveInteger]) -> "ContainerIPduBuilder":
        """Set unused_bit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unused_bit = value
        return self


    def add_contained_i_pdu_props(self, item: ContainedIPduProps) -> "ContainerIPduBuilder":
        """Add a single item to contained_i_pdu_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.contained_i_pdu_propses.append(item)
        return self

    def clear_contained_i_pdu_propses(self) -> "ContainerIPduBuilder":
        """Clear all items from contained_i_pdu_propses list.

        Returns:
            self for method chaining
        """
        self._obj.contained_i_pdu_propses = []
        return self

    def add_contained_pdu(self, item: PduTriggering) -> "ContainerIPduBuilder":
        """Add a single item to contained_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.contained_pdus.append(item)
        return self

    def clear_contained_pdus(self) -> "ContainerIPduBuilder":
        """Clear all items from contained_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.contained_pdus = []
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


    def build(self) -> ContainerIPdu:
        """Build and return the ContainerIPdu instance with validation."""
        self._validate_instance()
        pass
        return self._obj