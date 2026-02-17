"""DdsCpServiceInstanceOperation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 475)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DdsCpServiceInstanceOperation(ARObject):
    """AUTOSAR DdsCpServiceInstanceOperation."""

    def __init__(self) -> None:
        """Initialize DdsCpServiceInstanceOperation."""
        super().__init__()
        self.dds_operation: Optional[PduTriggering] = None


class DdsCpServiceInstanceOperationBuilder:
    """Builder for DdsCpServiceInstanceOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpServiceInstanceOperation = DdsCpServiceInstanceOperation()

    def build(self) -> DdsCpServiceInstanceOperation:
        """Build and return DdsCpServiceInstanceOperation object.

        Returns:
            DdsCpServiceInstanceOperation instance
        """
        # TODO: Add validation
        return self._obj
