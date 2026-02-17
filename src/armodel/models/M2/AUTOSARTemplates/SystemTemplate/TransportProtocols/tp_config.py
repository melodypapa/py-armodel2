"""TpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 587)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class TpConfig(FibexElement):
    """AUTOSAR TpConfig."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "communication_cluster": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CommunicationCluster,
        ),  # communicationCluster
    }

    def __init__(self) -> None:
        """Initialize TpConfig."""
        super().__init__()
        self.communication_cluster: Optional[CommunicationCluster] = None


class TpConfigBuilder:
    """Builder for TpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConfig = TpConfig()

    def build(self) -> TpConfig:
        """Build and return TpConfig object.

        Returns:
            TpConfig instance
        """
        # TODO: Add validation
        return self._obj
