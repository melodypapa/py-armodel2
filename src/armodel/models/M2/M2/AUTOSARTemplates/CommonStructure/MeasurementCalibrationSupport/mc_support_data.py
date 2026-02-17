"""McSupportData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 172)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "emulations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=McSwEmulationMethodSupport,
        ),  # emulations
        "mc_parameters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=McDataInstance,
        ),  # mcParameters
        "mc_variables": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=McDataInstance,
        ),  # mcVariables
        "measurables": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwSystemconstantValueSet,
        ),  # measurables
        "rpt_support_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptSupportData,
        ),  # rptSupportData
    }

    def __init__(self) -> None:
        """Initialize McSupportData."""
        super().__init__()
        self.emulations: list[McSwEmulationMethodSupport] = []
        self.mc_parameters: list[McDataInstance] = []
        self.mc_variables: list[McDataInstance] = []
        self.measurables: list[SwSystemconstantValueSet] = []
        self.rpt_support_data: Optional[RptSupportData] = None


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
