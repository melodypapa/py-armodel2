"""SystemSignalGroupToCommunicationResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 290)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)


class SystemSignalGroupToCommunicationResourceMapping(Identifiable):
    """AUTOSAR SystemSignalGroupToCommunicationResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    software_cluster: Optional[CpSoftwareCluster]
    system_signal_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SystemSignalGroupToCommunicationResourceMapping."""
        super().__init__()
        self.software_cluster: Optional[CpSoftwareCluster] = None
        self.system_signal_group_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignalGroupToCommunicationResourceMapping":
        """Deserialize XML element to SystemSignalGroupToCommunicationResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemSignalGroupToCommunicationResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SystemSignalGroupToCommunicationResourceMapping, cls).deserialize(element)

        # Parse software_cluster
        child = ARObject._find_child_element(element, "SOFTWARE-CLUSTER")
        if child is not None:
            software_cluster_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.software_cluster = software_cluster_value

        # Parse system_signal_group_ref
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL-GROUP")
        if child is not None:
            system_signal_group_ref_value = ARObject._deserialize_by_tag(child, "SystemSignalGroup")
            obj.system_signal_group_ref = system_signal_group_ref_value

        return obj



class SystemSignalGroupToCommunicationResourceMappingBuilder:
    """Builder for SystemSignalGroupToCommunicationResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignalGroupToCommunicationResourceMapping = SystemSignalGroupToCommunicationResourceMapping()

    def build(self) -> SystemSignalGroupToCommunicationResourceMapping:
        """Build and return SystemSignalGroupToCommunicationResourceMapping object.

        Returns:
            SystemSignalGroupToCommunicationResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
