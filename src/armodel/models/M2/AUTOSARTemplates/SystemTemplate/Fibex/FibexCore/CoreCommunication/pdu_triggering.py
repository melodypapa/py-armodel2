"""PduTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 303)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 348)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_port import (
    IPduPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.sec_oc_crypto_service_mapping import (
    SecOcCryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.trigger_i_pdu_send_condition import (
    TriggerIPduSendCondition,
)


class PduTriggering(Identifiable):
    """AUTOSAR PduTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_ref: Optional[ARRef]
    i_pdu_port_refs: list[ARRef]
    i_signal_refs: list[ARRef]
    sec_oc_crypto_service_ref: Optional[ARRef]
    trigger_i_pdu_send_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PduTriggering."""
        super().__init__()
        self.i_pdu_ref: Optional[ARRef] = None
        self.i_pdu_port_refs: list[ARRef] = []
        self.i_signal_refs: list[ARRef] = []
        self.sec_oc_crypto_service_ref: Optional[ARRef] = None
        self.trigger_i_pdu_send_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PduTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PduTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_ref
        if self.i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_pdu_ref, "Pdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_pdu_port_refs (list to container "I-PDU-PORT-REFS")
        if self.i_pdu_port_refs:
            wrapper = ET.Element("I-PDU-PORT-REFS")
            for item in self.i_pdu_port_refs:
                serialized = SerializationHelper.serialize_item(item, "IPduPort")
                if serialized is not None:
                    child_elem = ET.Element("I-PDU-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_signal_refs (list to container "I-SIGNAL-REFS")
        if self.i_signal_refs:
            wrapper = ET.Element("I-SIGNAL-REFS")
            for item in self.i_signal_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalTriggering")
                if serialized is not None:
                    child_elem = ET.Element("I-SIGNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sec_oc_crypto_service_ref
        if self.sec_oc_crypto_service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sec_oc_crypto_service_ref, "SecOcCryptoServiceMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEC-OC-CRYPTO-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_i_pdu_send_refs (list to container "TRIGGER-I-PDU-SEND-REFS")
        if self.trigger_i_pdu_send_refs:
            wrapper = ET.Element("TRIGGER-I-PDU-SEND-REFS")
            for item in self.trigger_i_pdu_send_refs:
                serialized = SerializationHelper.serialize_item(item, "TriggerIPduSendCondition")
                if serialized is not None:
                    child_elem = ET.Element("TRIGGER-I-PDU-SEND-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduTriggering":
        """Deserialize XML element to PduTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PduTriggering, cls).deserialize(element)

        # Parse i_pdu_ref
        child = SerializationHelper.find_child_element(element, "I-PDU-REF")
        if child is not None:
            i_pdu_ref_value = ARRef.deserialize(child)
            obj.i_pdu_ref = i_pdu_ref_value

        # Parse i_pdu_port_refs (list from container "I-PDU-PORT-REFS")
        obj.i_pdu_port_refs = []
        container = SerializationHelper.find_child_element(element, "I-PDU-PORT-REFS")
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
                    obj.i_pdu_port_refs.append(child_value)

        # Parse i_signal_refs (list from container "I-SIGNAL-REFS")
        obj.i_signal_refs = []
        container = SerializationHelper.find_child_element(element, "I-SIGNAL-REFS")
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
                    obj.i_signal_refs.append(child_value)

        # Parse sec_oc_crypto_service_ref
        child = SerializationHelper.find_child_element(element, "SEC-OC-CRYPTO-SERVICE-REF")
        if child is not None:
            sec_oc_crypto_service_ref_value = ARRef.deserialize(child)
            obj.sec_oc_crypto_service_ref = sec_oc_crypto_service_ref_value

        # Parse trigger_i_pdu_send_refs (list from container "TRIGGER-I-PDU-SEND-REFS")
        obj.trigger_i_pdu_send_refs = []
        container = SerializationHelper.find_child_element(element, "TRIGGER-I-PDU-SEND-REFS")
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
                    obj.trigger_i_pdu_send_refs.append(child_value)

        return obj



class PduTriggeringBuilder:
    """Builder for PduTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: PduTriggering = PduTriggering()


    def with_short_name(self, value: Identifier) -> "PduTriggeringBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "PduTriggeringBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "PduTriggeringBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "PduTriggeringBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "PduTriggeringBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "PduTriggeringBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "PduTriggeringBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "PduTriggeringBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "PduTriggeringBuilder":
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

    def with_i_pdu(self, value: Optional[Pdu]) -> "PduTriggeringBuilder":
        """Set i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_pdu = value
        return self

    def with_i_pdu_ports(self, items: list[IPduPort]) -> "PduTriggeringBuilder":
        """Set i_pdu_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_ports = list(items) if items else []
        return self

    def with_i_signals(self, items: list[ISignalTriggering]) -> "PduTriggeringBuilder":
        """Set i_signals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_signals = list(items) if items else []
        return self

    def with_sec_oc_crypto_service(self, value: Optional[SecOcCryptoServiceMapping]) -> "PduTriggeringBuilder":
        """Set sec_oc_crypto_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sec_oc_crypto_service = value
        return self

    def with_trigger_i_pdu_sends(self, items: list[TriggerIPduSendCondition]) -> "PduTriggeringBuilder":
        """Set trigger_i_pdu_sends list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_i_pdu_sends = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "PduTriggeringBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "PduTriggeringBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "PduTriggeringBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "PduTriggeringBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_i_pdu_port(self, item: IPduPort) -> "PduTriggeringBuilder":
        """Add a single item to i_pdu_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_ports.append(item)
        return self

    def clear_i_pdu_ports(self) -> "PduTriggeringBuilder":
        """Clear all items from i_pdu_ports list.

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_ports = []
        return self

    def add_i_signal(self, item: ISignalTriggering) -> "PduTriggeringBuilder":
        """Add a single item to i_signals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_signals.append(item)
        return self

    def clear_i_signals(self) -> "PduTriggeringBuilder":
        """Clear all items from i_signals list.

        Returns:
            self for method chaining
        """
        self._obj.i_signals = []
        return self

    def add_trigger_i_pdu_send(self, item: TriggerIPduSendCondition) -> "PduTriggeringBuilder":
        """Add a single item to trigger_i_pdu_sends list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_i_pdu_sends.append(item)
        return self

    def clear_trigger_i_pdu_sends(self) -> "PduTriggeringBuilder":
        """Clear all items from trigger_i_pdu_sends list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_i_pdu_sends = []
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


    def build(self) -> PduTriggering:
        """Build and return the PduTriggering instance with validation."""
        self._validate_instance()
        pass
        return self._obj