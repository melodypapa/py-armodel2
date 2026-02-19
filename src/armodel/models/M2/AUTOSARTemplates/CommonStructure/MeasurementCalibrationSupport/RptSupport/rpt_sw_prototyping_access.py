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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rpt_hook_access: Optional[RptAccessEnum]
    rpt_read_access: Optional[RptAccessEnum]
    rpt_write_access: Optional[RptAccessEnum]
    def __init__(self) -> None:
        """Initialize RptSwPrototypingAccess."""
        super().__init__()
        self.rpt_hook_access: Optional[RptAccessEnum] = None
        self.rpt_read_access: Optional[RptAccessEnum] = None
        self.rpt_write_access: Optional[RptAccessEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptSwPrototypingAccess":
        """Deserialize XML element to RptSwPrototypingAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptSwPrototypingAccess object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse rpt_hook_access
        child = ARObject._find_child_element(element, "RPT-HOOK-ACCESS")
        if child is not None:
            rpt_hook_access_value = RptAccessEnum.deserialize(child)
            obj.rpt_hook_access = rpt_hook_access_value

        # Parse rpt_read_access
        child = ARObject._find_child_element(element, "RPT-READ-ACCESS")
        if child is not None:
            rpt_read_access_value = RptAccessEnum.deserialize(child)
            obj.rpt_read_access = rpt_read_access_value

        # Parse rpt_write_access
        child = ARObject._find_child_element(element, "RPT-WRITE-ACCESS")
        if child is not None:
            rpt_write_access_value = RptAccessEnum.deserialize(child)
            obj.rpt_write_access = rpt_write_access_value

        return obj



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
