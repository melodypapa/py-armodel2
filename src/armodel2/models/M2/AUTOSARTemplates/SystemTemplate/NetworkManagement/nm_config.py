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
            if tag == "NM-CLUSTERS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "CAN-NM-CLUSTER":
                        obj.nm_clusters.append(SerializationHelper.deserialize_by_tag(item_elem, "CanNmCluster"))
                    elif concrete_tag == "FLEXRAY-NM-CLUSTER":
                        obj.nm_clusters.append(SerializationHelper.deserialize_by_tag(item_elem, "FlexrayNmCluster"))
                    elif concrete_tag == "J1939-NM-CLUSTER":
                        obj.nm_clusters.append(SerializationHelper.deserialize_by_tag(item_elem, "J1939NmCluster"))
                    elif concrete_tag == "UDP-NM-CLUSTER":
                        obj.nm_clusters.append(SerializationHelper.deserialize_by_tag(item_elem, "UdpNmCluster"))
            elif tag == "NM-CLUSTER-COUPLINGS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "CAN-NM-CLUSTER-COUPLING":
                        obj.nm_cluster_couplings.append(SerializationHelper.deserialize_by_tag(item_elem, "CanNmClusterCoupling"))
                    elif concrete_tag == "FLEXRAY-NM-CLUSTER-COUPLING":
                        obj.nm_cluster_couplings.append(SerializationHelper.deserialize_by_tag(item_elem, "FlexrayNmClusterCoupling"))
                    elif concrete_tag == "UDP-NM-CLUSTER-COUPLING":
                        obj.nm_cluster_couplings.append(SerializationHelper.deserialize_by_tag(item_elem, "UdpNmClusterCoupling"))
            elif tag == "NM-IF-ECUS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.nm_if_ecus.append(SerializationHelper.deserialize_by_tag(item_elem, "NmEcu"))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "nmCluster",
        "nmClusterCoupling",
        "nmIfEcu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> NmConfig:
        """Build and return the NmConfig instance with validation."""
        self._validate_instance()
        return self._obj