"""MultiLanguageOverviewParagraph AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
    LOverviewParagraph,
)


class MultiLanguageOverviewParagraph(ARObject):
    """AUTOSAR MultiLanguageOverviewParagraph."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("l2", None, False, False, LOverviewParagraph),  # l2
    ]

    def __init__(self) -> None:
        """Initialize MultiLanguageOverviewParagraph."""
        super().__init__()
        self.l2: LOverviewParagraph = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultiLanguageOverviewParagraph to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageOverviewParagraph":
        """Create MultiLanguageOverviewParagraph from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultiLanguageOverviewParagraph instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultiLanguageOverviewParagraph since parent returns ARObject
        return cast("MultiLanguageOverviewParagraph", obj)


class MultiLanguageOverviewParagraphBuilder:
    """Builder for MultiLanguageOverviewParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguageOverviewParagraph = MultiLanguageOverviewParagraph()

    def build(self) -> MultiLanguageOverviewParagraph:
        """Build and return MultiLanguageOverviewParagraph object.

        Returns:
            MultiLanguageOverviewParagraph instance
        """
        # TODO: Add validation
        return self._obj
