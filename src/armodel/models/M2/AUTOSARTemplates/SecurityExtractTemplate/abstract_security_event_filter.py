"""AbstractSecurityEventFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 21)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class AbstractSecurityEventFilter(Identifiable, ABC):
    """AUTOSAR AbstractSecurityEventFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractSecurityEventFilter."""
        super().__init__()


class AbstractSecurityEventFilterBuilder:
    """Builder for AbstractSecurityEventFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractSecurityEventFilter = AbstractSecurityEventFilter()

    def build(self) -> AbstractSecurityEventFilter:
        """Build and return AbstractSecurityEventFilter object.

        Returns:
            AbstractSecurityEventFilter instance
        """
        # TODO: Add validation
        return self._obj
