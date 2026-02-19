"""TDCpSoftwareClusterResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)


class TDCpSoftwareClusterResourceMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    resource: Optional[CpSoftwareCluster]
    timing: Optional[TimingDescription]
    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterResourceMapping."""
        super().__init__()
        self.resource: Optional[CpSoftwareCluster] = None
        self.timing: Optional[TimingDescription] = None
    def serialize(self) -> ET.Element:
        """Serialize TDCpSoftwareClusterResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDCpSoftwareClusterResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize resource
        if self.resource is not None:
            serialized = ARObject._serialize_item(self.resource, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing
        if self.timing is not None:
            serialized = ARObject._serialize_item(self.timing, "TimingDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterResourceMapping":
        """Deserialize XML element to TDCpSoftwareClusterResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDCpSoftwareClusterResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDCpSoftwareClusterResourceMapping, cls).deserialize(element)

        # Parse resource
        child = ARObject._find_child_element(element, "RESOURCE")
        if child is not None:
            resource_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.resource = resource_value

        # Parse timing
        child = ARObject._find_child_element(element, "TIMING")
        if child is not None:
            timing_value = ARObject._deserialize_by_tag(child, "TimingDescription")
            obj.timing = timing_value

        return obj



class TDCpSoftwareClusterResourceMappingBuilder:
    """Builder for TDCpSoftwareClusterResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDCpSoftwareClusterResourceMapping = TDCpSoftwareClusterResourceMapping()

    def build(self) -> TDCpSoftwareClusterResourceMapping:
        """Build and return TDCpSoftwareClusterResourceMapping object.

        Returns:
            TDCpSoftwareClusterResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
