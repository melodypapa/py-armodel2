"""BswQueuedDataReceptionPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BswQueuedDataReceptionPolicy(ARObject):
    """AUTOSAR BswQueuedDataReceptionPolicy."""

    def __init__(self) -> None:
        """Initialize BswQueuedDataReceptionPolicy."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None


class BswQueuedDataReceptionPolicyBuilder:
    """Builder for BswQueuedDataReceptionPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswQueuedDataReceptionPolicy = BswQueuedDataReceptionPolicy()

    def build(self) -> BswQueuedDataReceptionPolicy:
        """Build and return BswQueuedDataReceptionPolicy object.

        Returns:
            BswQueuedDataReceptionPolicy instance
        """
        # TODO: Add validation
        return self._obj
