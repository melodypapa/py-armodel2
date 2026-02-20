"""FlexrayNmClusterCoupling AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    FlexrayNmScheduleVariant,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_cluster import (
    FlexrayNmCluster,
)


class FlexrayNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR FlexrayNmClusterCoupling."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    coupled_cluster_refs: list[ARRef]
    nm_schedule: Optional[FlexrayNmScheduleVariant]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayNmClusterCoupling, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize coupled_cluster_refs (list to container "COUPLED-CLUSTER-REFS")
        if self.coupled_cluster_refs:
            wrapper = ET.Element("COUPLED-CLUSTER-REFS")
            for item in self.coupled_cluster_refs:
                serialized = ARObject._serialize_item(item, "FlexrayNmCluster")
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
            serialized = ARObject._serialize_item(self.nm_schedule, "FlexrayNmScheduleVariant")
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

        # Parse coupled_cluster_refs (list from container "COUPLED-CLUSTER-REFS")
        obj.coupled_cluster_refs = []
        container = ARObject._find_child_element(element, "COUPLED-CLUSTER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coupled_cluster_refs.append(child_value)

        # Parse nm_schedule
        child = ARObject._find_child_element(element, "NM-SCHEDULE")
        if child is not None:
            nm_schedule_value = FlexrayNmScheduleVariant.deserialize(child)
            obj.nm_schedule = nm_schedule_value

        return obj



class FlexrayNmClusterCouplingBuilder:
    """Builder for FlexrayNmClusterCoupling."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmClusterCoupling = FlexrayNmClusterCoupling()

    def build(self) -> FlexrayNmClusterCoupling:
        """Build and return FlexrayNmClusterCoupling object.

        Returns:
            FlexrayNmClusterCoupling instance
        """
        # TODO: Add validation
        return self._obj
