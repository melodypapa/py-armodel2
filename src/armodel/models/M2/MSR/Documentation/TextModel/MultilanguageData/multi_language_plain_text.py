"""MultiLanguagePlainText AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_plain_text import (
    LPlainText,
)


class MultiLanguagePlainText(ARObject):
    """AUTOSAR MultiLanguagePlainText."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("l10", None, False, False, LPlainText),  # l10
    ]

    def __init__(self) -> None:
        """Initialize MultiLanguagePlainText."""
        super().__init__()
        self.l10: LPlainText = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultiLanguagePlainText to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguagePlainText":
        """Create MultiLanguagePlainText from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultiLanguagePlainText instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultiLanguagePlainText since parent returns ARObject
        return cast("MultiLanguagePlainText", obj)


class MultiLanguagePlainTextBuilder:
    """Builder for MultiLanguagePlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguagePlainText = MultiLanguagePlainText()

    def build(self) -> MultiLanguagePlainText:
        """Build and return MultiLanguagePlainText object.

        Returns:
            MultiLanguagePlainText instance
        """
        # TODO: Add validation
        return self._obj
