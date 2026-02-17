"""LinMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config import (
    LinSlaveConfig,
)


class LinMaster(ARObject):
    """AUTOSAR LinMaster."""

    lin_slaves: list[LinSlaveConfig]
    time_base: Optional[TimeValue]
    time_base_jitter: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize LinMaster."""
        super().__init__()
        self.lin_slaves: list[LinSlaveConfig] = []
        self.time_base: Optional[TimeValue] = None
        self.time_base_jitter: Optional[TimeValue] = None


class LinMasterBuilder:
    """Builder for LinMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinMaster = LinMaster()

    def build(self) -> LinMaster:
        """Build and return LinMaster object.

        Returns:
            LinMaster instance
        """
        # TODO: Add validation
        return self._obj
