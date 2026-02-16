"""EmphasisText AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    Superscript,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)


class EmphasisText(ARObject):
    """AUTOSAR EmphasisText."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("color", None, True, False, None),  # color
        ("font", None, False, False, EEnumFont),  # font
        ("sub", None, True, False, None),  # sub
        ("sup", None, True, False, None),  # sup
        ("tt", None, False, False, Tt),  # tt
        ("type", None, False, False, EEnum),  # type
    ]

    def __init__(self) -> None:
        """Initialize EmphasisText."""
        super().__init__()
        self.color: Optional[String] = None
        self.font: Optional[EEnumFont] = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.tt: Optional[Tt] = None
        self.type: Optional[EEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EmphasisText to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EmphasisText":
        """Create EmphasisText from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EmphasisText instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EmphasisText since parent returns ARObject
        return cast("EmphasisText", obj)


class EmphasisTextBuilder:
    """Builder for EmphasisText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EmphasisText = EmphasisText()

    def build(self) -> EmphasisText:
        """Build and return EmphasisText object.

        Returns:
            EmphasisText instance
        """
        # TODO: Add validation
        return self._obj
