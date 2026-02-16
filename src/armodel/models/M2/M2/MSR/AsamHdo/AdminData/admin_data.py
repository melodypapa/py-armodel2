"""AdminData AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.AdminData.doc_revision import (
    DocRevision,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_plain_text import (
    MultiLanguagePlainText,
)


class AdminData(ARObject):
    """AUTOSAR AdminData."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "doc_revisions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DocRevision,
        ),  # docRevisions
        "used_languages": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultiLanguagePlainText,
        ),  # usedLanguages
    }

    def __init__(self) -> None:
        """Initialize AdminData."""
        super().__init__()
        self.doc_revisions: list[DocRevision] = []
        self.used_languages: Optional[MultiLanguagePlainText] = None


class AdminDataBuilder:
    """Builder for AdminData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AdminData = AdminData()

    def build(self) -> AdminData:
        """Build and return AdminData object.

        Returns:
            AdminData instance
        """
        # TODO: Add validation
        return self._obj
