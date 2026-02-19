"""BuildEngineeringObject AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 372)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RegularExpression,
    UriString,
)


class BuildEngineeringObject(EngineeringObject):
    """AUTOSAR BuildEngineeringObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    file_type: NameToken
    file_type_pattern: RegularExpression
    intended: Optional[UriString]
    def __init__(self) -> None:
        """Initialize BuildEngineeringObject."""
        super().__init__()
        self.file_type: NameToken = None
        self.file_type_pattern: RegularExpression = None
        self.intended: Optional[UriString] = None

    def serialize(self) -> ET.Element:
        """Serialize BuildEngineeringObject to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildEngineeringObject, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize file_type
        if self.file_type is not None:
            serialized = ARObject._serialize_item(self.file_type, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize file_type_pattern
        if self.file_type_pattern is not None:
            serialized = ARObject._serialize_item(self.file_type_pattern, "RegularExpression")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILE-TYPE-PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize intended
        if self.intended is not None:
            serialized = ARObject._serialize_item(self.intended, "UriString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTENDED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildEngineeringObject":
        """Deserialize XML element to BuildEngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildEngineeringObject object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildEngineeringObject, cls).deserialize(element)

        # Parse file_type
        child = ARObject._find_child_element(element, "FILE-TYPE")
        if child is not None:
            file_type_value = child.text
            obj.file_type = file_type_value

        # Parse file_type_pattern
        child = ARObject._find_child_element(element, "FILE-TYPE-PATTERN")
        if child is not None:
            file_type_pattern_value = child.text
            obj.file_type_pattern = file_type_pattern_value

        # Parse intended
        child = ARObject._find_child_element(element, "INTENDED")
        if child is not None:
            intended_value = child.text
            obj.intended = intended_value

        return obj



class BuildEngineeringObjectBuilder:
    """Builder for BuildEngineeringObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildEngineeringObject = BuildEngineeringObject()

    def build(self) -> BuildEngineeringObject:
        """Build and return BuildEngineeringObject object.

        Returns:
            BuildEngineeringObject instance
        """
        # TODO: Add validation
        return self._obj
