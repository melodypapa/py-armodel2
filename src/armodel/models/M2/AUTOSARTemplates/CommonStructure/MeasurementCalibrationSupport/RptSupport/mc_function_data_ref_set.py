"""McFunctionDataRefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 187)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


class McFunctionDataRefSet(ARObject):
    """AUTOSAR McFunctionDataRefSet."""

    def __init__(self) -> None:
        """Initialize McFunctionDataRefSet."""
        super().__init__()
        self.flat_map_entries: list[FlatInstanceDescriptor] = []
        self.mc_data_instances: list[McDataInstance] = []


class McFunctionDataRefSetBuilder:
    """Builder for McFunctionDataRefSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McFunctionDataRefSet = McFunctionDataRefSet()

    def build(self) -> McFunctionDataRefSet:
        """Build and return McFunctionDataRefSet object.

        Returns:
            McFunctionDataRefSet instance
        """
        # TODO: Add validation
        return self._obj
