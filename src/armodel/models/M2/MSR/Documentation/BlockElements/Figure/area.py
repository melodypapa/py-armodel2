"""Area AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 299)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import (
    AreaEnumNohref,
    AreaEnumShape,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Area(ARObject):
    """AUTOSAR Area."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accesskey: Optional[String]
    alt: Optional[String]
    class_: Optional[String]
    coords: Optional[String]
    href: Optional[String]
    nohref: Optional[AreaEnumNohref]
    onblur: Optional[String]
    onclick: Optional[String]
    ondblclick: Optional[String]
    onfocus: Optional[String]
    onkeydown: Optional[String]
    onkeypress: Optional[String]
    onkeyup: Optional[String]
    onmousedown: Optional[String]
    onmousemove: Optional[String]
    onmouseout: Optional[String]
    onmouseover: Optional[String]
    onmouseup: Optional[String]
    shape: Optional[AreaEnumShape]
    style: Optional[String]
    tabindex: Optional[String]
    title: Optional[String]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Area":
        """Deserialize XML element to Area object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Area object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse accesskey
        child = ARObject._find_child_element(element, "ACCESSKEY")
        if child is not None:
            accesskey_value = child.text
            obj.accesskey = accesskey_value

        # Parse alt
        child = ARObject._find_child_element(element, "ALT")
        if child is not None:
            alt_value = child.text
            obj.alt = alt_value

        # Parse class_
        child = ARObject._find_child_element(element, "CLASS")
        if child is not None:
            class__value = child.text
            obj.class_ = class__value

        # Parse coords
        child = ARObject._find_child_element(element, "COORDS")
        if child is not None:
            coords_value = child.text
            obj.coords = coords_value

        # Parse href
        child = ARObject._find_child_element(element, "HREF")
        if child is not None:
            href_value = child.text
            obj.href = href_value

        # Parse nohref
        child = ARObject._find_child_element(element, "NOHREF")
        if child is not None:
            nohref_value = AreaEnumNohref.deserialize(child)
            obj.nohref = nohref_value

        # Parse onblur
        child = ARObject._find_child_element(element, "ONBLUR")
        if child is not None:
            onblur_value = child.text
            obj.onblur = onblur_value

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

        # Parse onfocus
        child = ARObject._find_child_element(element, "ONFOCUS")
        if child is not None:
            onfocus_value = child.text
            obj.onfocus = onfocus_value

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

        # Parse shape
        child = ARObject._find_child_element(element, "SHAPE")
        if child is not None:
            shape_value = AreaEnumShape.deserialize(child)
            obj.shape = shape_value

        # Parse style
        child = ARObject._find_child_element(element, "STYLE")
        if child is not None:
            style_value = child.text
            obj.style = style_value

        # Parse tabindex
        child = ARObject._find_child_element(element, "TABINDEX")
        if child is not None:
            tabindex_value = child.text
            obj.tabindex = tabindex_value

        # Parse title
        child = ARObject._find_child_element(element, "TITLE")
        if child is not None:
            title_value = child.text
            obj.title = title_value

        return obj



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
