"""Area AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 299)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.Figure import (
    AreaEnumNohref,
    AreaEnumShape,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Area(ARObject):
    """AUTOSAR Area."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "AREA"


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
    _DESERIALIZE_DISPATCH = {
        "ACCESSKEY": lambda obj, elem: setattr(obj, "accesskey", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ALT": lambda obj, elem: setattr(obj, "alt", SerializationHelper.deserialize_by_tag(elem, "String")),
        "CLASS": lambda obj, elem: setattr(obj, "class_", SerializationHelper.deserialize_by_tag(elem, "String")),
        "COORDS": lambda obj, elem: setattr(obj, "coords", SerializationHelper.deserialize_by_tag(elem, "String")),
        "HREF": lambda obj, elem: setattr(obj, "href", SerializationHelper.deserialize_by_tag(elem, "String")),
        "NOHREF": lambda obj, elem: setattr(obj, "nohref", AreaEnumNohref.deserialize(elem)),
        "ONBLUR": lambda obj, elem: setattr(obj, "onblur", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONCLICK": lambda obj, elem: setattr(obj, "onclick", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONDBLCLICK": lambda obj, elem: setattr(obj, "ondblclick", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONFOCUS": lambda obj, elem: setattr(obj, "onfocus", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONKEYDOWN": lambda obj, elem: setattr(obj, "onkeydown", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONKEYPRESS": lambda obj, elem: setattr(obj, "onkeypress", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONKEYUP": lambda obj, elem: setattr(obj, "onkeyup", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONMOUSEDOWN": lambda obj, elem: setattr(obj, "onmousedown", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONMOUSEMOVE": lambda obj, elem: setattr(obj, "onmousemove", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONMOUSEOUT": lambda obj, elem: setattr(obj, "onmouseout", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONMOUSEOVER": lambda obj, elem: setattr(obj, "onmouseover", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ONMOUSEUP": lambda obj, elem: setattr(obj, "onmouseup", SerializationHelper.deserialize_by_tag(elem, "String")),
        "SHAPE": lambda obj, elem: setattr(obj, "shape", AreaEnumShape.deserialize(elem)),
        "STYLE": lambda obj, elem: setattr(obj, "style", SerializationHelper.deserialize_by_tag(elem, "String")),
        "TABINDEX": lambda obj, elem: setattr(obj, "tabindex", SerializationHelper.deserialize_by_tag(elem, "String")),
        "TITLE": lambda obj, elem: setattr(obj, "title", SerializationHelper.deserialize_by_tag(elem, "String")),
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

    def serialize(self) -> ET.Element:
        """Serialize Area to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ACCESSKEY":
                setattr(obj, "accesskey", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ALT":
                setattr(obj, "alt", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "CLASS":
                setattr(obj, "class_", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "COORDS":
                setattr(obj, "coords", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "HREF":
                setattr(obj, "href", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "NOHREF":
                setattr(obj, "nohref", AreaEnumNohref.deserialize(child))
            elif tag == "ONBLUR":
                setattr(obj, "onblur", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONCLICK":
                setattr(obj, "onclick", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONDBLCLICK":
                setattr(obj, "ondblclick", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONFOCUS":
                setattr(obj, "onfocus", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONKEYDOWN":
                setattr(obj, "onkeydown", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONKEYPRESS":
                setattr(obj, "onkeypress", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONKEYUP":
                setattr(obj, "onkeyup", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONMOUSEDOWN":
                setattr(obj, "onmousedown", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONMOUSEMOVE":
                setattr(obj, "onmousemove", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONMOUSEOUT":
                setattr(obj, "onmouseout", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONMOUSEOVER":
                setattr(obj, "onmouseover", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ONMOUSEUP":
                setattr(obj, "onmouseup", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "SHAPE":
                setattr(obj, "shape", AreaEnumShape.deserialize(child))
            elif tag == "STYLE":
                setattr(obj, "style", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "TABINDEX":
                setattr(obj, "tabindex", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "TITLE":
                setattr(obj, "title", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class AreaBuilder(BuilderBase):
    """Builder for Area with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Area = Area()


    def with_accesskey(self, value: Optional[String]) -> "AreaBuilder":
        """Set accesskey attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accesskey = value
        return self

    def with_alt(self, value: Optional[String]) -> "AreaBuilder":
        """Set alt attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alt = value
        return self

    def with_class(self, value: Optional[String]) -> "AreaBuilder":
        """Set class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        setattr(self._obj, 'class', value)
        return self

    def with_coords(self, value: Optional[String]) -> "AreaBuilder":
        """Set coords attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.coords = value
        return self

    def with_href(self, value: Optional[String]) -> "AreaBuilder":
        """Set href attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.href = value
        return self

    def with_nohref(self, value: Optional[AreaEnumNohref]) -> "AreaBuilder":
        """Set nohref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nohref = value
        return self

    def with_onblur(self, value: Optional[String]) -> "AreaBuilder":
        """Set onblur attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onblur = value
        return self

    def with_onclick(self, value: Optional[String]) -> "AreaBuilder":
        """Set onclick attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onclick = value
        return self

    def with_ondblclick(self, value: Optional[String]) -> "AreaBuilder":
        """Set ondblclick attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ondblclick = value
        return self

    def with_onfocus(self, value: Optional[String]) -> "AreaBuilder":
        """Set onfocus attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onfocus = value
        return self

    def with_onkeydown(self, value: Optional[String]) -> "AreaBuilder":
        """Set onkeydown attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onkeydown = value
        return self

    def with_onkeypress(self, value: Optional[String]) -> "AreaBuilder":
        """Set onkeypress attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onkeypress = value
        return self

    def with_onkeyup(self, value: Optional[String]) -> "AreaBuilder":
        """Set onkeyup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onkeyup = value
        return self

    def with_onmousedown(self, value: Optional[String]) -> "AreaBuilder":
        """Set onmousedown attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onmousedown = value
        return self

    def with_onmousemove(self, value: Optional[String]) -> "AreaBuilder":
        """Set onmousemove attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onmousemove = value
        return self

    def with_onmouseout(self, value: Optional[String]) -> "AreaBuilder":
        """Set onmouseout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onmouseout = value
        return self

    def with_onmouseover(self, value: Optional[String]) -> "AreaBuilder":
        """Set onmouseover attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onmouseover = value
        return self

    def with_onmouseup(self, value: Optional[String]) -> "AreaBuilder":
        """Set onmouseup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.onmouseup = value
        return self

    def with_shape(self, value: Optional[AreaEnumShape]) -> "AreaBuilder":
        """Set shape attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.shape = value
        return self

    def with_style(self, value: Optional[String]) -> "AreaBuilder":
        """Set style attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.style = value
        return self

    def with_tabindex(self, value: Optional[String]) -> "AreaBuilder":
        """Set tabindex attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tabindex = value
        return self

    def with_title(self, value: Optional[String]) -> "AreaBuilder":
        """Set title attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.title = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> Area:
        """Build and return the Area instance with validation."""
        self._validate_instance()
        pass
        return self._obj