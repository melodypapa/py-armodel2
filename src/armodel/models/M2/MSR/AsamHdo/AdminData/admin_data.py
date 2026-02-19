"""AdminData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 288)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 969)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1994)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 72)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 84)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_AdminData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LEnum,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.doc_revision import (
    DocRevision,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_plain_text import (
    MultiLanguagePlainText,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class AdminData(ARObject):
    """AUTOSAR AdminData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    doc_revisions: list[DocRevision]
    language: Optional[LEnum]
    sdg: list[Sdg]
    used_languages: Optional[MultiLanguagePlainText]
    def __init__(self) -> None:
        """Initialize AdminData."""
        super().__init__()
        self.doc_revisions: list[DocRevision] = []
        self.language: Optional[LEnum] = None
        self.sdg: list[Sdg] = []
        self.used_languages: Optional[MultiLanguagePlainText] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AdminData":
        """Deserialize XML element to AdminData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AdminData object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse doc_revisions (list)
        obj.doc_revisions = []
        for child in ARObject._find_all_child_elements(element, "DOC-REVISIONS"):
            doc_revisions_value = ARObject._deserialize_by_tag(child, "DocRevision")
            obj.doc_revisions.append(doc_revisions_value)

        # Parse language
        child = ARObject._find_child_element(element, "LANGUAGE")
        if child is not None:
            language_value = child.text
            obj.language = language_value

        # Parse sdg (list)
        obj.sdg = []
        for child in ARObject._find_all_child_elements(element, "SDG"):
            sdg_value = ARObject._deserialize_by_tag(child, "Sdg")
            obj.sdg.append(sdg_value)

        # Parse used_languages
        child = ARObject._find_child_element(element, "USED-LANGUAGES")
        if child is not None:
            used_languages_value = ARObject._deserialize_by_tag(child, "MultiLanguagePlainText")
            obj.used_languages = used_languages_value

        return obj



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
