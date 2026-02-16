"""Modification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Modification(ARObject):
    """AUTOSAR Modification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("change", None, False, False, MultiLanguageOverviewParagraph),  # change
        ("reason", None, False, False, MultiLanguageOverviewParagraph),  # reason
    ]

    def __init__(self) -> None:
        """Initialize Modification."""
        super().__init__()
        self.change: MultiLanguageOverviewParagraph = None
        self.reason: Optional[MultiLanguageOverviewParagraph] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Modification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Modification":
        """Create Modification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Modification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Modification since parent returns ARObject
        return cast("Modification", obj)


class ModificationBuilder:
    """Builder for Modification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Modification = Modification()

    def build(self) -> Modification:
        """Build and return Modification object.

        Returns:
            Modification instance
        """
        # TODO: Add validation
        return self._obj
