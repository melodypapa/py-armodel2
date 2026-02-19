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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.document_element_scope import (
    DocumentElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)


class SpecificationDocumentScope(SpecElementReference):
    """AUTOSAR SpecificationDocumentScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_documentation: Optional[Documentation]
    documents: list[DocumentElementScope]
    def __init__(self) -> None:
        """Initialize SpecificationDocumentScope."""
        super().__init__()
        self.custom_documentation: Optional[Documentation] = None
        self.documents: list[DocumentElementScope] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecificationDocumentScope":
        """Deserialize XML element to SpecificationDocumentScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecificationDocumentScope object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse custom_documentation
        child = ARObject._find_child_element(element, "CUSTOM-DOCUMENTATION")
        if child is not None:
            custom_documentation_value = ARObject._deserialize_by_tag(child, "Documentation")
            obj.custom_documentation = custom_documentation_value

        # Parse documents (list)
        obj.documents = []
        for child in ARObject._find_all_child_elements(element, "DOCUMENTS"):
            documents_value = ARObject._deserialize_by_tag(child, "DocumentElementScope")
            obj.documents.append(documents_value)

        return obj



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
