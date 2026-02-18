"""McGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 190)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2034)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_McGroups.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_function import (
    McFunction,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group_data_ref_set import (
    McGroupDataRefSet,
)


class McGroup(ARElement):
    """AUTOSAR McGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mc_functions: list[McFunction]
    ref_calprm_set: Optional[McGroupDataRefSet]
    ref: Optional[McGroupDataRefSet]
    sub_groups: list[McGroup]
    def __init__(self) -> None:
        """Initialize McGroup."""
        super().__init__()
        self.mc_functions: list[McFunction] = []
        self.ref_calprm_set: Optional[McGroupDataRefSet] = None
        self.ref: Optional[McGroupDataRefSet] = None
        self.sub_groups: list[McGroup] = []


class McGroupBuilder:
    """Builder for McGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McGroup = McGroup()

    def build(self) -> McGroup:
        """Build and return McGroup object.

        Returns:
            McGroup instance
        """
        # TODO: Add validation
        return self._obj
