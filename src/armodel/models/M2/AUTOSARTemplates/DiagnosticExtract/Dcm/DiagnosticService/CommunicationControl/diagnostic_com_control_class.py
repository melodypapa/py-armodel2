"""DiagnosticComControlClass AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control import (
    DiagnosticComControl,
)


class DiagnosticComControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticComControlClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "all_channelses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CommunicationCluster,
        ),  # allChannelses
        "all_physicals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EthernetPhysical),
        ),  # allPhysicals
        "specific_channels": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticComControl,
        ),  # specificChannels
        "sub_nodes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticComControl,
        ),  # subNodes
    }

    def __init__(self) -> None:
        """Initialize DiagnosticComControlClass."""
        super().__init__()
        self.all_channelses: list[CommunicationCluster] = []
        self.all_physicals: list[Any] = []
        self.specific_channels: list[DiagnosticComControl] = []
        self.sub_nodes: list[DiagnosticComControl] = []


class DiagnosticComControlClassBuilder:
    """Builder for DiagnosticComControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlClass = DiagnosticComControlClass()

    def build(self) -> DiagnosticComControlClass:
        """Build and return DiagnosticComControlClass object.

        Returns:
            DiagnosticComControlClass instance
        """
        # TODO: Add validation
        return self._obj
