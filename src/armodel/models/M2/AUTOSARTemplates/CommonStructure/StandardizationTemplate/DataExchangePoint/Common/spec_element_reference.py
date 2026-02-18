"""SpecElementReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from abc import ABC, abstractmethod


class SpecElementReference(Identifiable, ABC):
    """AUTOSAR SpecElementReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    alternative: Optional[String]
    def __init__(self) -> None:
        """Initialize SpecElementReference."""
        super().__init__()
        self.alternative: Optional[String] = None


class SpecElementReferenceBuilder:
    """Builder for SpecElementReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecElementReference = SpecElementReference()

    def build(self) -> SpecElementReference:
        """Build and return SpecElementReference object.

        Returns:
            SpecElementReference instance
        """
        # TODO: Add validation
        return self._obj
