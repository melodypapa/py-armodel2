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
