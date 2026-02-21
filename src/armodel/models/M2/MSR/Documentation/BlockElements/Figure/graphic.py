"""Graphic AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 302)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_attribute

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import (
    GraphicFitEnum,
    GraphicNotationEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class Graphic(EngineeringObject):
    """AUTOSAR Graphic."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    editfit: Optional[GraphicFitEnum]
    edit_height: Optional[String]
    editscale: Optional[String]
    edit_width: Optional[String]
    _filename: Optional[String]
    fit: Optional[GraphicFitEnum]
    generator: Optional[NameToken]
    height: Optional[String]
    html_fit: Optional[GraphicFitEnum]
    html_height: Optional[String]
    html_scale: Optional[String]
    html_width: Optional[String]
    notation: Optional[GraphicNotationEnum]
    scale: Optional[String]
    width: Optional[String]
    def __init__(self) -> None:
        """Initialize Graphic."""
        super().__init__()
        self.editfit: Optional[GraphicFitEnum] = None
        self.edit_height: Optional[String] = None
        self.editscale: Optional[String] = None
        self.edit_width: Optional[String] = None
        self._filename: Optional[String] = None
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
    @property
    @xml_attribute
    def filename(self) -> String:
        """Get filename XML attribute."""
        return self._filename

    @filename.setter
    def filename(self, value: String) -> None:
        """Set filename XML attribute."""
        self._filename = value


    def serialize(self) -> ET.Element:
        """Serialize Graphic to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Graphic, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize editfit
        if self.editfit is not None:
            serialized = SerializationHelper.serialize_item(self.editfit, "GraphicFitEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EDITFIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize edit_height
        if self.edit_height is not None:
            serialized = SerializationHelper.serialize_item(self.edit_height, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EDIT-HEIGHT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize editscale
        if self.editscale is not None:
            serialized = SerializationHelper.serialize_item(self.editscale, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EDITSCALE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize edit_width
        if self.edit_width is not None:
            serialized = SerializationHelper.serialize_item(self.edit_width, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EDIT-WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filename as XML attribute
        if self.filename is not None:
            elem.attrib["FILENAME"] = str(self.filename)

        # Serialize fit
        if self.fit is not None:
            serialized = SerializationHelper.serialize_item(self.fit, "GraphicFitEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize generator
        if self.generator is not None:
            serialized = SerializationHelper.serialize_item(self.generator, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GENERATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize height
        if self.height is not None:
            serialized = SerializationHelper.serialize_item(self.height, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEIGHT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize html_fit
        if self.html_fit is not None:
            serialized = SerializationHelper.serialize_item(self.html_fit, "GraphicFitEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HTML-FIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize html_height
        if self.html_height is not None:
            serialized = SerializationHelper.serialize_item(self.html_height, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HTML-HEIGHT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize html_scale
        if self.html_scale is not None:
            serialized = SerializationHelper.serialize_item(self.html_scale, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HTML-SCALE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize html_width
        if self.html_width is not None:
            serialized = SerializationHelper.serialize_item(self.html_width, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HTML-WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize notation
        if self.notation is not None:
            serialized = SerializationHelper.serialize_item(self.notation, "GraphicNotationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scale
        if self.scale is not None:
            serialized = SerializationHelper.serialize_item(self.scale, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCALE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize width
        if self.width is not None:
            serialized = SerializationHelper.serialize_item(self.width, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Graphic":
        """Deserialize XML element to Graphic object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Graphic object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Graphic, cls).deserialize(element)

        # Parse editfit
        child = SerializationHelper.find_child_element(element, "EDITFIT")
        if child is not None:
            editfit_value = GraphicFitEnum.deserialize(child)
            obj.editfit = editfit_value

        # Parse edit_height
        child = SerializationHelper.find_child_element(element, "EDIT-HEIGHT")
        if child is not None:
            edit_height_value = child.text
            obj.edit_height = edit_height_value

        # Parse editscale
        child = SerializationHelper.find_child_element(element, "EDITSCALE")
        if child is not None:
            editscale_value = child.text
            obj.editscale = editscale_value

        # Parse edit_width
        child = SerializationHelper.find_child_element(element, "EDIT-WIDTH")
        if child is not None:
            edit_width_value = child.text
            obj.edit_width = edit_width_value

        # Parse filename from XML attribute
        if "FILENAME" in element.attrib:
            filename_value = element.attrib["FILENAME"]
            obj.filename = filename_value

        # Parse fit
        child = SerializationHelper.find_child_element(element, "FIT")
        if child is not None:
            fit_value = GraphicFitEnum.deserialize(child)
            obj.fit = fit_value

        # Parse generator
        child = SerializationHelper.find_child_element(element, "GENERATOR")
        if child is not None:
            generator_value = child.text
            obj.generator = generator_value

        # Parse height
        child = SerializationHelper.find_child_element(element, "HEIGHT")
        if child is not None:
            height_value = child.text
            obj.height = height_value

        # Parse html_fit
        child = SerializationHelper.find_child_element(element, "HTML-FIT")
        if child is not None:
            html_fit_value = GraphicFitEnum.deserialize(child)
            obj.html_fit = html_fit_value

        # Parse html_height
        child = SerializationHelper.find_child_element(element, "HTML-HEIGHT")
        if child is not None:
            html_height_value = child.text
            obj.html_height = html_height_value

        # Parse html_scale
        child = SerializationHelper.find_child_element(element, "HTML-SCALE")
        if child is not None:
            html_scale_value = child.text
            obj.html_scale = html_scale_value

        # Parse html_width
        child = SerializationHelper.find_child_element(element, "HTML-WIDTH")
        if child is not None:
            html_width_value = child.text
            obj.html_width = html_width_value

        # Parse notation
        child = SerializationHelper.find_child_element(element, "NOTATION")
        if child is not None:
            notation_value = GraphicNotationEnum.deserialize(child)
            obj.notation = notation_value

        # Parse scale
        child = SerializationHelper.find_child_element(element, "SCALE")
        if child is not None:
            scale_value = child.text
            obj.scale = scale_value

        # Parse width
        child = SerializationHelper.find_child_element(element, "WIDTH")
        if child is not None:
            width_value = child.text
            obj.width = width_value

        return obj



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
