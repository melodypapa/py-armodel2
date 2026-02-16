"""AdminData AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("doc_revisions", None, False, True, DocRevision),  # docRevisions
        ("used_languages", None, False, False, MultiLanguagePlainText),  # usedLanguages
    ]

    def __init__(self) -> None:
        """Initialize AdminData."""
        super().__init__()
        self.doc_revisions: list[DocRevision] = []
        self.used_languages: Optional[MultiLanguagePlainText] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AdminData to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AdminData":
        """Create AdminData from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AdminData instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AdminData since parent returns ARObject
        return cast("AdminData", obj)


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
