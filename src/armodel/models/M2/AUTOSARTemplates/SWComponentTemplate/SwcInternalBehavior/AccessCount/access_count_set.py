"""AccessCountSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count import (
    AccessCount,
)


class AccessCountSet(ARObject):
    """AUTOSAR AccessCountSet."""

    def __init__(self) -> None:
        """Initialize AccessCountSet."""
        super().__init__()
        self.access_counts: list[AccessCount] = []
        self.count_profile: Optional[NameToken] = None


class AccessCountSetBuilder:
    """Builder for AccessCountSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCountSet = AccessCountSet()

    def build(self) -> AccessCountSet:
        """Build and return AccessCountSet object.

        Returns:
            AccessCountSet instance
        """
        # TODO: Add validation
        return self._obj
