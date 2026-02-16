"""SdgCaption AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class SdgCaption(MultilanguageReferrable):
    """AUTOSAR SdgCaption."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("desc", None, False, False, MultiLanguageOverviewParagraph),  # desc
    ]

    def __init__(self) -> None:
        """Initialize SdgCaption."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgCaption to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgCaption":
        """Create SdgCaption from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgCaption instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgCaption since parent returns ARObject
        return cast("SdgCaption", obj)


class SdgCaptionBuilder:
    """Builder for SdgCaption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgCaption = SdgCaption()

    def build(self) -> SdgCaption:
        """Build and return SdgCaption object.

        Returns:
            SdgCaption instance
        """
        # TODO: Add validation
        return self._obj
