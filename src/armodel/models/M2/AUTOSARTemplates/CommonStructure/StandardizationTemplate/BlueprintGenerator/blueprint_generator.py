"""BlueprintGenerator AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class BlueprintGenerator(ARObject):
    """AUTOSAR BlueprintGenerator."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("expression", None, True, False, None),  # expression
        ("introduction", None, False, False, DocumentationBlock),  # introduction
    ]

    def __init__(self) -> None:
        """Initialize BlueprintGenerator."""
        super().__init__()
        self.expression: Optional[VerbatimString] = None
        self.introduction: Optional[DocumentationBlock] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BlueprintGenerator to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintGenerator":
        """Create BlueprintGenerator from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BlueprintGenerator instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BlueprintGenerator since parent returns ARObject
        return cast("BlueprintGenerator", obj)


class BlueprintGeneratorBuilder:
    """Builder for BlueprintGenerator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintGenerator = BlueprintGenerator()

    def build(self) -> BlueprintGenerator:
        """Build and return BlueprintGenerator object.

        Returns:
            BlueprintGenerator instance
        """
        # TODO: Add validation
        return self._obj
