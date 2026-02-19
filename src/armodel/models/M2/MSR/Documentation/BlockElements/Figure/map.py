"""Map AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 305)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    area: Area
    class_: Optional[String]
    name: Optional[NameToken]
    onclick: Optional[String]
    ondblclick: Optional[String]
    onkeydown: Optional[String]
    onkeypress: Optional[String]
    onkeyup: Optional[String]
    onmousedown: Optional[String]
    onmousemove: Optional[String]
    onmouseout: Optional[String]
    onmouseover: Optional[String]
    onmouseup: Optional[String]
    title: Optional[String]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Map":
        """Deserialize XML element to Map object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Map object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse area
        child = ARObject._find_child_element(element, "AREA")
        if child is not None:
            area_value = ARObject._deserialize_by_tag(child, "Area")
            obj.area = area_value

        # Parse class_
        child = ARObject._find_child_element(element, "CLASS")
        if child is not None:
            class__value = child.text
            obj.class_ = class__value

        # Parse name
        child = ARObject._find_child_element(element, "NAME")
        if child is not None:
            name_value = child.text
            obj.name = name_value

        # Parse onclick
        child = ARObject._find_child_element(element, "ONCLICK")
        if child is not None:
            onclick_value = child.text
            obj.onclick = onclick_value

        # Parse ondblclick
        child = ARObject._find_child_element(element, "ONDBLCLICK")
        if child is not None:
            ondblclick_value = child.text
            obj.ondblclick = ondblclick_value

        # Parse onkeydown
        child = ARObject._find_child_element(element, "ONKEYDOWN")
        if child is not None:
            onkeydown_value = child.text
            obj.onkeydown = onkeydown_value

        # Parse onkeypress
        child = ARObject._find_child_element(element, "ONKEYPRESS")
        if child is not None:
            onkeypress_value = child.text
            obj.onkeypress = onkeypress_value

        # Parse onkeyup
        child = ARObject._find_child_element(element, "ONKEYUP")
        if child is not None:
            onkeyup_value = child.text
            obj.onkeyup = onkeyup_value

        # Parse onmousedown
        child = ARObject._find_child_element(element, "ONMOUSEDOWN")
        if child is not None:
            onmousedown_value = child.text
            obj.onmousedown = onmousedown_value

        # Parse onmousemove
        child = ARObject._find_child_element(element, "ONMOUSEMOVE")
        if child is not None:
            onmousemove_value = child.text
            obj.onmousemove = onmousemove_value

        # Parse onmouseout
        child = ARObject._find_child_element(element, "ONMOUSEOUT")
        if child is not None:
            onmouseout_value = child.text
            obj.onmouseout = onmouseout_value

        # Parse onmouseover
        child = ARObject._find_child_element(element, "ONMOUSEOVER")
        if child is not None:
            onmouseover_value = child.text
            obj.onmouseover = onmouseover_value

        # Parse onmouseup
        child = ARObject._find_child_element(element, "ONMOUSEUP")
        if child is not None:
            onmouseup_value = child.text
            obj.onmouseup = onmouseup_value

        # Parse title
        child = ARObject._find_child_element(element, "TITLE")
        if child is not None:
            title_value = child.text
            obj.title = title_value

        return obj



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
