"""BuildActionInvocator AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 372)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class BuildActionInvocator(ARObject):
    """AUTOSAR BuildActionInvocator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    command: Optional[VerbatimString]
    def __init__(self) -> None:
        """Initialize BuildActionInvocator."""
        super().__init__()
        self.command: Optional[VerbatimString] = None

    def serialize(self) -> ET.Element:
        """Serialize BuildActionInvocator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildActionInvocator, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize command
        if self.command is not None:
            serialized = SerializationHelper.serialize_item(self.command, "VerbatimString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMAND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionInvocator":
        """Deserialize XML element to BuildActionInvocator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionInvocator object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildActionInvocator, cls).deserialize(element)

        # Parse command
        child = SerializationHelper.find_child_element(element, "COMMAND")
        if child is not None:
            command_value = SerializationHelper.deserialize_by_tag(child, "VerbatimString")
            obj.command = command_value

        return obj



class BuildActionInvocatorBuilder:
    """Builder for BuildActionInvocator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionInvocator = BuildActionInvocator()

    def build(self) -> BuildActionInvocator:
        """Build and return BuildActionInvocator object.

        Returns:
            BuildActionInvocator instance
        """
        # TODO: Add validation
        return self._obj
