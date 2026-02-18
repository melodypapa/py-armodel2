"""Traceable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 312)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from abc import ABC, abstractmethod


class Traceable(MultilanguageReferrable, ABC):
    """AUTOSAR Traceable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    traces: list[Traceable]
    def __init__(self) -> None:
        """Initialize Traceable."""
        super().__init__()
        self.traces: list[Traceable] = []


class TraceableBuilder:
    """Builder for Traceable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Traceable = Traceable()

    def build(self) -> Traceable:
        """Build and return Traceable object.

        Returns:
            Traceable instance
        """
        # TODO: Add validation
        return self._obj
