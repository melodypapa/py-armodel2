"""Xfile AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 319)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Xfile(SingleLanguageReferrable):
    """AUTOSAR Xfile."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tool: Optional[String]
    tool_version: Optional[String]
    url: Optional[Any]
    def __init__(self) -> None:
        """Initialize Xfile."""
        super().__init__()
        self.tool: Optional[String] = None
        self.tool_version: Optional[String] = None
        self.url: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize Xfile to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Xfile, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tool
        if self.tool is not None:
            serialized = SerializationHelper.serialize_item(self.tool, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tool_version
        if self.tool_version is not None:
            serialized = SerializationHelper.serialize_item(self.tool_version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize url
        if self.url is not None:
            serialized = SerializationHelper.serialize_item(self.url, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("URL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xfile":
        """Deserialize XML element to Xfile object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xfile object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Xfile, cls).deserialize(element)

        # Parse tool
        child = SerializationHelper.find_child_element(element, "TOOL")
        if child is not None:
            tool_value = child.text
            obj.tool = tool_value

        # Parse tool_version
        child = SerializationHelper.find_child_element(element, "TOOL-VERSION")
        if child is not None:
            tool_version_value = child.text
            obj.tool_version = tool_version_value

        # Parse url
        child = SerializationHelper.find_child_element(element, "URL")
        if child is not None:
            url_value = child.text
            obj.url = url_value

        return obj



class XfileBuilder:
    """Builder for Xfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xfile = Xfile()

    def build(self) -> Xfile:
        """Build and return Xfile object.

        Returns:
            Xfile instance
        """
        # TODO: Add validation
        return self._obj
