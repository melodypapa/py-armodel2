"""Identifiable AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "admin_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AdminData,
        ),  # adminData
        "annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Annotation,
        ),  # annotations
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
        "uuid": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # uuid
    }

    def __init__(self) -> None:
        """Initialize Identifiable."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.annotations: list[Annotation] = []
        self.category: Optional[CategoryString] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.uuid: Optional[String] = None


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
