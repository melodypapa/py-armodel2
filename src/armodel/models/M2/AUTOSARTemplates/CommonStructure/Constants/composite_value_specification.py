"""CompositeValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 434)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from abc import ABC, abstractmethod


class CompositeValueSpecification(ValueSpecification, ABC):
    """AUTOSAR CompositeValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize CompositeValueSpecification."""
        super().__init__()


class CompositeValueSpecificationBuilder:
    """Builder for CompositeValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositeValueSpecification = CompositeValueSpecification()

    def build(self) -> CompositeValueSpecification:
        """Build and return CompositeValueSpecification object.

        Returns:
            CompositeValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
