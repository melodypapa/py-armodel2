"""CpSoftwareClusterCommunicationResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 902)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterCommunicationResource(CpSoftwareClusterResource):
    """AUTOSAR CpSoftwareClusterCommunicationResource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "communication": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # communication
    }

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterCommunicationResource."""
        super().__init__()
        self.communication: Optional[CpSoftwareCluster] = None


class CpSoftwareClusterCommunicationResourceBuilder:
    """Builder for CpSoftwareClusterCommunicationResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterCommunicationResource = CpSoftwareClusterCommunicationResource()

    def build(self) -> CpSoftwareClusterCommunicationResource:
        """Build and return CpSoftwareClusterCommunicationResource object.

        Returns:
            CpSoftwareClusterCommunicationResource instance
        """
        # TODO: Add validation
        return self._obj
