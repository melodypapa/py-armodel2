"""TDCpSoftwareClusterMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)


class TDCpSoftwareClusterMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "provider": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # provider
        "requestors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CpSoftwareCluster,
        ),  # requestors
        "timing": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingDescription,
        ),  # timing
    }

    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requestors: list[CpSoftwareCluster] = []
        self.timing: Optional[TimingDescription] = None


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
