"""Documentation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation_context import (
    DocumentationContext,
)
from armodel.models.M2.MSR.Documentation.Chapters.predefined_chapter import (
    PredefinedChapter,
)


class Documentation(ARElement):
    """AUTOSAR Documentation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "contexts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DocumentationContext,
        ),  # contexts
        "documentation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PredefinedChapter,
        ),  # documentation
    }

    def __init__(self) -> None:
        """Initialize Documentation."""
        super().__init__()
        self.contexts: list[DocumentationContext] = []
        self.documentation: Optional[PredefinedChapter] = None


class DocumentationBuilder:
    """Builder for Documentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Documentation = Documentation()

    def build(self) -> Documentation:
        """Build and return Documentation object.

        Returns:
            Documentation instance
        """
        # TODO: Add validation
        return self._obj
