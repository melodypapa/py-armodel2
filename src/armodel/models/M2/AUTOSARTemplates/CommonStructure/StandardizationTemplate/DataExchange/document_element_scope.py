"""DocumentElementScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DocumentElementScope(SpecElementReference):
    """AUTOSAR DocumentElementScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_document: Optional[Any]
    tailorings: list[Any]
    def __init__(self) -> None:
        """Initialize DocumentElementScope."""
        super().__init__()
        self.custom_document: Optional[Any] = None
        self.tailorings: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentElementScope":
        """Deserialize XML element to DocumentElementScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentElementScope object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse custom_document
        child = ARObject._find_child_element(element, "CUSTOM-DOCUMENT")
        if child is not None:
            custom_document_value = child.text
            obj.custom_document = custom_document_value

        # Parse tailorings (list)
        obj.tailorings = []
        for child in ARObject._find_all_child_elements(element, "TAILORINGS"):
            tailorings_value = child.text
            obj.tailorings.append(tailorings_value)

        return obj



class DocumentElementScopeBuilder:
    """Builder for DocumentElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentElementScope = DocumentElementScope()

    def build(self) -> DocumentElementScope:
        """Build and return DocumentElementScope object.

        Returns:
            DocumentElementScope instance
        """
        # TODO: Add validation
        return self._obj
