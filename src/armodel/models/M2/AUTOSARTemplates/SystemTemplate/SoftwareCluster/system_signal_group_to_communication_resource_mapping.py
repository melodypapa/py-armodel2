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
