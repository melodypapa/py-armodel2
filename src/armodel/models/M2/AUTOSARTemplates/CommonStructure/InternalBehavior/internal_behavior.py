"""InternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 64)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 319)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 516)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2033)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 231)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 453)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class InternalBehavior(Identifiable):
    """AUTOSAR InternalBehavior."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize InternalBehavior."""
        super().__init__()
        self.constants: list[ParameterDataPrototype] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_types: list[DataTypeMappingSet] = []
        self.exclusive_areas: list[ExclusiveArea] = []
        self.exclusive_area_nestings: list[ExclusiveAreaNestingOrder] = []
        self.static_memories: list[VariableDataPrototype] = []


class InternalBehaviorBuilder:
    """Builder for InternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalBehavior = InternalBehavior()

    def build(self) -> InternalBehavior:
        """Build and return InternalBehavior object.

        Returns:
            InternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
