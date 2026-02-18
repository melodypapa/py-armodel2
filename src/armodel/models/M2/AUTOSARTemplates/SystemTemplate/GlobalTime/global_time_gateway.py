"""GlobalTimeGateway AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 861)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)


class GlobalTimeGateway(Identifiable):
    """AUTOSAR GlobalTimeGateway."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    host: Optional[EcuInstance]
    master: Optional[GlobalTimeMaster]
    slave: Optional[GlobalTimeSlave]
    def __init__(self) -> None:
        """Initialize GlobalTimeGateway."""
        super().__init__()
        self.host: Optional[EcuInstance] = None
        self.master: Optional[GlobalTimeMaster] = None
        self.slave: Optional[GlobalTimeSlave] = None


class GlobalTimeGatewayBuilder:
    """Builder for GlobalTimeGateway."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeGateway = GlobalTimeGateway()

    def build(self) -> GlobalTimeGateway:
        """Build and return GlobalTimeGateway object.

        Returns:
            GlobalTimeGateway instance
        """
        # TODO: Add validation
        return self._obj
