"""SpecificationDocumentScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "custom_documentation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Documentation,
        ),  # customDocumentation
        "documents": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DocumentElementScope,
        ),  # documents
    }

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
