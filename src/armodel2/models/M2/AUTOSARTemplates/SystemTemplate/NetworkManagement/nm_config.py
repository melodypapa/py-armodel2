"""NmConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 672)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
    NmEcu,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class NmConfig(FibexElement):
    """AUTOSAR NmConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NM-CONFIG"


    nm_clusters: list[NmCluster]
    nm_cluster_couplings: list[NmClusterCoupling]
    nm_if_ecus: list[NmEcu]
    _DESERIALIZE_DISPATCH = {
        "NM-CLUSTERS": ("_POLYMORPHIC_LIST", "nm_clusters", ["CanNmCluster", "FlexrayNmCluster", "J1939NmCluster", "UdpNmCluster"]),
        "NM-CLUSTER-COUPLINGS": ("_POLYMORPHIC_LIST", "nm_cluster_couplings", ["CanNmClusterCoupling", "FlexrayNmClusterCoupling", "UdpNmClusterCoupling"]),
        "NM-IF-ECUS": lambda obj, elem: obj.nm_if_ecus.append(SerializationHelper.deserialize_by_tag(elem, "NmEcu")),
    }


    def __init__(self) -> None:
        """Initialize NmConfig."""
        super().__init__()
        self.nm_clusters: list[NmCluster] = []
        self.nm_cluster_couplings: list[NmClusterCoupling] = []
        self.nm_if_ecus: list[NmEcu] = []

    def serialize(self) -> ET.Element:
        """Serialize NmConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_clusters (list to container "NM-CLUSTERS")
        if self.nm_clusters:
            wrapper = ET.Element("NM-CLUSTERS")
            for item in self.nm_clusters:
                serialized = SerializationHelper.serialize_item(item, "NmCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_cluster_couplings (list to container "NM-CLUSTER-COUPLINGS")
        if self.nm_cluster_couplings:
            wrapper = ET.Element("NM-CLUSTER-COUPLINGS")
            for item in self.nm_cluster_couplings:
                serialized = SerializationHelper.serialize_item(item, "NmClusterCoupling")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_if_ecus (list to container "NM-IF-ECUS")
        if self.nm_if_ecus:
            wrapper = ET.Element("NM-IF-ECUS")
            for item in self.nm_if_ecus:
                serialized = SerializationHelper.serialize_item(item, "NmEcu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmConfig":
        """Deserialize XML element to NmConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "NM-CLUSTERS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CAN-NM-CLUSTER":
                        obj.nm_clusters.append(SerializationHelper.deserialize_by_tag(child[0], "CanNmCluster"))
                    elif concrete_tag == "FLEXRAY-NM-CLUSTER":
                        obj.nm_clusters.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayNmCluster"))
                    elif concrete_tag == "J1939-NM-CLUSTER":
                        obj.nm_clusters.append(SerializationHelper.deserialize_by_tag(child[0], "J1939NmCluster"))
                    elif concrete_tag == "UDP-NM-CLUSTER":
                        obj.nm_clusters.append(SerializationHelper.deserialize_by_tag(child[0], "UdpNmCluster"))
            elif tag == "NM-CLUSTER-COUPLINGS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CAN-NM-CLUSTER-COUPLING":
                        obj.nm_cluster_couplings.append(SerializationHelper.deserialize_by_tag(child[0], "CanNmClusterCoupling"))
                    elif concrete_tag == "FLEXRAY-NM-CLUSTER-COUPLING":
                        obj.nm_cluster_couplings.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayNmClusterCoupling"))
                    elif concrete_tag == "UDP-NM-CLUSTER-COUPLING":
                        obj.nm_cluster_couplings.append(SerializationHelper.deserialize_by_tag(child[0], "UdpNmClusterCoupling"))
            elif tag == "NM-IF-ECUS":
                obj.nm_if_ecus.append(SerializationHelper.deserialize_by_tag(child, "NmEcu"))

        return obj



class NmConfigBuilder(FibexElementBuilder):
    """Builder for NmConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NmConfig = NmConfig()


    def with_nm_clusters(self, items: list[NmCluster]) -> "NmConfigBuilder":
        """Set nm_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nm_clusters = list(items) if items else []
        return self

    def with_nm_cluster_couplings(self, items: list[NmClusterCoupling]) -> "NmConfigBuilder":
        """Set nm_cluster_couplings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nm_cluster_couplings = list(items) if items else []
        return self

    def with_nm_if_ecus(self, items: list[NmEcu]) -> "NmConfigBuilder":
        """Set nm_if_ecus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nm_if_ecus = list(items) if items else []
        return self


    def add_nm_cluster(self, item: NmCluster) -> "NmConfigBuilder":
        """Add a single item to nm_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nm_clusters.append(item)
        return self

    def clear_nm_clusters(self) -> "NmConfigBuilder":
        """Clear all items from nm_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.nm_clusters = []
        return self

    def add_nm_cluster_coupling(self, item: NmClusterCoupling) -> "NmConfigBuilder":
        """Add a single item to nm_cluster_couplings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nm_cluster_couplings.append(item)
        return self

    def clear_nm_cluster_couplings(self) -> "NmConfigBuilder":
        """Clear all items from nm_cluster_couplings list.

        Returns:
            self for method chaining
        """
        self._obj.nm_cluster_couplings = []
        return self

    def add_nm_if_ecu(self, item: NmEcu) -> "NmConfigBuilder":
        """Add a single item to nm_if_ecus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nm_if_ecus.append(item)
        return self

    def clear_nm_if_ecus(self) -> "NmConfigBuilder":
        """Clear all items from nm_if_ecus list.

        Returns:
            self for method chaining
        """
        self._obj.nm_if_ecus = []
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


    def build(self) -> NmConfig:
        """Build and return the NmConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj