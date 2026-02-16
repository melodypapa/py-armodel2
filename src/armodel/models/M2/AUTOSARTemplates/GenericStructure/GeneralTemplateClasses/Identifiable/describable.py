"""Describable AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "admin_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AdminData,
        ),  # adminData
        "category": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # category
        "desc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultiLanguageOverviewParagraph,
        ),  # desc
        "introduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # introduction
    }

    def __init__(self) -> None:
        """Initialize Describable."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.category: Optional[CategoryString] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.introduction: Optional[DocumentationBlock] = None


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
