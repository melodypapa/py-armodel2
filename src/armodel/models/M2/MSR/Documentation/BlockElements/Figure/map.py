"""Map AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 305)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.area import (
    Area,
)


class Map(ARObject):
    """AUTOSAR Map."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "area": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Area,
        ),  # area
        "class_": XMLMember(
            xml_tag='CLASS',
            is_attribute=True,
            multiplicity="0..1",
            xml_name_override='CLASS',
        ),  # class
        "name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # name
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
        "title": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # title
    }

    def __init__(self) -> None:
        """Initialize Map."""
        super().__init__()
        self.area: Area = None
        self.class_: Optional[String] = None
        self.name: Optional[NameToken] = None
        self.onclick: Optional[String] = None
        self.ondblclick: Optional[String] = None
        self.onkeydown: Optional[String] = None
        self.onkeypress: Optional[String] = None
        self.onkeyup: Optional[String] = None
        self.onmousedown: Optional[String] = None
        self.onmousemove: Optional[String] = None
        self.onmouseout: Optional[String] = None
        self.onmouseover: Optional[String] = None
        self.onmouseup: Optional[String] = None
        self.title: Optional[String] = None


class MapBuilder:
    """Builder for Map."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Map = Map()

    def build(self) -> Map:
        """Build and return Map object.

        Returns:
            Map instance
        """
        # TODO: Add validation
        return self._obj
