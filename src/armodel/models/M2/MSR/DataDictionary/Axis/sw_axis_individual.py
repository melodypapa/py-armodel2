"""SwAxisIndividual AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 354)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_generic import (
    SwAxisGeneric,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



class SwAxisIndividual(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisIndividual."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_method: Optional[CompuMethod]
    data_constr: Optional[DataConstr]
    input_variable: Optional[ApplicationPrimitiveDataType]
    sw_axis_generic: Optional[SwAxisGeneric]
    sw_max_axis: Optional[Integer]
    sw_min_axis: Optional[Integer]
    sw_variable_ref_proxie_refs: list[ARRef]
    unit: Optional[Unit]
    def __init__(self) -> None:
        """Initialize SwAxisIndividual."""
        super().__init__()
        self.compu_method: Optional[CompuMethod] = None
        self.data_constr: Optional[DataConstr] = None
        self.input_variable: Optional[ApplicationPrimitiveDataType] = None
        self.sw_axis_generic: Optional[SwAxisGeneric] = None
        self.sw_max_axis: Optional[Integer] = None
        self.sw_min_axis: Optional[Integer] = None
        self.sw_variable_ref_proxie_refs: list[ARRef] = []
        self.unit: Optional[Unit] = None

    def serialize(self) -> ET.Element:
        """Serialize SwAxisIndividual to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAxisIndividual, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_method
        if self.compu_method is not None:
            serialized = ARObject._serialize_item(self.compu_method, "CompuMethod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-METHOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_constr
        if self.data_constr is not None:
            serialized = ARObject._serialize_item(self.data_constr, "DataConstr")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-CONSTR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize input_variable
        if self.input_variable is not None:
            serialized = ARObject._serialize_item(self.input_variable, "ApplicationPrimitiveDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INPUT-VARIABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_axis_generic
        if self.sw_axis_generic is not None:
            serialized = ARObject._serialize_item(self.sw_axis_generic, "SwAxisGeneric")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-AXIS-GENERIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_max_axis
        if self.sw_max_axis is not None:
            serialized = ARObject._serialize_item(self.sw_max_axis, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-MAX-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_min_axis
        if self.sw_min_axis is not None:
            serialized = ARObject._serialize_item(self.sw_min_axis, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-MIN-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_variable_ref_proxie_refs (list to container "SW-VARIABLE-REF-PROXIES")
        if self.sw_variable_ref_proxie_refs:
            wrapper = ET.Element("SW-VARIABLE-REF-PROXIES")
            for item in self.sw_variable_ref_proxie_refs:
                serialized = ARObject._serialize_item(item, "SwVariableRefProxy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize unit
        if self.unit is not None:
            serialized = ARObject._serialize_item(self.unit, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisIndividual":
        """Deserialize XML element to SwAxisIndividual object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisIndividual object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAxisIndividual, cls).deserialize(element)

        # Parse compu_method
        child = ARObject._find_child_element(element, "COMPU-METHOD")
        if child is not None:
            compu_method_value = ARObject._deserialize_by_tag(child, "CompuMethod")
            obj.compu_method = compu_method_value

        # Parse data_constr
        child = ARObject._find_child_element(element, "DATA-CONSTR")
        if child is not None:
            data_constr_value = ARObject._deserialize_by_tag(child, "DataConstr")
            obj.data_constr = data_constr_value

        # Parse input_variable
        child = ARObject._find_child_element(element, "INPUT-VARIABLE")
        if child is not None:
            input_variable_value = ARObject._deserialize_by_tag(child, "ApplicationPrimitiveDataType")
            obj.input_variable = input_variable_value

        # Parse sw_axis_generic
        child = ARObject._find_child_element(element, "SW-AXIS-GENERIC")
        if child is not None:
            sw_axis_generic_value = ARObject._deserialize_by_tag(child, "SwAxisGeneric")
            obj.sw_axis_generic = sw_axis_generic_value

        # Parse sw_max_axis
        child = ARObject._find_child_element(element, "SW-MAX-AXIS")
        if child is not None:
            sw_max_axis_value = child.text
            obj.sw_max_axis = sw_max_axis_value

        # Parse sw_min_axis
        child = ARObject._find_child_element(element, "SW-MIN-AXIS")
        if child is not None:
            sw_min_axis_value = child.text
            obj.sw_min_axis = sw_min_axis_value

        # Parse sw_variable_ref_proxie_refs (list from container "SW-VARIABLE-REF-PROXIES")
        obj.sw_variable_ref_proxie_refs = []
        container = ARObject._find_child_element(element, "SW-VARIABLE-REF-PROXIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_variable_ref_proxie_refs.append(child_value)

        # Parse unit
        child = ARObject._find_child_element(element, "UNIT")
        if child is not None:
            unit_value = ARObject._deserialize_by_tag(child, "Unit")
            obj.unit = unit_value

        return obj



class SwAxisIndividualBuilder:
    """Builder for SwAxisIndividual."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisIndividual = SwAxisIndividual()

    def build(self) -> SwAxisIndividual:
        """Build and return SwAxisIndividual object.

        Returns:
            SwAxisIndividual instance
        """
        # TODO: Add validation
        return self._obj
