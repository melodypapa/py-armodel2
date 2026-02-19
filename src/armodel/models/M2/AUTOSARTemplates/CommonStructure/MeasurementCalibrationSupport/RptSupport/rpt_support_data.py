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
    def serialize(self) -> ET.Element:
        """Serialize RptSupportData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize executions (list to container "EXECUTIONS")
        if self.executions:
            wrapper = ET.Element("EXECUTIONS")
            for item in self.executions:
                serialized = ARObject._serialize_item(item, "RptExecutionContext")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_components (list to container "RPT-COMPONENTS")
        if self.rpt_components:
            wrapper = ET.Element("RPT-COMPONENTS")
            for item in self.rpt_components:
                serialized = ARObject._serialize_item(item, "RptComponent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_service_points (list to container "RPT-SERVICE-POINTS")
        if self.rpt_service_points:
            wrapper = ET.Element("RPT-SERVICE-POINTS")
            for item in self.rpt_service_points:
                serialized = ARObject._serialize_item(item, "RptServicePoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

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

        # Parse executions (list from container "EXECUTIONS")
        obj.executions = []
        container = ARObject._find_child_element(element, "EXECUTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.executions.append(child_value)

        # Parse rpt_components (list from container "RPT-COMPONENTS")
        obj.rpt_components = []
        container = ARObject._find_child_element(element, "RPT-COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_components.append(child_value)

        # Parse rpt_service_points (list from container "RPT-SERVICE-POINTS")
        obj.rpt_service_points = []
        container = ARObject._find_child_element(element, "RPT-SERVICE-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_service_points.append(child_value)

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
