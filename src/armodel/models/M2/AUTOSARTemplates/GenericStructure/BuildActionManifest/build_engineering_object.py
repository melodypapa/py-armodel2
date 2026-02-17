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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RegularExpression,
    UriString,
)


class BuildEngineeringObject(EngineeringObject):
    """AUTOSAR BuildEngineeringObject."""

    file_type: NameToken
    file_type_pattern: RegularExpression
    intended: Optional[UriString]
    def __init__(self) -> None:
        """Initialize BuildEngineeringObject."""
        super().__init__()
        self.file_type: NameToken = None
        self.file_type_pattern: RegularExpression = None
        self.intended: Optional[UriString] = None


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
