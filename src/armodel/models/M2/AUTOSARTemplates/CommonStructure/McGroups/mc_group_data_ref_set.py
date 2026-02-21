"""McGroupDataRefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 191)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2035)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_McGroups.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


@atp_variant()

class McGroupDataRefSet(ARObject):
    """AUTOSAR McGroupDataRefSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    flat_map_entrie_refs: list[ARRef]
    mc_data_instance_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize McGroupDataRefSet."""
        super().__init__()
        self.flat_map_entrie_refs: list[ARRef] = []
        self.mc_data_instance_refs: list[ARRef] = []



class McGroupDataRefSetBuilder:
    """Builder for McGroupDataRefSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McGroupDataRefSet = McGroupDataRefSet()

    def build(self) -> McGroupDataRefSet:
        """Build and return McGroupDataRefSet object.

        Returns:
            McGroupDataRefSet instance
        """
        # TODO: Add validation
        return self._obj
