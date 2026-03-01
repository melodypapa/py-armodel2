"""IPSecConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 571)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_config_props import (
    IPSecConfigProps,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_rule import (
        IPSecRule,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class IPSecConfig(ARObject):
    """AUTOSAR IPSecConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-P-SEC-CONFIG"


    ip_sec_config_ref: Optional[ARRef]
    ip_sec_rules: list[IPSecRule]
    _DESERIALIZE_DISPATCH = {
        "IP-SEC-CONFIG-REF": lambda obj, elem: setattr(obj, "ip_sec_config_ref", ARRef.deserialize(elem)),
        "IP-SEC-RULES": lambda obj, elem: obj.ip_sec_rules.append(SerializationHelper.deserialize_by_tag(elem, "IPSecRule")),
    }


    def __init__(self) -> None:
        """Initialize IPSecConfig."""
        super().__init__()
        self.ip_sec_config_ref: Optional[ARRef] = None
        self.ip_sec_rules: list[IPSecRule] = []

    def serialize(self) -> ET.Element:
        """Serialize IPSecConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPSecConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ip_sec_config_ref
        if self.ip_sec_config_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ip_sec_config_ref, "IPSecConfigProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-SEC-CONFIG-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_sec_rules (list to container "IP-SEC-RULES")
        if self.ip_sec_rules:
            wrapper = ET.Element("IP-SEC-RULES")
            for item in self.ip_sec_rules:
                serialized = SerializationHelper.serialize_item(item, "IPSecRule")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecConfig":
        """Deserialize XML element to IPSecConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPSecConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPSecConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "IP-SEC-CONFIG-REF":
                setattr(obj, "ip_sec_config_ref", ARRef.deserialize(child))
            elif tag == "IP-SEC-RULES":
                obj.ip_sec_rules.append(SerializationHelper.deserialize_by_tag(child, "IPSecRule"))

        return obj



class IPSecConfigBuilder(BuilderBase):
    """Builder for IPSecConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPSecConfig = IPSecConfig()


    def with_ip_sec_config(self, value: Optional[IPSecConfigProps]) -> "IPSecConfigBuilder":
        """Set ip_sec_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ip_sec_config = value
        return self

    def with_ip_sec_rules(self, items: list[IPSecRule]) -> "IPSecConfigBuilder":
        """Set ip_sec_rules list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ip_sec_rules = list(items) if items else []
        return self


    def add_ip_sec_rule(self, item: IPSecRule) -> "IPSecConfigBuilder":
        """Add a single item to ip_sec_rules list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ip_sec_rules.append(item)
        return self

    def clear_ip_sec_rules(self) -> "IPSecConfigBuilder":
        """Clear all items from ip_sec_rules list.

        Returns:
            self for method chaining
        """
        self._obj.ip_sec_rules = []
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


    def build(self) -> IPSecConfig:
        """Build and return the IPSecConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj