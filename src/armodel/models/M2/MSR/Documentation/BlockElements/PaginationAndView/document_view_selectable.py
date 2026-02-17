"""DocumentViewSelectable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 340)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_PaginationAndView.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameTokens,
    ViewTokens,
)


class DocumentViewSelectable(ARObject):
    """AUTOSAR DocumentViewSelectable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "si": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # si
        "view": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # view
    }

    def __init__(self) -> None:
        """Initialize DocumentViewSelectable."""
        super().__init__()
        self.si: NameTokens = None
        self.view: Optional[ViewTokens] = None


class DocumentViewSelectableBuilder:
    """Builder for DocumentViewSelectable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentViewSelectable = DocumentViewSelectable()

    def build(self) -> DocumentViewSelectable:
        """Build and return DocumentViewSelectable object.

        Returns:
            DocumentViewSelectable instance
        """
        # TODO: Add validation
        return self._obj
