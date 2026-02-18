"""AttributeCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.abstract_multiplicity_restriction import (
    AbstractMultiplicityRestriction,
)
from abc import ABC, abstractmethod


class AttributeCondition(AbstractMultiplicityRestriction, ABC):
    """AUTOSAR AttributeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AttributeCondition."""
        super().__init__()


class AttributeConditionBuilder:
    """Builder for AttributeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeCondition = AttributeCondition()

    def build(self) -> AttributeCondition:
        """Build and return AttributeCondition object.

        Returns:
            AttributeCondition instance
        """
        # TODO: Add validation
        return self._obj
