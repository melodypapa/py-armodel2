"""Documentation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("contexts", None, False, True, DocumentationContext),  # contexts
        ("documentation", None, False, False, PredefinedChapter),  # documentation
    ]

    def __init__(self) -> None:
        """Initialize Documentation."""
        super().__init__()
        self.contexts: list[DocumentationContext] = []
        self.documentation: Optional[PredefinedChapter] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Documentation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Documentation":
        """Create Documentation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Documentation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Documentation since parent returns ARObject
        return cast("Documentation", obj)


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
