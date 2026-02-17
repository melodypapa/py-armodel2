"""ClientServerOperationComProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR ClientServerOperationComProps."""

    def __init__(self) -> None:
        """Initialize ClientServerOperationComProps."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None


class ClientServerOperationComPropsBuilder:
    """Builder for ClientServerOperationComProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationComProps = ClientServerOperationComProps()

    def build(self) -> ClientServerOperationComProps:
        """Build and return ClientServerOperationComProps object.

        Returns:
            ClientServerOperationComProps instance
        """
        # TODO: Add validation
        return self._obj
