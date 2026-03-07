"""CanNmClusterCoupling AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 684)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import NmClusterCouplingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.can_nm_cluster import (
    CanNmCluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR CanNmClusterCoupling."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-NM-CLUSTER-COUPLING"


    coupled_cluster_refs: list[ARRef]
    nm_busload_reduction: Optional[Any]
    nm_immediate: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "COUPLED-CLUSTER-REFS": lambda obj, elem: [obj.coupled_cluster_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "NM-BUSLOAD-REDUCTION": lambda obj, elem: setattr(obj, "nm_busload_reduction", SerializationHelper.deserialize_by_tag(elem, "any (BooleanEnabled)")),
        "NM-IMMEDIATE": lambda obj, elem: setattr(obj, "nm_immediate", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize CanNmClusterCoupling."""
        super().__init__()
        self.coupled_cluster_refs: list[ARRef] = []
        self.nm_busload_reduction: Optional[Any] = None
        self.nm_immediate: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CanNmClusterCoupling to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanNmClusterCoupling, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize coupled_cluster_refs (list to container "COUPLED-CLUSTER-REFS")
        if self.coupled_cluster_refs:
            wrapper = ET.Element("COUPLED-CLUSTER-REFS")
            for item in self.coupled_cluster_refs:
                serialized = SerializationHelper.serialize_item(item, "CanNmCluster")
                if serialized is not None:
                    child_elem = ET.Element("COUPLED-CLUSTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_busload_reduction
        if self.nm_busload_reduction is not None:
            serialized = SerializationHelper.serialize_item(self.nm_busload_reduction, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-BUSLOAD-REDUCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_immediate
        if self.nm_immediate is not None:
            serialized = SerializationHelper.serialize_item(self.nm_immediate, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-IMMEDIATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmClusterCoupling":
        """Deserialize XML element to CanNmClusterCoupling object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanNmClusterCoupling object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanNmClusterCoupling, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COUPLED-CLUSTER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.coupled_cluster_refs.append(ARRef.deserialize(item_elem))
            elif tag == "NM-BUSLOAD-REDUCTION":
                setattr(obj, "nm_busload_reduction", SerializationHelper.deserialize_by_tag(child, "any (BooleanEnabled)"))
            elif tag == "NM-IMMEDIATE":
                setattr(obj, "nm_immediate", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class CanNmClusterCouplingBuilder(NmClusterCouplingBuilder):
    """Builder for CanNmClusterCoupling with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanNmClusterCoupling = CanNmClusterCoupling()


    def with_coupled_clusters(self, items: list[CanNmCluster]) -> "CanNmClusterCouplingBuilder":
        """Set coupled_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters = list(items) if items else []
        return self

    def with_nm_busload_reduction(self, value: Optional[Any]) -> "CanNmClusterCouplingBuilder":
        """Set nm_busload_reduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_busload_reduction' is required and cannot be None")
        self._obj.nm_busload_reduction = value
        return self

    def with_nm_immediate(self, value: Optional[Boolean]) -> "CanNmClusterCouplingBuilder":
        """Set nm_immediate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_immediate' is required and cannot be None")
        self._obj.nm_immediate = value
        return self


    def add_coupled_cluster(self, item: CanNmCluster) -> "CanNmClusterCouplingBuilder":
        """Add a single item to coupled_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters.append(item)
        return self

    def clear_coupled_clusters(self) -> "CanNmClusterCouplingBuilder":
        """Clear all items from coupled_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "coupledCluster",
        "nmBusloadReduction",
        "nmImmediate",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CanNmClusterCoupling:
        """Build and return the CanNmClusterCoupling instance with validation."""
        self._validate_instance()
        return self._obj