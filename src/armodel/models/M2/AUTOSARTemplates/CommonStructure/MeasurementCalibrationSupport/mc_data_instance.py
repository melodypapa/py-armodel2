"""McDataInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 177)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 997)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    McdIdentifier,
    PositiveInteger,
    SymbolString,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.implementation_element_in_parameter_instance_ref import (
    ImplementationElementInParameterInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_sw_prototyping_access import (
    RptSwPrototypingAccess,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
        FlatInstanceDescriptor,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_access_details import (
        McDataAccessDetails,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
        RoleBasedMcDataAssignment,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class McDataInstance(Identifiable):
    """AUTOSAR McDataInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_size: Optional[PositiveInteger]
    display_identifier: Optional[McdIdentifier]
    flat_map_entry_ref: Optional[ARRef]
    instance_in: Optional[ImplementationElementInParameterInstanceRef]
    mc_data_access_details: Optional[McDataAccessDetails]
    mc_datas: list[RoleBasedMcDataAssignment]
    resulting: Optional[SwDataDefProps]
    resulting_rpt_sw: Optional[RptSwPrototypingAccess]
    role: Optional[Identifier]
    rpt_impl_policy: Optional[RptImplPolicy]
    sub_elements: list[McDataInstance]
    symbol: Optional[SymbolString]
    def __init__(self) -> None:
        """Initialize McDataInstance."""
        super().__init__()
        self.array_size: Optional[PositiveInteger] = None
        self.display_identifier: Optional[McdIdentifier] = None
        self.flat_map_entry_ref: Optional[ARRef] = None
        self.instance_in: Optional[ImplementationElementInParameterInstanceRef] = None
        self.mc_data_access_details: Optional[McDataAccessDetails] = None
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.resulting: Optional[SwDataDefProps] = None
        self.resulting_rpt_sw: Optional[RptSwPrototypingAccess] = None
        self.role: Optional[Identifier] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.sub_elements: list[McDataInstance] = []
        self.symbol: Optional[SymbolString] = None

    def serialize(self) -> ET.Element:
        """Serialize McDataInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McDataInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_size
        if self.array_size is not None:
            serialized = ARObject._serialize_item(self.array_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize display_identifier
        if self.display_identifier is not None:
            serialized = ARObject._serialize_item(self.display_identifier, "McdIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DISPLAY-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flat_map_entry_ref
        if self.flat_map_entry_ref is not None:
            serialized = ARObject._serialize_item(self.flat_map_entry_ref, "FlatInstanceDescriptor")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLAT-MAP-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize instance_in
        if self.instance_in is not None:
            serialized = ARObject._serialize_item(self.instance_in, "ImplementationElementInParameterInstanceRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INSTANCE-IN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mc_data_access_details
        if self.mc_data_access_details is not None:
            serialized = ARObject._serialize_item(self.mc_data_access_details, "McDataAccessDetails")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MC-DATA-ACCESS-DETAILS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mc_datas (list to container "MC-DATAS")
        if self.mc_datas:
            wrapper = ET.Element("MC-DATAS")
            for item in self.mc_datas:
                serialized = ARObject._serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resulting
        if self.resulting is not None:
            serialized = ARObject._serialize_item(self.resulting, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESULTING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resulting_rpt_sw
        if self.resulting_rpt_sw is not None:
            serialized = ARObject._serialize_item(self.resulting_rpt_sw, "RptSwPrototypingAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESULTING-RPT-SW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize role
        if self.role is not None:
            serialized = ARObject._serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_impl_policy
        if self.rpt_impl_policy is not None:
            serialized = ARObject._serialize_item(self.rpt_impl_policy, "RptImplPolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_elements (list to container "SUB-ELEMENTS")
        if self.sub_elements:
            wrapper = ET.Element("SUB-ELEMENTS")
            for item in self.sub_elements:
                serialized = ARObject._serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol
        if self.symbol is not None:
            serialized = ARObject._serialize_item(self.symbol, "SymbolString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McDataInstance":
        """Deserialize XML element to McDataInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McDataInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McDataInstance, cls).deserialize(element)

        # Parse array_size
        child = ARObject._find_child_element(element, "ARRAY-SIZE")
        if child is not None:
            array_size_value = child.text
            obj.array_size = array_size_value

        # Parse display_identifier
        child = ARObject._find_child_element(element, "DISPLAY-IDENTIFIER")
        if child is not None:
            display_identifier_value = child.text
            obj.display_identifier = display_identifier_value

        # Parse flat_map_entry_ref
        child = ARObject._find_child_element(element, "FLAT-MAP-ENTRY-REF")
        if child is not None:
            flat_map_entry_ref_value = ARRef.deserialize(child)
            obj.flat_map_entry_ref = flat_map_entry_ref_value

        # Parse instance_in
        child = ARObject._find_child_element(element, "INSTANCE-IN")
        if child is not None:
            instance_in_value = ARObject._deserialize_by_tag(child, "ImplementationElementInParameterInstanceRef")
            obj.instance_in = instance_in_value

        # Parse mc_data_access_details
        child = ARObject._find_child_element(element, "MC-DATA-ACCESS-DETAILS")
        if child is not None:
            mc_data_access_details_value = ARObject._deserialize_by_tag(child, "McDataAccessDetails")
            obj.mc_data_access_details = mc_data_access_details_value

        # Parse mc_datas (list from container "MC-DATAS")
        obj.mc_datas = []
        container = ARObject._find_child_element(element, "MC-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_datas.append(child_value)

        # Parse resulting
        child = ARObject._find_child_element(element, "RESULTING")
        if child is not None:
            resulting_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.resulting = resulting_value

        # Parse resulting_rpt_sw
        child = ARObject._find_child_element(element, "RESULTING-RPT-SW")
        if child is not None:
            resulting_rpt_sw_value = ARObject._deserialize_by_tag(child, "RptSwPrototypingAccess")
            obj.resulting_rpt_sw = resulting_rpt_sw_value

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse rpt_impl_policy
        child = ARObject._find_child_element(element, "RPT-IMPL-POLICY")
        if child is not None:
            rpt_impl_policy_value = ARObject._deserialize_by_tag(child, "RptImplPolicy")
            obj.rpt_impl_policy = rpt_impl_policy_value

        # Parse sub_elements (list from container "SUB-ELEMENTS")
        obj.sub_elements = []
        container = ARObject._find_child_element(element, "SUB-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_elements.append(child_value)

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = ARObject._deserialize_by_tag(child, "SymbolString")
            obj.symbol = symbol_value

        return obj



class McDataInstanceBuilder:
    """Builder for McDataInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McDataInstance = McDataInstance()

    def build(self) -> McDataInstance:
        """Build and return McDataInstance object.

        Returns:
            McDataInstance instance
        """
        # TODO: Add validation
        return self._obj
