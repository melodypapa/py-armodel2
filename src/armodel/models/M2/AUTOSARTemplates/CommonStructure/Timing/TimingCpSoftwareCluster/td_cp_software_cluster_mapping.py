"""TDCpSoftwareClusterMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 157)

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


class TDCpSoftwareClusterMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provider: Optional[CpSoftwareCluster]
    requestors: list[CpSoftwareCluster]
    timing: Optional[TimingDescription]
    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requestors: list[CpSoftwareCluster] = []
        self.timing: Optional[TimingDescription] = None
    def serialize(self) -> ET.Element:
        """Serialize TDCpSoftwareClusterMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDCpSoftwareClusterMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider
        if self.provider is not None:
            serialized = ARObject._serialize_item(self.provider, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requestors (list to container "REQUESTORS")
        if self.requestors:
            wrapper = ET.Element("REQUESTORS")
            for item in self.requestors:
                serialized = ARObject._serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterMapping":
        """Deserialize XML element to TDCpSoftwareClusterMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDCpSoftwareClusterMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDCpSoftwareClusterMapping, cls).deserialize(element)

        # Parse provider
        child = ARObject._find_child_element(element, "PROVIDER")
        if child is not None:
            provider_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.provider = provider_value

        # Parse requestors (list from container "REQUESTORS")
        obj.requestors = []
        container = ARObject._find_child_element(element, "REQUESTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.requestors.append(child_value)

        # Parse timing
        child = ARObject._find_child_element(element, "TIMING")
        if child is not None:
            timing_value = ARObject._deserialize_by_tag(child, "TimingDescription")
            obj.timing = timing_value

        return obj



class TDCpSoftwareClusterMappingBuilder:
    """Builder for TDCpSoftwareClusterMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDCpSoftwareClusterMapping = TDCpSoftwareClusterMapping()

    def build(self) -> TDCpSoftwareClusterMapping:
        """Build and return TDCpSoftwareClusterMapping object.

        Returns:
            TDCpSoftwareClusterMapping instance
        """
        # TODO: Add validation
        return self._obj
