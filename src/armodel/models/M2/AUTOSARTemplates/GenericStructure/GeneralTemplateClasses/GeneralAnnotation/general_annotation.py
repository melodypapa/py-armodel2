"""GeneralAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class GeneralAnnotation(ARObject):
    """AUTOSAR GeneralAnnotation."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("annotation", None, True, False, None),  # annotation
        ("annotation_text", None, False, False, DocumentationBlock),  # annotationText
        ("label", None, False, False, MultilanguageLongName),  # label
    ]

    def __init__(self) -> None:
        """Initialize GeneralAnnotation."""
        super().__init__()
        self.annotation: String = None
        self.annotation_text: DocumentationBlock = None
        self.label: Optional[MultilanguageLongName] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GeneralAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GeneralAnnotation":
        """Create GeneralAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GeneralAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GeneralAnnotation since parent returns ARObject
        return cast("GeneralAnnotation", obj)


class GeneralAnnotationBuilder:
    """Builder for GeneralAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralAnnotation = GeneralAnnotation()

    def build(self) -> GeneralAnnotation:
        """Build and return GeneralAnnotation object.

        Returns:
            GeneralAnnotation instance
        """
        # TODO: Add validation
        return self._obj
