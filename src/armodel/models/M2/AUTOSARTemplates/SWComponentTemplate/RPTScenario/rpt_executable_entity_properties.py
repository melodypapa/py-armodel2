"""RptExecutableEntityProperties AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 859)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptExecutionControlEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    RptServicePointEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RptExecutableEntityProperties(ARObject):
    """AUTOSAR RptExecutableEntityProperties."""

    max_rpt_event_id: Optional[PositiveInteger]
    min_rpt_event_id: Optional[PositiveInteger]
    rpt_execution_control: Optional[RptExecutionControlEnum]
    rpt_service_point_enum: Optional[RptServicePointEnum]
    def __init__(self) -> None:
        """Initialize RptExecutableEntityProperties."""
        super().__init__()
        self.max_rpt_event_id: Optional[PositiveInteger] = None
        self.min_rpt_event_id: Optional[PositiveInteger] = None
        self.rpt_execution_control: Optional[RptExecutionControlEnum] = None
        self.rpt_service_point_enum: Optional[RptServicePointEnum] = None


class RptExecutableEntityPropertiesBuilder:
    """Builder for RptExecutableEntityProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptExecutableEntityProperties = RptExecutableEntityProperties()

    def build(self) -> RptExecutableEntityProperties:
        """Build and return RptExecutableEntityProperties object.

        Returns:
            RptExecutableEntityProperties instance
        """
        # TODO: Add validation
        return self._obj
