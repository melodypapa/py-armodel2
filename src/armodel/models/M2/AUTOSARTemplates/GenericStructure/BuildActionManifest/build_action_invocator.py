"""BuildActionInvocator AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 372)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize command
        if self.command is not None:
            serialized = ARObject._serialize_item(self.command, "VerbatimString")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse command
        child = ARObject._find_child_element(element, "COMMAND")
        if child is not None:
            command_value = ARObject._deserialize_by_tag(child, "VerbatimString")
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
