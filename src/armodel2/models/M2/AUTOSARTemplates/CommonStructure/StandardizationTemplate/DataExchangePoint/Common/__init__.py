"""Common module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
        SpecElementReference,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_scope import (
        SpecElementScope,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
        RestrictionWithSeverity,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.data_format_element_reference import (
        DataFormatElementReference,
    )

__all__ = [
    "DataFormatElementReference",
    "RestrictionWithSeverity",
    "SpecElementReference",
    "SpecElementScope",
]
