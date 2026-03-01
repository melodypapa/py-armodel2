"""DdsCpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 525)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_domain import (
    DdsCpDomain,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsCpConfig(ARElement):
    """AUTOSAR DdsCpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-CP-CONFIG"


    dds_domains: list[DdsCpDomain]
    dds_qos_profiles: list[DdsCpQosProfile]
    _DESERIALIZE_DISPATCH = {
        "DDS-DOMAINS": lambda obj, elem: obj.dds_domains.append(SerializationHelper.deserialize_by_tag(elem, "DdsCpDomain")),
        "DDS-QOS-PROFILES": lambda obj, elem: obj.dds_qos_profiles.append(SerializationHelper.deserialize_by_tag(elem, "DdsCpQosProfile")),
    }


    def __init__(self) -> None:
        """Initialize DdsCpConfig."""
        super().__init__()
        self.dds_domains: list[DdsCpDomain] = []
        self.dds_qos_profiles: list[DdsCpQosProfile] = []

    def serialize(self) -> ET.Element:
        """Serialize DdsCpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_domains (list to container "DDS-DOMAINS")
        if self.dds_domains:
            wrapper = ET.Element("DDS-DOMAINS")
            for item in self.dds_domains:
                serialized = SerializationHelper.serialize_item(item, "DdsCpDomain")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dds_qos_profiles (list to container "DDS-QOS-PROFILES")
        if self.dds_qos_profiles:
            wrapper = ET.Element("DDS-QOS-PROFILES")
            for item in self.dds_qos_profiles:
                serialized = SerializationHelper.serialize_item(item, "DdsCpQosProfile")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpConfig":
        """Deserialize XML element to DdsCpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DDS-DOMAINS":
                obj.dds_domains.append(SerializationHelper.deserialize_by_tag(child, "DdsCpDomain"))
            elif tag == "DDS-QOS-PROFILES":
                obj.dds_qos_profiles.append(SerializationHelper.deserialize_by_tag(child, "DdsCpQosProfile"))

        return obj



class DdsCpConfigBuilder(ARElementBuilder):
    """Builder for DdsCpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpConfig = DdsCpConfig()


    def with_dds_domains(self, items: list[DdsCpDomain]) -> "DdsCpConfigBuilder":
        """Set dds_domains list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dds_domains = list(items) if items else []
        return self

    def with_dds_qos_profiles(self, items: list[DdsCpQosProfile]) -> "DdsCpConfigBuilder":
        """Set dds_qos_profiles list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dds_qos_profiles = list(items) if items else []
        return self


    def add_dds_domain(self, item: DdsCpDomain) -> "DdsCpConfigBuilder":
        """Add a single item to dds_domains list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dds_domains.append(item)
        return self

    def clear_dds_domains(self) -> "DdsCpConfigBuilder":
        """Clear all items from dds_domains list.

        Returns:
            self for method chaining
        """
        self._obj.dds_domains = []
        return self

    def add_dds_qos_profile(self, item: DdsCpQosProfile) -> "DdsCpConfigBuilder":
        """Add a single item to dds_qos_profiles list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dds_qos_profiles.append(item)
        return self

    def clear_dds_qos_profiles(self) -> "DdsCpConfigBuilder":
        """Clear all items from dds_qos_profiles list.

        Returns:
            self for method chaining
        """
        self._obj.dds_qos_profiles = []
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


    def build(self) -> DdsCpConfig:
        """Build and return the DdsCpConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj