"""Tt AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 318)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class Tt(ARObject):
    """AUTOSAR Tt."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    term: String
    tex_render: Optional[String]
    type: NameToken
    def __init__(self) -> None:
        """Initialize Tt."""
        super().__init__()
        self.term: String = None
        self.tex_render: Optional[String] = None
        self.type: NameToken = None

    def serialize(self) -> ET.Element:
        """Serialize Tt to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize term
        if self.term is not None:
            serialized = SerializationHelper.serialize_item(self.term, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TERM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tex_render
        if self.tex_render is not None:
            serialized = SerializationHelper.serialize_item(self.tex_render, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEX-RENDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type
        if self.type is not None:
            serialized = SerializationHelper.serialize_item(self.type, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tt":
        """Deserialize XML element to Tt object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Tt object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse term
        child = SerializationHelper.find_child_element(element, "TERM")
        if child is not None:
            term_value = child.text
            obj.term = term_value

        # Parse tex_render
        child = SerializationHelper.find_child_element(element, "TEX-RENDER")
        if child is not None:
            tex_render_value = child.text
            obj.tex_render = tex_render_value

        # Parse type
        child = SerializationHelper.find_child_element(element, "TYPE")
        if child is not None:
            type_value = child.text
            obj.type = type_value

        return obj



class TtBuilder:
    """Builder for Tt."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Tt = Tt()

    def build(self) -> Tt:
        """Build and return Tt object.

        Returns:
            Tt instance
        """
        # TODO: Add validation
        return self._obj
