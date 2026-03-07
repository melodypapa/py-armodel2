"""FlexrayNmClusterCoupling AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import NmClusterCouplingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    FlexrayNmScheduleVariant,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_cluster import (
    FlexrayNmCluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR FlexrayNmClusterCoupling."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-NM-CLUSTER-COUPLING"


    coupled_cluster_refs: list[ARRef]
    nm_schedule: Optional[FlexrayNmScheduleVariant]
    _DESERIALIZE_DISPATCH = {
        "COUPLED-CLUSTER-REFS": lambda obj, elem: [obj.coupled_cluster_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "NM-SCHEDULE": lambda obj, elem: setattr(obj, "nm_schedule", FlexrayNmScheduleVariant.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize FlexrayNmClusterCoupling."""
        super().__init__()
        self.coupled_cluster_refs: list[ARRef] = []
        self.nm_schedule: Optional[FlexrayNmScheduleVariant] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayNmClusterCoupling to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayNmClusterCoupling, self).serialize()

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
                serialized = SerializationHelper.serialize_item(item, "FlexrayNmCluster")
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

        # Serialize nm_schedule
        if self.nm_schedule is not None:
            serialized = SerializationHelper.serialize_item(self.nm_schedule, "FlexrayNmScheduleVariant")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-SCHEDULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmClusterCoupling":
        """Deserialize XML element to FlexrayNmClusterCoupling object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayNmClusterCoupling object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayNmClusterCoupling, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COUPLED-CLUSTER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.coupled_cluster_refs.append(ARRef.deserialize(item_elem))
            elif tag == "NM-SCHEDULE":
                setattr(obj, "nm_schedule", FlexrayNmScheduleVariant.deserialize(child))

        return obj



class FlexrayNmClusterCouplingBuilder(NmClusterCouplingBuilder):
    """Builder for FlexrayNmClusterCoupling with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayNmClusterCoupling = FlexrayNmClusterCoupling()


    def with_coupled_clusters(self, items: list[FlexrayNmCluster]) -> "FlexrayNmClusterCouplingBuilder":
        """Set coupled_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters = list(items) if items else []
        return self

    def with_nm_schedule(self, value: Optional[FlexrayNmScheduleVariant]) -> "FlexrayNmClusterCouplingBuilder":
        """Set nm_schedule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_schedule' is required and cannot be None")
        self._obj.nm_schedule = value
        return self


    def add_coupled_cluster(self, item: FlexrayNmCluster) -> "FlexrayNmClusterCouplingBuilder":
        """Add a single item to coupled_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters.append(item)
        return self

    def clear_coupled_clusters(self) -> "FlexrayNmClusterCouplingBuilder":
        """Clear all items from coupled_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "coupledCluster",
        "nmSchedule",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FlexrayNmClusterCoupling:
        """Build and return the FlexrayNmClusterCoupling instance with validation."""
        self._validate_instance()
        return self._obj