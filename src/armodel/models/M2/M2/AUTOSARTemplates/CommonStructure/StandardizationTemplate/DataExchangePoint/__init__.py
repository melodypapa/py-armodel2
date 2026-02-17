"""DataExchangePoint module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.data_exchange_point import (
        DataExchangePoint,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.baseline import (
        Baseline,
    )

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.data_exchange_point_kind import (
    DataExchangePointKind,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.severity_enum import (
    SeverityEnum,
)

__all__ = [
    "Baseline",
    "DataExchangePoint",
    "DataExchangePointKind",
    "SeverityEnum",
]
