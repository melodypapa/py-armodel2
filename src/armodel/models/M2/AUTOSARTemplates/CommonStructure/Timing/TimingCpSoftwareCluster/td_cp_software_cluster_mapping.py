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
