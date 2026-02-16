"""DiagnosticComControlClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("all_channelses", None, False, True, CommunicationCluster),  # allChannelses
        ("all_physicals", None, False, True, any (EthernetPhysical)),  # allPhysicals
        ("specific_channels", None, False, True, DiagnosticComControl),  # specificChannels
        ("sub_nodes", None, False, True, DiagnosticComControl),  # subNodes
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticComControlClass."""
        super().__init__()
        self.all_channelses: list[CommunicationCluster] = []
        self.all_physicals: list[Any] = []
        self.specific_channels: list[DiagnosticComControl] = []
        self.sub_nodes: list[DiagnosticComControl] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticComControlClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlClass":
        """Create DiagnosticComControlClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticComControlClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticComControlClass since parent returns ARObject
        return cast("DiagnosticComControlClass", obj)


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
