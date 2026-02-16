"""LOverviewParagraph AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class LOverviewParagraph(ARObject):
    """AUTOSAR LOverviewParagraph."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("blueprint_value", None, True, False, None),  # blueprintValue
    ]

    def __init__(self) -> None:
        """Initialize LOverviewParagraph."""
        super().__init__()
        self.blueprint_value: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LOverviewParagraph to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LOverviewParagraph":
        """Create LOverviewParagraph from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LOverviewParagraph instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LOverviewParagraph since parent returns ARObject
        return cast("LOverviewParagraph", obj)


class LOverviewParagraphBuilder:
    """Builder for LOverviewParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LOverviewParagraph = LOverviewParagraph()

    def build(self) -> LOverviewParagraph:
        """Build and return LOverviewParagraph object.

        Returns:
            LOverviewParagraph instance
        """
        # TODO: Add validation
        return self._obj
