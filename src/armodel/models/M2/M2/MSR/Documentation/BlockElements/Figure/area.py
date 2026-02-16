"""Area AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Area(ARObject):
    """AUTOSAR Area."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "accesskey": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # accesskey
        "alt": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # alt
        "class_": XMLMember(
            xml_tag='CLASS',
            is_attribute=True,
            multiplicity="0..1",
            xml_name_override='CLASS',
        ),  # class
        "coords": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # coords
        "href": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # href
        "nohref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AreaEnumNohref,
        ),  # nohref
        "onblur": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onblur
        "onclick": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onclick
        "ondblclick": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ondblclick
        "onfocus": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onfocus
        "onkeydown": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onkeydown
        "onkeypress": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onkeypress
        "onkeyup": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onkeyup
        "onmousedown": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onmousedown
        "onmousemove": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onmousemove
        "onmouseout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onmouseout
        "onmouseover": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onmouseover
        "onmouseup": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onmouseup
        "shape": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AreaEnumShape,
        ),  # shape
        "style": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # style
        "tabindex": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tabindex
        "title": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # title
    }

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
