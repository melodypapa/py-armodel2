"""McSupportData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 172)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_sw_emulation_method_support import (
    McSwEmulationMethodSupport,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_support_data import (
    RptSupportData,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)


class McSupportData(ARObject):
    """AUTOSAR McSupportData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    emulations: list[McSwEmulationMethodSupport]
    mc_parameters: list[McDataInstance]
    mc_variables: list[McDataInstance]
    measurables: list[SwSystemconstantValueSet]
    rpt_support_data: Optional[RptSupportData]
    def __init__(self) -> None:
        """Initialize McSupportData."""
        super().__init__()
        self.emulations: list[McSwEmulationMethodSupport] = []
        self.mc_parameters: list[McDataInstance] = []
        self.mc_variables: list[McDataInstance] = []
        self.measurables: list[SwSystemconstantValueSet] = []
        self.rpt_support_data: Optional[RptSupportData] = None

    def serialize(self) -> ET.Element:
        """Serialize McSupportData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize emulations (list to container "EMULATIONS")
        if self.emulations:
            wrapper = ET.Element("EMULATIONS")
            for item in self.emulations:
                serialized = ARObject._serialize_item(item, "McSwEmulationMethodSupport")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_parameters (list to container "MC-PARAMETERS")
        if self.mc_parameters:
            wrapper = ET.Element("MC-PARAMETERS")
            for item in self.mc_parameters:
                serialized = ARObject._serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_variables (list to container "MC-VARIABLES")
        if self.mc_variables:
            wrapper = ET.Element("MC-VARIABLES")
            for item in self.mc_variables:
                serialized = ARObject._serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize measurables (list to container "MEASURABLES")
        if self.measurables:
            wrapper = ET.Element("MEASURABLES")
            for item in self.measurables:
                serialized = ARObject._serialize_item(item, "SwSystemconstantValueSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_support_data
        if self.rpt_support_data is not None:
            serialized = ARObject._serialize_item(self.rpt_support_data, "RptSupportData")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-SUPPORT-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McSupportData":
        """Deserialize XML element to McSupportData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McSupportData object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse emulations (list from container "EMULATIONS")
        obj.emulations = []
        container = ARObject._find_child_element(element, "EMULATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.emulations.append(child_value)

        # Parse mc_parameters (list from container "MC-PARAMETERS")
        obj.mc_parameters = []
        container = ARObject._find_child_element(element, "MC-PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_parameters.append(child_value)

        # Parse mc_variables (list from container "MC-VARIABLES")
        obj.mc_variables = []
        container = ARObject._find_child_element(element, "MC-VARIABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_variables.append(child_value)

        # Parse measurables (list from container "MEASURABLES")
        obj.measurables = []
        container = ARObject._find_child_element(element, "MEASURABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.measurables.append(child_value)

        # Parse rpt_support_data
        child = ARObject._find_child_element(element, "RPT-SUPPORT-DATA")
        if child is not None:
            rpt_support_data_value = ARObject._deserialize_by_tag(child, "RptSupportData")
            obj.rpt_support_data = rpt_support_data_value

        return obj



class McSupportDataBuilder:
    """Builder for McSupportData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McSupportData = McSupportData()

    def build(self) -> McSupportData:
        """Build and return McSupportData object.

        Returns:
            McSupportData instance
        """
        # TODO: Add validation
        return self._obj
