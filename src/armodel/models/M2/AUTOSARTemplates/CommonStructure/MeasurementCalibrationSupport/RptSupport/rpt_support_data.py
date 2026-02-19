"""RptSupportData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 198)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_component import (
    RptComponent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_service_point import (
    RptServicePoint,
)


class RptSupportData(ARObject):
    """AUTOSAR RptSupportData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    executions: list[RptExecutionContext]
    rpt_components: list[RptComponent]
    rpt_service_points: list[RptServicePoint]
    def __init__(self) -> None:
        """Initialize RptSupportData."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.rpt_components: list[RptComponent] = []
        self.rpt_service_points: list[RptServicePoint] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptSupportData":
        """Deserialize XML element to RptSupportData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptSupportData object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse executions (list)
        obj.executions = []
        for child in ARObject._find_all_child_elements(element, "EXECUTIONS"):
            executions_value = ARObject._deserialize_by_tag(child, "RptExecutionContext")
            obj.executions.append(executions_value)

        # Parse rpt_components (list)
        obj.rpt_components = []
        for child in ARObject._find_all_child_elements(element, "RPT-COMPONENTS"):
            rpt_components_value = ARObject._deserialize_by_tag(child, "RptComponent")
            obj.rpt_components.append(rpt_components_value)

        # Parse rpt_service_points (list)
        obj.rpt_service_points = []
        for child in ARObject._find_all_child_elements(element, "RPT-SERVICE-POINTS"):
            rpt_service_points_value = ARObject._deserialize_by_tag(child, "RptServicePoint")
            obj.rpt_service_points.append(rpt_service_points_value)

        return obj



class RptSupportDataBuilder:
    """Builder for RptSupportData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptSupportData = RptSupportData()

    def build(self) -> RptSupportData:
        """Build and return RptSupportData object.

        Returns:
            RptSupportData instance
        """
        # TODO: Add validation
        return self._obj
