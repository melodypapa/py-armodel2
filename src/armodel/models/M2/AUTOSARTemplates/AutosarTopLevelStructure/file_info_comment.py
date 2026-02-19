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

        # Parse sdgs (list)
        obj.sdgs = []
        for child in ARObject._find_all_child_elements(element, "SDGS"):
            sdgs_value = ARObject._deserialize_by_tag(child, "Sdg")
            obj.sdgs.append(sdgs_value)

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
