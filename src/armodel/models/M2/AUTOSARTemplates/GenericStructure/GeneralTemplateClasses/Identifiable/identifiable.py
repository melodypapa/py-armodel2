"""Identifiable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    String,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Identifiable(MultilanguageReferrable):
    """AUTOSAR Identifiable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("admin_data", None, False, False, AdminData),  # adminData
        ("annotations", None, False, True, Annotation),  # annotations
        ("category", None, True, False, None),  # category
        ("desc", None, False, False, MultiLanguageOverviewParagraph),  # desc
        ("introduction", None, False, False, DocumentationBlock),  # introduction
        ("uuid", None, True, False, None),  # uuid
    ]

    def __init__(self) -> None:
        """Initialize Identifiable."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.annotations: list[Annotation] = []
        self.category: Optional[CategoryString] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.uuid: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Identifiable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Identifiable":
        """Create Identifiable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Identifiable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Identifiable since parent returns ARObject
        return cast("Identifiable", obj)


class IdentifiableBuilder:
    """Builder for Identifiable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Identifiable = Identifiable()

    def build(self) -> Identifiable:
        """Build and return Identifiable object.

        Returns:
            Identifiable instance
        """
        # TODO: Add validation
        return self._obj
