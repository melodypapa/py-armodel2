"""EOCExecutableEntityRefAbstract AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class EOCExecutableEntityRefAbstract(Identifiable, ABC):
    """AUTOSAR EOCExecutableEntityRefAbstract."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    direct_successors: list[Any]
    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefAbstract."""
        super().__init__()
        self.direct_successors: list[Any] = []


class EOCExecutableEntityRefAbstractBuilder:
    """Builder for EOCExecutableEntityRefAbstract."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRefAbstract = EOCExecutableEntityRefAbstract()

    def build(self) -> EOCExecutableEntityRefAbstract:
        """Build and return EOCExecutableEntityRefAbstract object.

        Returns:
            EOCExecutableEntityRefAbstract instance
        """
        # TODO: Add validation
        return self._obj
