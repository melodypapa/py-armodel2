"""IPSecConfigProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 572)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    IPsecDpdActionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IPSecConfigProps(ARElement):
    """AUTOSAR IPSecConfigProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-P-SEC-CONFIG-PROPS"


    ah_cipher_suites: list[String]
    dpd_action: Optional[IPsecDpdActionEnum]
    dpd_delay: Optional[TimeValue]
    esp_cipher_suites: list[String]
    ike_cipher_suite: Optional[String]
    ike_over_time: Optional[TimeValue]
    ike_rand_time: Optional[PositiveInteger]
    ike_reauth_time: Optional[TimeValue]
    ike_rekey_time: Optional[TimeValue]
    sa_over_time: Optional[PositiveInteger]
    sa_rand_time: Optional[TimeValue]
    sa_rekey_time: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "AH-CIPHER-SUITES": lambda obj, elem: obj.ah_cipher_suites.append(SerializationHelper.deserialize_by_tag(elem, "String")),
        "DPD-ACTION": lambda obj, elem: setattr(obj, "dpd_action", IPsecDpdActionEnum.deserialize(elem)),
        "DPD-DELAY": lambda obj, elem: setattr(obj, "dpd_delay", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "ESP-CIPHER-SUITES": lambda obj, elem: obj.esp_cipher_suites.append(SerializationHelper.deserialize_by_tag(elem, "String")),
        "IKE-CIPHER-SUITE": lambda obj, elem: setattr(obj, "ike_cipher_suite", SerializationHelper.deserialize_by_tag(elem, "String")),
        "IKE-OVER-TIME": lambda obj, elem: setattr(obj, "ike_over_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "IKE-RAND-TIME": lambda obj, elem: setattr(obj, "ike_rand_time", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IKE-REAUTH-TIME": lambda obj, elem: setattr(obj, "ike_reauth_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "IKE-REKEY-TIME": lambda obj, elem: setattr(obj, "ike_rekey_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "SA-OVER-TIME": lambda obj, elem: setattr(obj, "sa_over_time", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SA-RAND-TIME": lambda obj, elem: setattr(obj, "sa_rand_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "SA-REKEY-TIME": lambda obj, elem: setattr(obj, "sa_rekey_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize IPSecConfigProps."""
        super().__init__()
        self.ah_cipher_suites: list[String] = []
        self.dpd_action: Optional[IPsecDpdActionEnum] = None
        self.dpd_delay: Optional[TimeValue] = None
        self.esp_cipher_suites: list[String] = []
        self.ike_cipher_suite: Optional[String] = None
        self.ike_over_time: Optional[TimeValue] = None
        self.ike_rand_time: Optional[PositiveInteger] = None
        self.ike_reauth_time: Optional[TimeValue] = None
        self.ike_rekey_time: Optional[TimeValue] = None
        self.sa_over_time: Optional[PositiveInteger] = None
        self.sa_rand_time: Optional[TimeValue] = None
        self.sa_rekey_time: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize IPSecConfigProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPSecConfigProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ah_cipher_suites (list to container "AH-CIPHER-SUITES")
        if self.ah_cipher_suites:
            wrapper = ET.Element("AH-CIPHER-SUITES")
            for item in self.ah_cipher_suites:
                serialized = SerializationHelper.serialize_item(item, "String")
                if serialized is not None:
                    child_elem = ET.Element("AH-CIPHER-SUITE")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dpd_action
        if self.dpd_action is not None:
            serialized = SerializationHelper.serialize_item(self.dpd_action, "IPsecDpdActionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DPD-ACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dpd_delay
        if self.dpd_delay is not None:
            serialized = SerializationHelper.serialize_item(self.dpd_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DPD-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize esp_cipher_suites (list to container "ESP-CIPHER-SUITES")
        if self.esp_cipher_suites:
            wrapper = ET.Element("ESP-CIPHER-SUITES")
            for item in self.esp_cipher_suites:
                serialized = SerializationHelper.serialize_item(item, "String")
                if serialized is not None:
                    child_elem = ET.Element("ESP-CIPHER-SUITE")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ike_cipher_suite
        if self.ike_cipher_suite is not None:
            serialized = SerializationHelper.serialize_item(self.ike_cipher_suite, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-CIPHER-SUITE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ike_over_time
        if self.ike_over_time is not None:
            serialized = SerializationHelper.serialize_item(self.ike_over_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-OVER-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ike_rand_time
        if self.ike_rand_time is not None:
            serialized = SerializationHelper.serialize_item(self.ike_rand_time, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-RAND-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ike_reauth_time
        if self.ike_reauth_time is not None:
            serialized = SerializationHelper.serialize_item(self.ike_reauth_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-REAUTH-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ike_rekey_time
        if self.ike_rekey_time is not None:
            serialized = SerializationHelper.serialize_item(self.ike_rekey_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-REKEY-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sa_over_time
        if self.sa_over_time is not None:
            serialized = SerializationHelper.serialize_item(self.sa_over_time, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SA-OVER-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sa_rand_time
        if self.sa_rand_time is not None:
            serialized = SerializationHelper.serialize_item(self.sa_rand_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SA-RAND-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sa_rekey_time
        if self.sa_rekey_time is not None:
            serialized = SerializationHelper.serialize_item(self.sa_rekey_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SA-REKEY-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecConfigProps":
        """Deserialize XML element to IPSecConfigProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPSecConfigProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPSecConfigProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "AH-CIPHER-SUITES":
                obj.ah_cipher_suites.append(SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "DPD-ACTION":
                setattr(obj, "dpd_action", IPsecDpdActionEnum.deserialize(child))
            elif tag == "DPD-DELAY":
                setattr(obj, "dpd_delay", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "ESP-CIPHER-SUITES":
                obj.esp_cipher_suites.append(SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "IKE-CIPHER-SUITE":
                setattr(obj, "ike_cipher_suite", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "IKE-OVER-TIME":
                setattr(obj, "ike_over_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "IKE-RAND-TIME":
                setattr(obj, "ike_rand_time", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IKE-REAUTH-TIME":
                setattr(obj, "ike_reauth_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "IKE-REKEY-TIME":
                setattr(obj, "ike_rekey_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "SA-OVER-TIME":
                setattr(obj, "sa_over_time", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SA-RAND-TIME":
                setattr(obj, "sa_rand_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "SA-REKEY-TIME":
                setattr(obj, "sa_rekey_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class IPSecConfigPropsBuilder(ARElementBuilder):
    """Builder for IPSecConfigProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPSecConfigProps = IPSecConfigProps()


    def with_ah_cipher_suites(self, items: list[String]) -> "IPSecConfigPropsBuilder":
        """Set ah_cipher_suites list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ah_cipher_suites = list(items) if items else []
        return self

    def with_dpd_action(self, value: Optional[IPsecDpdActionEnum]) -> "IPSecConfigPropsBuilder":
        """Set dpd_action attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dpd_action = value
        return self

    def with_dpd_delay(self, value: Optional[TimeValue]) -> "IPSecConfigPropsBuilder":
        """Set dpd_delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dpd_delay = value
        return self

    def with_esp_cipher_suites(self, items: list[String]) -> "IPSecConfigPropsBuilder":
        """Set esp_cipher_suites list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.esp_cipher_suites = list(items) if items else []
        return self

    def with_ike_cipher_suite(self, value: Optional[String]) -> "IPSecConfigPropsBuilder":
        """Set ike_cipher_suite attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ike_cipher_suite = value
        return self

    def with_ike_over_time(self, value: Optional[TimeValue]) -> "IPSecConfigPropsBuilder":
        """Set ike_over_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ike_over_time = value
        return self

    def with_ike_rand_time(self, value: Optional[PositiveInteger]) -> "IPSecConfigPropsBuilder":
        """Set ike_rand_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ike_rand_time = value
        return self

    def with_ike_reauth_time(self, value: Optional[TimeValue]) -> "IPSecConfigPropsBuilder":
        """Set ike_reauth_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ike_reauth_time = value
        return self

    def with_ike_rekey_time(self, value: Optional[TimeValue]) -> "IPSecConfigPropsBuilder":
        """Set ike_rekey_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ike_rekey_time = value
        return self

    def with_sa_over_time(self, value: Optional[PositiveInteger]) -> "IPSecConfigPropsBuilder":
        """Set sa_over_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sa_over_time = value
        return self

    def with_sa_rand_time(self, value: Optional[TimeValue]) -> "IPSecConfigPropsBuilder":
        """Set sa_rand_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sa_rand_time = value
        return self

    def with_sa_rekey_time(self, value: Optional[TimeValue]) -> "IPSecConfigPropsBuilder":
        """Set sa_rekey_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sa_rekey_time = value
        return self


    def add_ah_cipher_suite(self, item: String) -> "IPSecConfigPropsBuilder":
        """Add a single item to ah_cipher_suites list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ah_cipher_suites.append(item)
        return self

    def clear_ah_cipher_suites(self) -> "IPSecConfigPropsBuilder":
        """Clear all items from ah_cipher_suites list.

        Returns:
            self for method chaining
        """
        self._obj.ah_cipher_suites = []
        return self

    def add_esp_cipher_suite(self, item: String) -> "IPSecConfigPropsBuilder":
        """Add a single item to esp_cipher_suites list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.esp_cipher_suites.append(item)
        return self

    def clear_esp_cipher_suites(self) -> "IPSecConfigPropsBuilder":
        """Clear all items from esp_cipher_suites list.

        Returns:
            self for method chaining
        """
        self._obj.esp_cipher_suites = []
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


    def build(self) -> IPSecConfigProps:
        """Build and return the IPSecConfigProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj