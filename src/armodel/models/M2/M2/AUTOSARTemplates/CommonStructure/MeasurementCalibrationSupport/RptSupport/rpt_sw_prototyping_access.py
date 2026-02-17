"""RptSwPrototypingAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 199)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 856)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptAccessEnum,
)


class RptSwPrototypingAccess(ARObject):
    """AUTOSAR RptSwPrototypingAccess."""

    def __init__(self) -> None:
        """Initialize RptSwPrototypingAccess."""
        super().__init__()
        self.rpt_hook_access: Optional[RptAccessEnum] = None
        self.rpt_read_access: Optional[RptAccessEnum] = None
        self.rpt_write_access: Optional[RptAccessEnum] = None


class RptSwPrototypingAccessBuilder:
    """Builder for RptSwPrototypingAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptSwPrototypingAccess = RptSwPrototypingAccess()

    def build(self) -> RptSwPrototypingAccess:
        """Build and return RptSwPrototypingAccess object.

        Returns:
            RptSwPrototypingAccess instance
        """
        # TODO: Add validation
        return self._obj
