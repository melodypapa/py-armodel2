"""RestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 86)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint import (
    SeverityEnum,
)
from abc import ABC, abstractmethod


class RestrictionWithSeverity(ARObject, ABC):
    """AUTOSAR RestrictionWithSeverity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    severity: SeverityEnum
    def __init__(self) -> None:
        """Initialize RestrictionWithSeverity."""
        super().__init__()
        self.severity: SeverityEnum = None


class RestrictionWithSeverityBuilder:
    """Builder for RestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RestrictionWithSeverity = RestrictionWithSeverity()

    def build(self) -> RestrictionWithSeverity:
        """Build and return RestrictionWithSeverity object.

        Returns:
            RestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
