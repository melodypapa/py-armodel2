"""PrivacyLevel AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 18)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)


class PrivacyLevel(ARObject):
    """AUTOSAR PrivacyLevel."""

    def __init__(self) -> None:
        """Initialize PrivacyLevel."""
        super().__init__()
        self.compu_method: Optional[CompuMethod] = None
        self.privacy_level: Optional[PositiveInteger] = None


class PrivacyLevelBuilder:
    """Builder for PrivacyLevel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrivacyLevel = PrivacyLevel()

    def build(self) -> PrivacyLevel:
        """Build and return PrivacyLevel object.

        Returns:
            PrivacyLevel instance
        """
        # TODO: Add validation
        return self._obj
