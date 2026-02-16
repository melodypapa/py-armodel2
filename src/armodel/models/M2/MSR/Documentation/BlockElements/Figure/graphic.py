"""Graphic AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class Graphic(EngineeringObject):
    """AUTOSAR Graphic."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("editfit", None, False, False, GraphicFitEnum),  # editfit
        ("edit_height", None, True, False, None),  # editHeight
        ("editscale", None, True, False, None),  # editscale
        ("edit_width", None, True, False, None),  # editWidth
        ("filename", None, True, False, None),  # filename
        ("fit", None, False, False, GraphicFitEnum),  # fit
        ("generator", None, True, False, None),  # generator
        ("height", None, True, False, None),  # height
        ("html_fit", None, False, False, GraphicFitEnum),  # htmlFit
        ("html_height", None, True, False, None),  # htmlHeight
        ("html_scale", None, True, False, None),  # htmlScale
        ("html_width", None, True, False, None),  # htmlWidth
        ("notation", None, False, False, GraphicNotationEnum),  # notation
        ("scale", None, True, False, None),  # scale
        ("width", None, True, False, None),  # width
    ]

    def __init__(self) -> None:
        """Initialize Graphic."""
        super().__init__()
        self.editfit: Optional[GraphicFitEnum] = None
        self.edit_height: Optional[String] = None
        self.editscale: Optional[String] = None
        self.edit_width: Optional[String] = None
        self.filename: Optional[String] = None
        self.fit: Optional[GraphicFitEnum] = None
        self.generator: Optional[NameToken] = None
        self.height: Optional[String] = None
        self.html_fit: Optional[GraphicFitEnum] = None
        self.html_height: Optional[String] = None
        self.html_scale: Optional[String] = None
        self.html_width: Optional[String] = None
        self.notation: Optional[GraphicNotationEnum] = None
        self.scale: Optional[String] = None
        self.width: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Graphic to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Graphic":
        """Create Graphic from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Graphic instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Graphic since parent returns ARObject
        return cast("Graphic", obj)


class GraphicBuilder:
    """Builder for Graphic."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Graphic = Graphic()

    def build(self) -> Graphic:
        """Build and return Graphic object.

        Returns:
            Graphic instance
        """
        # TODO: Add validation
        return self._obj
