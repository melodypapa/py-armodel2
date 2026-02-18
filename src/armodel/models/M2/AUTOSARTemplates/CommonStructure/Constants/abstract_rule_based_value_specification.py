"""AbstractRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 462)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from abc import ABC, abstractmethod


class AbstractRuleBasedValueSpecification(ValueSpecification, ABC):
    """AUTOSAR AbstractRuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractRuleBasedValueSpecification."""
        super().__init__()


class AbstractRuleBasedValueSpecificationBuilder:
    """Builder for AbstractRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractRuleBasedValueSpecification = AbstractRuleBasedValueSpecification()

    def build(self) -> AbstractRuleBasedValueSpecification:
        """Build and return AbstractRuleBasedValueSpecification object.

        Returns:
            AbstractRuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
