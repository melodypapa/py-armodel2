"""Area AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 299)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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

    def serialize(self) -> ET.Element:
        """Serialize Area to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Area, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accesskey
        if self.accesskey is not None:
            serialized = SerializationHelper.serialize_item(self.accesskey, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESSKEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize alt
        if self.alt is not None:
            serialized = SerializationHelper.serialize_item(self.alt, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize class_
        if self.class_ is not None:
            serialized = SerializationHelper.serialize_item(self.class_, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize coords
        if self.coords is not None:
            serialized = SerializationHelper.serialize_item(self.coords, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COORDS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize href
        if self.href is not None:
            serialized = SerializationHelper.serialize_item(self.href, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nohref
        if self.nohref is not None:
            serialized = SerializationHelper.serialize_item(self.nohref, "AreaEnumNohref")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOHREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onblur
        if self.onblur is not None:
            serialized = SerializationHelper.serialize_item(self.onblur, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONBLUR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onclick
        if self.onclick is not None:
            serialized = SerializationHelper.serialize_item(self.onclick, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONCLICK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ondblclick
        if self.ondblclick is not None:
            serialized = SerializationHelper.serialize_item(self.ondblclick, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONDBLCLICK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onfocus
        if self.onfocus is not None:
            serialized = SerializationHelper.serialize_item(self.onfocus, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONFOCUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onkeydown
        if self.onkeydown is not None:
            serialized = SerializationHelper.serialize_item(self.onkeydown, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONKEYDOWN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onkeypress
        if self.onkeypress is not None:
            serialized = SerializationHelper.serialize_item(self.onkeypress, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONKEYPRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onkeyup
        if self.onkeyup is not None:
            serialized = SerializationHelper.serialize_item(self.onkeyup, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONKEYUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onmousedown
        if self.onmousedown is not None:
            serialized = SerializationHelper.serialize_item(self.onmousedown, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONMOUSEDOWN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onmousemove
        if self.onmousemove is not None:
            serialized = SerializationHelper.serialize_item(self.onmousemove, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONMOUSEMOVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onmouseout
        if self.onmouseout is not None:
            serialized = SerializationHelper.serialize_item(self.onmouseout, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONMOUSEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onmouseover
        if self.onmouseover is not None:
            serialized = SerializationHelper.serialize_item(self.onmouseover, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONMOUSEOVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize onmouseup
        if self.onmouseup is not None:
            serialized = SerializationHelper.serialize_item(self.onmouseup, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONMOUSEUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize shape
        if self.shape is not None:
            serialized = SerializationHelper.serialize_item(self.shape, "AreaEnumShape")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHAPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize style
        if self.style is not None:
            serialized = SerializationHelper.serialize_item(self.style, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STYLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tabindex
        if self.tabindex is not None:
            serialized = SerializationHelper.serialize_item(self.tabindex, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TABINDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize title
        if self.title is not None:
            serialized = SerializationHelper.serialize_item(self.title, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TITLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Area":
        """Deserialize XML element to Area object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Area object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Area, cls).deserialize(element)

        # Parse accesskey
        child = SerializationHelper.find_child_element(element, "ACCESSKEY")
        if child is not None:
            accesskey_value = child.text
            obj.accesskey = accesskey_value

        # Parse alt
        child = SerializationHelper.find_child_element(element, "ALT")
        if child is not None:
            alt_value = child.text
            obj.alt = alt_value

        # Parse class_
        child = SerializationHelper.find_child_element(element, "CLASS")
        if child is not None:
            class__value = child.text
            obj.class_ = class__value

        # Parse coords
        child = SerializationHelper.find_child_element(element, "COORDS")
        if child is not None:
            coords_value = child.text
            obj.coords = coords_value

        # Parse href
        child = SerializationHelper.find_child_element(element, "HREF")
        if child is not None:
            href_value = child.text
            obj.href = href_value

        # Parse nohref
        child = SerializationHelper.find_child_element(element, "NOHREF")
        if child is not None:
            nohref_value = AreaEnumNohref.deserialize(child)
            obj.nohref = nohref_value

        # Parse onblur
        child = SerializationHelper.find_child_element(element, "ONBLUR")
        if child is not None:
            onblur_value = child.text
            obj.onblur = onblur_value

        # Parse onclick
        child = SerializationHelper.find_child_element(element, "ONCLICK")
        if child is not None:
            onclick_value = child.text
            obj.onclick = onclick_value

        # Parse ondblclick
        child = SerializationHelper.find_child_element(element, "ONDBLCLICK")
        if child is not None:
            ondblclick_value = child.text
            obj.ondblclick = ondblclick_value

        # Parse onfocus
        child = SerializationHelper.find_child_element(element, "ONFOCUS")
        if child is not None:
            onfocus_value = child.text
            obj.onfocus = onfocus_value

        # Parse onkeydown
        child = SerializationHelper.find_child_element(element, "ONKEYDOWN")
        if child is not None:
            onkeydown_value = child.text
            obj.onkeydown = onkeydown_value

        # Parse onkeypress
        child = SerializationHelper.find_child_element(element, "ONKEYPRESS")
        if child is not None:
            onkeypress_value = child.text
            obj.onkeypress = onkeypress_value

        # Parse onkeyup
        child = SerializationHelper.find_child_element(element, "ONKEYUP")
        if child is not None:
            onkeyup_value = child.text
            obj.onkeyup = onkeyup_value

        # Parse onmousedown
        child = SerializationHelper.find_child_element(element, "ONMOUSEDOWN")
        if child is not None:
            onmousedown_value = child.text
            obj.onmousedown = onmousedown_value

        # Parse onmousemove
        child = SerializationHelper.find_child_element(element, "ONMOUSEMOVE")
        if child is not None:
            onmousemove_value = child.text
            obj.onmousemove = onmousemove_value

        # Parse onmouseout
        child = SerializationHelper.find_child_element(element, "ONMOUSEOUT")
        if child is not None:
            onmouseout_value = child.text
            obj.onmouseout = onmouseout_value

        # Parse onmouseover
        child = SerializationHelper.find_child_element(element, "ONMOUSEOVER")
        if child is not None:
            onmouseover_value = child.text
            obj.onmouseover = onmouseover_value

        # Parse onmouseup
        child = SerializationHelper.find_child_element(element, "ONMOUSEUP")
        if child is not None:
            onmouseup_value = child.text
            obj.onmouseup = onmouseup_value

        # Parse shape
        child = SerializationHelper.find_child_element(element, "SHAPE")
        if child is not None:
            shape_value = AreaEnumShape.deserialize(child)
            obj.shape = shape_value

        # Parse style
        child = SerializationHelper.find_child_element(element, "STYLE")
        if child is not None:
            style_value = child.text
            obj.style = style_value

        # Parse tabindex
        child = SerializationHelper.find_child_element(element, "TABINDEX")
        if child is not None:
            tabindex_value = child.text
            obj.tabindex = tabindex_value

        # Parse title
        child = SerializationHelper.find_child_element(element, "TITLE")
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
