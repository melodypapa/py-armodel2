"""SystemSignalToCommunicationResourceMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SystemSignalToCommunicationResourceMapping(Identifiable):
    """AUTOSAR SystemSignalToCommunicationResourceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "software_cluster": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # softwareCluster
        "system_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SystemSignal,
        ),  # systemSignal
    }

    def __init__(self) -> None:
        """Initialize SystemSignalToCommunicationResourceMapping."""
        super().__init__()
        self.software_cluster: Optional[CpSoftwareCluster] = None
        self.system_signal: Optional[SystemSignal] = None


class SystemSignalToCommunicationResourceMappingBuilder:
    """Builder for SystemSignalToCommunicationResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignalToCommunicationResourceMapping = SystemSignalToCommunicationResourceMapping()

    def build(self) -> SystemSignalToCommunicationResourceMapping:
        """Build and return SystemSignalToCommunicationResourceMapping object.

        Returns:
            SystemSignalToCommunicationResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
