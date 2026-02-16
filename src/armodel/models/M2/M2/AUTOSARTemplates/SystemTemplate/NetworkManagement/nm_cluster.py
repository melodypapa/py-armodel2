"""NmCluster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class NmCluster(Identifiable):
    """AUTOSAR NmCluster."""
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
        "nm_channel": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmChannel
        "nm_node": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmNode
        "nm_node_id_enabled": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmNodeIdEnabled
        "nm_pnc": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmPnc
        "nm_repeat_msg_ind_enabled": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmRepeatMsgIndEnabled
        "nm": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nm
        "pnc_cluster": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pncCluster
    }

    def __init__(self) -> None:
        """Initialize NmCluster."""
        super().__init__()
        self.communication_cluster: Optional[CommunicationCluster] = None
        self.nm_channel: Optional[Boolean] = None
        self.nm_node: Optional[Boolean] = None
        self.nm_node_id_enabled: Optional[Boolean] = None
        self.nm_pnc: Optional[Boolean] = None
        self.nm_repeat_msg_ind_enabled: Optional[Boolean] = None
        self.nm: Optional[Boolean] = None
        self.pnc_cluster: Optional[PositiveInteger] = None


class NmClusterBuilder:
    """Builder for NmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmCluster = NmCluster()

    def build(self) -> NmCluster:
        """Build and return NmCluster object.

        Returns:
            NmCluster instance
        """
        # TODO: Add validation
        return self._obj
