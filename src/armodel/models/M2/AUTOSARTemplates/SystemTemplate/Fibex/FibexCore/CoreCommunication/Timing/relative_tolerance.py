"""RelativeTolerance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class RelativeTolerance(ARObject):
    """AUTOSAR RelativeTolerance."""

    def __init__(self) -> None:
        """Initialize RelativeTolerance."""
        super().__init__()
        self.relative: Optional[Integer] = None


class RelativeToleranceBuilder:
    """Builder for RelativeTolerance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RelativeTolerance = RelativeTolerance()

    def build(self) -> RelativeTolerance:
        """Build and return RelativeTolerance object.

        Returns:
            RelativeTolerance instance
        """
        # TODO: Add validation
        return self._obj
