"""ExecutionOrderConstraint module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.execution_order_constraint import (
        ExecutionOrderConstraint,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
        EOCExecutableEntityRefAbstract,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_group import (
        EOCExecutableEntityRefGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref import (
        EOCExecutableEntityRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_event_ref import (
        EOCEventRef,
    )

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.execution_order_constraint_type_enum import (
    ExecutionOrderConstraintTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.let_data_exchange_paradigm_enum import (
    LetDataExchangeParadigmEnum,
)

__all__ = [
    "EOCEventRef",
    "EOCExecutableEntityRef",
    "EOCExecutableEntityRefAbstract",
    "EOCExecutableEntityRefGroup",
    "ExecutionOrderConstraint",
    "ExecutionOrderConstraintTypeEnum",
    "LetDataExchangeParadigmEnum",
]
