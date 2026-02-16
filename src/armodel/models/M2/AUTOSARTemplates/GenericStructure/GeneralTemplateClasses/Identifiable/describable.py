"""Describable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Describable(ARObject):
    """AUTOSAR Describable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("admin_data", None, False, False, AdminData),  # adminData
        ("category", None, True, False, None),  # category
        ("desc", None, False, False, MultiLanguageOverviewParagraph),  # desc
        ("introduction", None, False, False, DocumentationBlock),  # introduction
    ]

    def __init__(self) -> None:
        """Initialize Describable."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.category: Optional[CategoryString] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.introduction: Optional[DocumentationBlock] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Describable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Describable":
        """Create Describable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Describable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Describable since parent returns ARObject
        return cast("Describable", obj)


class DescribableBuilder:
    """Builder for Describable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Describable = Describable()

    def build(self) -> Describable:
        """Build and return Describable object.

        Returns:
            Describable instance
        """
        # TODO: Add validation
        return self._obj
