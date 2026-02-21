"""LGraphic AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 307)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.graphic import (
    Graphic,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.map import (
    Map,
)


class LGraphic(LanguageSpecific):
    """AUTOSAR LGraphic."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    graphic: Graphic
    map: Optional[Map]
    def __init__(self) -> None:
        """Initialize LGraphic."""
        super().__init__()
        self.graphic: Graphic = None
        self.map: Optional[Map] = None

    def serialize(self) -> ET.Element:
        """Serialize LGraphic to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LGraphic, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize graphic
        if self.graphic is not None:
            serialized = SerializationHelper.serialize_item(self.graphic, "Graphic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GRAPHIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize map
        if self.map is not None:
            serialized = SerializationHelper.serialize_item(self.map, "Map")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LGraphic":
        """Deserialize XML element to LGraphic object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LGraphic object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LGraphic, cls).deserialize(element)

        # Parse graphic
        child = SerializationHelper.find_child_element(element, "GRAPHIC")
        if child is not None:
            graphic_value = SerializationHelper.deserialize_by_tag(child, "Graphic")
            obj.graphic = graphic_value

        # Parse map
        child = SerializationHelper.find_child_element(element, "MAP")
        if child is not None:
            map_value = SerializationHelper.deserialize_by_tag(child, "Map")
            obj.map = map_value

        return obj



class LGraphicBuilder:
    """Builder for LGraphic."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LGraphic = LGraphic()

    def build(self) -> LGraphic:
        """Build and return LGraphic object.

        Returns:
            LGraphic instance
        """
        # TODO: Add validation
        return self._obj
