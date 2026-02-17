"""DataComProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import (
    DataConsistencyPolicyEnum,
    SendIndicationEnum,
)


class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR DataComProps."""

    def __init__(self) -> None:
        """Initialize DataComProps."""
        super().__init__()
        self.data: Optional[DataConsistencyPolicyEnum] = None
        self.send_indication_enum: Optional[SendIndicationEnum] = None


class DataComPropsBuilder:
    """Builder for DataComProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataComProps = DataComProps()

    def build(self) -> DataComProps:
        """Build and return DataComProps object.

        Returns:
            DataComProps instance
        """
        # TODO: Add validation
        return self._obj
