"""SpecificationScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_document_scope import (
    SpecificationDocumentScope,
)


class SpecificationScope(ARObject):
    """AUTOSAR SpecificationScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    specification_documents: list[SpecificationDocumentScope]
    def __init__(self) -> None:
        """Initialize SpecificationScope."""
        super().__init__()
        self.specification_documents: list[SpecificationDocumentScope] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecificationScope":
        """Deserialize XML element to SpecificationScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecificationScope object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse specification_documents (list)
        obj.specification_documents = []
        for child in ARObject._find_all_child_elements(element, "SPECIFICATION-DOCUMENTS"):
            specification_documents_value = ARObject._deserialize_by_tag(child, "SpecificationDocumentScope")
            obj.specification_documents.append(specification_documents_value)

        return obj



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
