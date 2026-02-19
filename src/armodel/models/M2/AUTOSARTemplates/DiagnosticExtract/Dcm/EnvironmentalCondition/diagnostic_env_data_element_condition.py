"""DiagnosticEnvDataElementCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_compare_condition import (
    DiagnosticEnvCompareCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class DiagnosticEnvDataElementCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvDataElementCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compare_value: Optional[ValueSpecification]
    data_prototype_ref: Optional[ARRef]
    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvDataElementCondition."""
        super().__init__()
        self.compare_value: Optional[ValueSpecification] = None
        self.data_prototype_ref: Optional[ARRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvDataElementCondition":
        """Deserialize XML element to DiagnosticEnvDataElementCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvDataElementCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvDataElementCondition, cls).deserialize(element)

        # Parse compare_value
        child = ARObject._find_child_element(element, "COMPARE-VALUE")
        if child is not None:
            compare_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.compare_value = compare_value_value

        # Parse data_prototype_ref
        child = ARObject._find_child_element(element, "DATA-PROTOTYPE")
        if child is not None:
            data_prototype_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.data_prototype_ref = data_prototype_ref_value

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



class DiagnosticEnvDataElementConditionBuilder:
    """Builder for DiagnosticEnvDataElementCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvDataElementCondition = DiagnosticEnvDataElementCondition()

    def build(self) -> DiagnosticEnvDataElementCondition:
        """Build and return DiagnosticEnvDataElementCondition object.

        Returns:
            DiagnosticEnvDataElementCondition instance
        """
        # TODO: Add validation
        return self._obj
