"""EthernetWakeupSleepOnDatalineConfigSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthernetWakeupSleepOnDatalineConfigSet(FibexElement):
    """AUTOSAR EthernetWakeupSleepOnDatalineConfigSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG-SET"


    ethernets: list[Any]
    _DESERIALIZE_DISPATCH = {
        "ETHERNETS": lambda obj, elem: obj.ethernets.append(SerializationHelper.deserialize_by_tag(elem, "any (EthernetWakeupSleep)")),
    }


    def __init__(self) -> None:
        """Initialize EthernetWakeupSleepOnDatalineConfigSet."""
        super().__init__()
        self.ethernets: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EthernetWakeupSleepOnDatalineConfigSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetWakeupSleepOnDatalineConfigSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ethernets (list to container "ETHERNETS")
        if self.ethernets:
            wrapper = ET.Element("ETHERNETS")
            for item in self.ethernets:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetWakeupSleepOnDatalineConfigSet":
        """Deserialize XML element to EthernetWakeupSleepOnDatalineConfigSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetWakeupSleepOnDatalineConfigSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetWakeupSleepOnDatalineConfigSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ETHERNETS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ethernets.append(SerializationHelper.deserialize_by_tag(item_elem, "any (EthernetWakeupSleep)"))

        return obj



class EthernetWakeupSleepOnDatalineConfigSetBuilder(FibexElementBuilder):
    """Builder for EthernetWakeupSleepOnDatalineConfigSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthernetWakeupSleepOnDatalineConfigSet = EthernetWakeupSleepOnDatalineConfigSet()


    def with_ethernets(self, items: list[any (EthernetWakeupSleep)]) -> "EthernetWakeupSleepOnDatalineConfigSetBuilder":
        """Set ethernets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ethernets = list(items) if items else []
        return self


    def add_ethernet(self, item: any (EthernetWakeupSleep)) -> "EthernetWakeupSleepOnDatalineConfigSetBuilder":
        """Add a single item to ethernets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ethernets.append(item)
        return self

    def clear_ethernets(self) -> "EthernetWakeupSleepOnDatalineConfigSetBuilder":
        """Clear all items from ethernets list.

        Returns:
            self for method chaining
        """
        self._obj.ethernets = []
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


    def build(self) -> EthernetWakeupSleepOnDatalineConfigSet:
        """Build and return the EthernetWakeupSleepOnDatalineConfigSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj