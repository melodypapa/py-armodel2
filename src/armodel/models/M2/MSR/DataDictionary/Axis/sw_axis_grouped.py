"""SwAxisGrouped AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 357)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
    ApplicationPrimitiveDataType,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)


class SwAxisGrouped(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisGrouped."""

    def __init__(self) -> None:
        """Initialize SwAxisGrouped."""
        super().__init__()
        self.shared_axis_type: Optional[ApplicationPrimitiveDataType] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calprm_ref_proxy: SwCalprmRefProxy = None


class SwAxisGroupedBuilder:
    """Builder for SwAxisGrouped."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisGrouped = SwAxisGrouped()

    def build(self) -> SwAxisGrouped:
        """Build and return SwAxisGrouped object.

        Returns:
            SwAxisGrouped instance
        """
        # TODO: Add validation
        return self._obj
