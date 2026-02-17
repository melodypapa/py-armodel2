"""DataExchange module."""
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_scope import (
    SpecificationScope,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_document_scope import (
    SpecificationDocumentScope,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.document_element_scope import (
    DocumentElementScope,
)

__all__ = [
    "DocumentElementScope",
    "SpecificationDocumentScope",
    "SpecificationScope",
]
