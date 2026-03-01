"""StateDependentFirewall AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 583)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.firewall_rule_props import (
    FirewallRuleProps,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class StateDependentFirewall(ARElement):
    """AUTOSAR StateDependentFirewall."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STATE-DEPENDENT-FIREWALL"


    default_action: Optional[FirewallActionEnum]
    firewall_rule_propses: list[FirewallRuleProps]
    firewall_state_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DEFAULT-ACTION": lambda obj, elem: setattr(obj, "default_action", SerializationHelper.deserialize_by_tag(elem, "FirewallActionEnum")),
        "FIREWALL-RULE-PROPSES": lambda obj, elem: obj.firewall_rule_propses.append(SerializationHelper.deserialize_by_tag(elem, "FirewallRuleProps")),
        "FIREWALL-STATE-REFS": lambda obj, elem: [obj.firewall_state_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize StateDependentFirewall."""
        super().__init__()
        self.default_action: Optional[FirewallActionEnum] = None
        self.firewall_rule_propses: list[FirewallRuleProps] = []
        self.firewall_state_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize StateDependentFirewall to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StateDependentFirewall, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_action
        if self.default_action is not None:
            serialized = SerializationHelper.serialize_item(self.default_action, "FirewallActionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-ACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize firewall_rule_propses (list to container "FIREWALL-RULE-PROPSES")
        if self.firewall_rule_propses:
            wrapper = ET.Element("FIREWALL-RULE-PROPSES")
            for item in self.firewall_rule_propses:
                serialized = SerializationHelper.serialize_item(item, "FirewallRuleProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize firewall_state_refs (list to container "FIREWALL-STATE-REFS")
        if self.firewall_state_refs:
            wrapper = ET.Element("FIREWALL-STATE-REFS")
            for item in self.firewall_state_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    child_elem = ET.Element("FIREWALL-STATE-REF")
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
    def deserialize(cls, element: ET.Element) -> "StateDependentFirewall":
        """Deserialize XML element to StateDependentFirewall object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StateDependentFirewall object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StateDependentFirewall, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEFAULT-ACTION":
                setattr(obj, "default_action", SerializationHelper.deserialize_by_tag(child, "FirewallActionEnum"))
            elif tag == "FIREWALL-RULE-PROPSES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.firewall_rule_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "FirewallRuleProps"))
            elif tag == "FIREWALL-STATE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.firewall_state_refs.append(ARRef.deserialize(item_elem))

        return obj



class StateDependentFirewallBuilder(ARElementBuilder):
    """Builder for StateDependentFirewall with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StateDependentFirewall = StateDependentFirewall()


    def with_default_action(self, value: Optional[FirewallActionEnum]) -> "StateDependentFirewallBuilder":
        """Set default_action attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_action = value
        return self

    def with_firewall_rule_propses(self, items: list[FirewallRuleProps]) -> "StateDependentFirewallBuilder":
        """Set firewall_rule_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.firewall_rule_propses = list(items) if items else []
        return self

    def with_firewall_states(self, items: list[ModeDeclaration]) -> "StateDependentFirewallBuilder":
        """Set firewall_states list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.firewall_states = list(items) if items else []
        return self


    def add_firewall_rule_props(self, item: FirewallRuleProps) -> "StateDependentFirewallBuilder":
        """Add a single item to firewall_rule_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.firewall_rule_propses.append(item)
        return self

    def clear_firewall_rule_propses(self) -> "StateDependentFirewallBuilder":
        """Clear all items from firewall_rule_propses list.

        Returns:
            self for method chaining
        """
        self._obj.firewall_rule_propses = []
        return self

    def add_firewall_state(self, item: ModeDeclaration) -> "StateDependentFirewallBuilder":
        """Add a single item to firewall_states list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.firewall_states.append(item)
        return self

    def clear_firewall_states(self) -> "StateDependentFirewallBuilder":
        """Clear all items from firewall_states list.

        Returns:
            self for method chaining
        """
        self._obj.firewall_states = []
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


    def build(self) -> StateDependentFirewall:
        """Build and return the StateDependentFirewall instance with validation."""
        self._validate_instance()
        pass
        return self._obj