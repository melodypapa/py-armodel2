"""SpecElementScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class SpecElementScope(SpecElementReference):
    """AUTOSAR SpecElementScope."""
    """Abstract base class - do not instantiate directly."""

    in_scope: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SpecElementScope."""
        super().__init__()
        self.in_scope: Optional[Boolean] = None


class SpecElementScopeBuilder:
    """Builder for SpecElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecElementScope = SpecElementScope()

    def build(self) -> SpecElementScope:
        """Build and return SpecElementScope object.

        Returns:
            SpecElementScope instance
        """
        # TODO: Add validation
        return self._obj
