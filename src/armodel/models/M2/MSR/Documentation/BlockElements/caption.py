"""Caption AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Caption(MultilanguageReferrable):
    """AUTOSAR Caption."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("desc", None, False, False, MultiLanguageOverviewParagraph),  # desc
    ]

    def __init__(self) -> None:
        """Initialize Caption."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Caption to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Caption":
        """Create Caption from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Caption instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Caption since parent returns ARObject
        return cast("Caption", obj)


class CaptionBuilder:
    """Builder for Caption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Caption = Caption()

    def build(self) -> Caption:
        """Build and return Caption object.

        Returns:
            Caption instance
        """
        # TODO: Add validation
        return self._obj
