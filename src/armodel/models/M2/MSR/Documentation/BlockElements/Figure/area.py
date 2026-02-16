"""Area AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Area(ARObject):
    """AUTOSAR Area."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accesskey", None, True, False, None),  # accesskey
        ("alt", None, True, False, None),  # alt
        ("class_", 'CLASS', True, False, None),  # class
        ("coords", None, True, False, None),  # coords
        ("href", None, True, False, None),  # href
        ("nohref", None, False, False, AreaEnumNohref),  # nohref
        ("onblur", None, True, False, None),  # onblur
        ("onclick", None, True, False, None),  # onclick
        ("ondblclick", None, True, False, None),  # ondblclick
        ("onfocus", None, True, False, None),  # onfocus
        ("onkeydown", None, True, False, None),  # onkeydown
        ("onkeypress", None, True, False, None),  # onkeypress
        ("onkeyup", None, True, False, None),  # onkeyup
        ("onmousedown", None, True, False, None),  # onmousedown
        ("onmousemove", None, True, False, None),  # onmousemove
        ("onmouseout", None, True, False, None),  # onmouseout
        ("onmouseover", None, True, False, None),  # onmouseover
        ("onmouseup", None, True, False, None),  # onmouseup
        ("shape", None, False, False, AreaEnumShape),  # shape
        ("style", None, True, False, None),  # style
        ("tabindex", None, True, False, None),  # tabindex
        ("title", None, True, False, None),  # title
    ]

    def __init__(self) -> None:
        """Initialize Area."""
        super().__init__()
        self.accesskey: Optional[String] = None
        self.alt: Optional[String] = None
        self.class_: Optional[String] = None
        self.coords: Optional[String] = None
        self.href: Optional[String] = None
        self.nohref: Optional[AreaEnumNohref] = None
        self.onblur: Optional[String] = None
        self.onclick: Optional[String] = None
        self.ondblclick: Optional[String] = None
        self.onfocus: Optional[String] = None
        self.onkeydown: Optional[String] = None
        self.onkeypress: Optional[String] = None
        self.onkeyup: Optional[String] = None
        self.onmousedown: Optional[String] = None
        self.onmousemove: Optional[String] = None
        self.onmouseout: Optional[String] = None
        self.onmouseover: Optional[String] = None
        self.onmouseup: Optional[String] = None
        self.shape: Optional[AreaEnumShape] = None
        self.style: Optional[String] = None
        self.tabindex: Optional[String] = None
        self.title: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Area to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Area":
        """Create Area from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Area instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Area since parent returns ARObject
        return cast("Area", obj)


class AreaBuilder:
    """Builder for Area."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Area = Area()

    def build(self) -> Area:
        """Build and return Area object.

        Returns:
            Area instance
        """
        # TODO: Add validation
        return self._obj
