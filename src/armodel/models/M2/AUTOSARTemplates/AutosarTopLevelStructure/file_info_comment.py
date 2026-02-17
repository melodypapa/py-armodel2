"""FileInfoComment AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 29)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AutosarTopLevelStructure.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class FileInfoComment(ARObject):
    """AUTOSAR FileInfoComment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sdgs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Sdg,
        ),  # sdgs
    }

    def __init__(self) -> None:
        """Initialize FileInfoComment."""
        super().__init__()
        self.sdgs: list[Sdg] = []


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
