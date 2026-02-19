"""SystemSignalToCommunicationResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 289)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SystemSignalToCommunicationResourceMapping(Identifiable):
    """AUTOSAR SystemSignalToCommunicationResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    software_cluster: Optional[CpSoftwareCluster]
    system_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SystemSignalToCommunicationResourceMapping."""
        super().__init__()
        self.software_cluster: Optional[CpSoftwareCluster] = None
        self.system_signal: Optional[SystemSignal] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignalToCommunicationResourceMapping":
        """Deserialize XML element to SystemSignalToCommunicationResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemSignalToCommunicationResourceMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse software_cluster
        child = ARObject._find_child_element(element, "SOFTWARE-CLUSTER")
        if child is not None:
            software_cluster_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.software_cluster = software_cluster_value

        # Parse system_signal
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL")
        if child is not None:
            system_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.system_signal = system_signal_value

        return obj



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
