"""TimingDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class TimingDescription(Identifiable, ABC):
    """AUTOSAR TimingDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize TimingDescription."""
        super().__init__()


class TimingDescriptionBuilder:
    """Builder for TimingDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescription = TimingDescription()

    def build(self) -> TimingDescription:
        """Build and return TimingDescription object.

        Returns:
            TimingDescription instance
        """
        # TODO: Add validation
        return self._obj
