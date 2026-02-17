"""SpecificationScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_document_scope import (
    SpecificationDocumentScope,
)


class SpecificationScope(ARObject):
    """AUTOSAR SpecificationScope."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "specification_documents": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SpecificationDocumentScope,
        ),  # specificationDocuments
    }

    def __init__(self) -> None:
        """Initialize SpecificationScope."""
        super().__init__()
        self.specification_documents: list[SpecificationDocumentScope] = []


class SpecificationScopeBuilder:
    """Builder for SpecificationScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecificationScope = SpecificationScope()

    def build(self) -> SpecificationScope:
        """Build and return SpecificationScope object.

        Returns:
            SpecificationScope instance
        """
        # TODO: Add validation
        return self._obj
