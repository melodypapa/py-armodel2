"""Sd AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_attribute

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    VerbatimStringPlain,
)


class Sd(ARObject):
    """AUTOSAR Sd."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _gid: NameToken
    value: VerbatimStringPlain
    xml_space: Optional[XmlSpaceEnum]
    def __init__(self) -> None:
        """Initialize Sd."""
        super().__init__()
        self._gid: NameToken = None
        self.value: VerbatimStringPlain = None
        self.xml_space: Optional[XmlSpaceEnum] = None
    @property
    @xml_attribute
    def gid(self) -> NameToken:
        """Get gid XML attribute."""
        return self._gid

    @gid.setter
    def gid(self, value: NameToken) -> None:
        """Set gid XML attribute."""
        self._gid = value


    def serialize(self) -> ET.Element:
        """Serialize Sd to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Sd, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize gid as XML attribute
        if self.gid is not None:
            elem.attrib["GID"] = str(self.gid)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "VerbatimStringPlain")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize xml_space
        if self.xml_space is not None:
            serialized = SerializationHelper.serialize_item(self.xml_space, "XmlSpaceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XML-SPACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sd":
        """Deserialize XML element to Sd object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Sd object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Sd, cls).deserialize(element)

        # Parse gid from XML attribute
        if "GID" in element.attrib:
            gid_value = element.attrib["GID"]
            obj.gid = gid_value

        # Parse value
        child = SerializationHelper.find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        # Parse xml_space
        child = SerializationHelper.find_child_element(element, "XML-SPACE")
        if child is not None:
            xml_space_value = SerializationHelper.deserialize_by_tag(child, "XmlSpaceEnum")
            obj.xml_space = xml_space_value

        return obj



class SdBuilder:
    """Builder for Sd."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sd = Sd()

    def build(self) -> Sd:
        """Build and return Sd object.

        Returns:
            Sd instance
        """
        # TODO: Add validation
        return self._obj
