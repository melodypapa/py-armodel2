"""LGraphic AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.graphic import (
    Graphic,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.map import (
    Map,
)


class LGraphic(LanguageSpecific):
    """AUTOSAR LGraphic."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("graphic", None, False, False, Graphic),  # graphic
        ("map", None, False, False, Map),  # map
    ]

    def __init__(self) -> None:
        """Initialize LGraphic."""
        super().__init__()
        self.graphic: Graphic = None
        self.map: Optional[Map] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LGraphic to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LGraphic":
        """Create LGraphic from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LGraphic instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LGraphic since parent returns ARObject
        return cast("LGraphic", obj)


class LGraphicBuilder:
    """Builder for LGraphic."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LGraphic = LGraphic()

    def build(self) -> LGraphic:
        """Build and return LGraphic object.

        Returns:
            LGraphic instance
        """
        # TODO: Add validation
        return self._obj
