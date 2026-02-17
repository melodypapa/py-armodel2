"""Common module."""
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_scope import (
    SpecElementScope,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.data_format_element_reference import (
    DataFormatElementReference,
)

__all__ = [
    "DataFormatElementReference",
    "RestrictionWithSeverity",
    "SpecElementReference",
    "SpecElementScope",
]
