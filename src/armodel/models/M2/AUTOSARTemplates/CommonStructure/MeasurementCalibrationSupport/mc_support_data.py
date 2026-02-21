"""McSupportData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 172)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    measurable_refs: list[ARRef]
    rpt_support_data: Optional[RptSupportData]
    def __init__(self) -> None:
        """Initialize McSupportData."""
        super().__init__()
        self.emulations: list[McSwEmulationMethodSupport] = []
        self.mc_parameters: list[McDataInstance] = []
        self.mc_variables: list[McDataInstance] = []
        self.measurable_refs: list[ARRef] = []
        self.rpt_support_data: Optional[RptSupportData] = None

    def serialize(self) -> ET.Element:
        """Serialize McSupportData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McSupportData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize emulations (list to container "EMULATIONS")
        if self.emulations:
            wrapper = ET.Element("EMULATIONS")
            for item in self.emulations:
                serialized = SerializationHelper.serialize_item(item, "McSwEmulationMethodSupport")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_parameters (list to container "MC-PARAMETERS")
        if self.mc_parameters:
            wrapper = ET.Element("MC-PARAMETERS")
            for item in self.mc_parameters:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_variables (list to container "MC-VARIABLES")
        if self.mc_variables:
            wrapper = ET.Element("MC-VARIABLES")
            for item in self.mc_variables:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize measurable_refs (list to container "MEASURABLE-REFS")
        if self.measurable_refs:
            wrapper = ET.Element("MEASURABLE-REFS")
            for item in self.measurable_refs:
                serialized = SerializationHelper.serialize_item(item, "SwSystemconstantValueSet")
                if serialized is not None:
                    child_elem = ET.Element("MEASURABLE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_support_data
        if self.rpt_support_data is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_support_data, "RptSupportData")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McSupportData, cls).deserialize(element)

        # Parse emulations (list from container "EMULATIONS")
        obj.emulations = []
        container = SerializationHelper.find_child_element(element, "EMULATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.emulations.append(child_value)

        # Parse mc_parameters (list from container "MC-PARAMETERS")
        obj.mc_parameters = []
        container = SerializationHelper.find_child_element(element, "MC-PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_parameters.append(child_value)

        # Parse mc_variables (list from container "MC-VARIABLES")
        obj.mc_variables = []
        container = SerializationHelper.find_child_element(element, "MC-VARIABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_variables.append(child_value)

        # Parse measurable_refs (list from container "MEASURABLE-REFS")
        obj.measurable_refs = []
        container = SerializationHelper.find_child_element(element, "MEASURABLE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.measurable_refs.append(child_value)

        # Parse rpt_support_data
        child = SerializationHelper.find_child_element(element, "RPT-SUPPORT-DATA")
        if child is not None:
            rpt_support_data_value = SerializationHelper.deserialize_by_tag(child, "RptSupportData")
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
