"""McDataInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 177)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 997)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "array_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # arraySize
        "display_identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # displayIdentifier
        "flat_map_entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FlatInstanceDescriptor,
        ),  # flatMapEntry
        "instance_in": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ImplementationElementInParameterInstanceRef,
        ),  # instanceIn
        "mc_data_access_details": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McDataAccessDetails,
        ),  # mcDataAccessDetails
        "mc_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RoleBasedMcDataAssignment,
        ),  # mcDatas
        "resulting": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # resulting
        "resulting_rpt_sw": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptSwPrototypingAccess,
        ),  # resultingRptSw
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
        "rpt_impl_policy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptImplPolicy,
        ),  # rptImplPolicy
        "sub_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=McDataInstance,
        ),  # subElements
        "symbol": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # symbol
    }

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
