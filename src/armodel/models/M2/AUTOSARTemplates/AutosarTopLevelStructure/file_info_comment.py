"""FileInfoComment AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 29)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AutosarTopLevelStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class FileInfoComment(ARObject):
    """AUTOSAR FileInfoComment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sdgs: list[Sdg]
    def __init__(self) -> None:
        """Initialize FileInfoComment."""
        super().__init__()
        self.sdgs: list[Sdg] = []

    def serialize(self) -> ET.Element:
        """Serialize FileInfoComment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize sdgs (list to container "SDGS")
        if self.sdgs:
            wrapper = ET.Element("SDGS")
            for item in self.sdgs:
                serialized = ARObject._serialize_item(item, "Sdg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FileInfoComment":
        """Deserialize XML element to FileInfoComment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FileInfoComment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sdgs (list from container "SDGS")
        obj.sdgs = []
        container = ARObject._find_child_element(element, "SDGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdgs.append(child_value)

        return obj



class FileInfoCommentBuilder:
    """Builder for FileInfoComment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FileInfoComment = FileInfoComment()

    def build(self) -> FileInfoComment:
        """Build and return FileInfoComment object.

        Returns:
            FileInfoComment instance
        """
        # TODO: Add validation
        return self._obj
