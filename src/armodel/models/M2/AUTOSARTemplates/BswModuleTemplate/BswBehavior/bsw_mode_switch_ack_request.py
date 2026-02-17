"""BswModeSwitchAckRequest AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BswModeSwitchAckRequest(ARObject):
    """AUTOSAR BswModeSwitchAckRequest."""

    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize BswModeSwitchAckRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None


class BswModeSwitchAckRequestBuilder:
    """Builder for BswModeSwitchAckRequest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchAckRequest = BswModeSwitchAckRequest()

    def build(self) -> BswModeSwitchAckRequest:
        """Build and return BswModeSwitchAckRequest object.

        Returns:
            BswModeSwitchAckRequest instance
        """
        # TODO: Add validation
        return self._obj
