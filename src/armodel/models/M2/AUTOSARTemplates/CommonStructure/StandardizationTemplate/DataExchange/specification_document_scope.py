"""SpecificationDocumentScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.document_element_scope import (
    DocumentElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)


class SpecificationDocumentScope(SpecElementReference):
    """AUTOSAR SpecificationDocumentScope."""

    custom_documentation: Optional[Documentation]
    documents: list[DocumentElementScope]
    def __init__(self) -> None:
        """Initialize SpecificationDocumentScope."""
        super().__init__()
        self.custom_documentation: Optional[Documentation] = None
        self.documents: list[DocumentElementScope] = []


class SpecificationDocumentScopeBuilder:
    """Builder for SpecificationDocumentScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecificationDocumentScope = SpecificationDocumentScope()

    def build(self) -> SpecificationDocumentScope:
        """Build and return SpecificationDocumentScope object.

        Returns:
            SpecificationDocumentScope instance
        """
        # TODO: Add validation
        return self._obj
