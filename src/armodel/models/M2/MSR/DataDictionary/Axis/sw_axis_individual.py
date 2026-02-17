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

    compu_method: Optional[CompuMethod]
    data_constr: Optional[DataConstr]
    input_variable: Optional[ApplicationPrimitiveDataType]
    sw_axis_generic: Optional[SwAxisGeneric]
    sw_max_axis: Optional[Integer]
    sw_min_axis: Optional[Integer]
    sw_variable_ref_proxies: list[SwVariableRefProxy]
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
        self.sw_variable_ref_proxies: list[SwVariableRefProxy] = []
        self.unit: Optional[Unit] = None


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
