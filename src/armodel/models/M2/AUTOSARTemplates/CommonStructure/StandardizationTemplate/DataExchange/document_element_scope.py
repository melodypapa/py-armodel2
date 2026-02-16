"""DocumentElementScope AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)


class DocumentElementScope(SpecElementReference):
    """AUTOSAR DocumentElementScope."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "custom_document": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (TraceableElement),
        ),  # customDocument
        "tailorings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DataFormatElement),
        ),  # tailorings
    }

    def __init__(self) -> None:
        """Initialize DocumentElementScope."""
        super().__init__()
        self.custom_document: Optional[Any] = None
        self.tailorings: list[Any] = []


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
