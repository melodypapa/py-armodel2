"""McDataInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    McdIdentifier,
    PositiveInteger,
    SymbolString,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.implementation_element_in_parameter_instance_ref import (
    ImplementationElementInParameterInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_access_details import (
    McDataAccessDetails,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_sw_prototyping_access import (
    RptSwPrototypingAccess,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class McDataInstance(Identifiable):
    """AUTOSAR McDataInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("array_size", None, True, False, None),  # arraySize
        ("display_identifier", None, True, False, None),  # displayIdentifier
        ("flat_map_entry", None, False, False, FlatInstanceDescriptor),  # flatMapEntry
        ("instance_in", None, False, False, ImplementationElementInParameterInstanceRef),  # instanceIn
        ("mc_data_access_details", None, False, False, McDataAccessDetails),  # mcDataAccessDetails
        ("mc_datas", None, False, True, RoleBasedMcDataAssignment),  # mcDatas
        ("resulting", None, False, False, SwDataDefProps),  # resulting
        ("resulting_rpt_sw", None, False, False, RptSwPrototypingAccess),  # resultingRptSw
        ("role", None, True, False, None),  # role
        ("rpt_impl_policy", None, False, False, RptImplPolicy),  # rptImplPolicy
        ("sub_elements", None, False, True, McDataInstance),  # subElements
        ("symbol", None, True, False, None),  # symbol
    ]

    def __init__(self) -> None:
        """Initialize McDataInstance."""
        super().__init__()
        self.array_size: Optional[PositiveInteger] = None
        self.display_identifier: Optional[McdIdentifier] = None
        self.flat_map_entry: Optional[FlatInstanceDescriptor] = None
        self.instance_in: Optional[ImplementationElementInParameterInstanceRef] = None
        self.mc_data_access_details: Optional[McDataAccessDetails] = None
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.resulting: Optional[SwDataDefProps] = None
        self.resulting_rpt_sw: Optional[RptSwPrototypingAccess] = None
        self.role: Optional[Identifier] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.sub_elements: list[McDataInstance] = []
        self.symbol: Optional[SymbolString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert McDataInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McDataInstance":
        """Create McDataInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            McDataInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to McDataInstance since parent returns ARObject
        return cast("McDataInstance", obj)


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
