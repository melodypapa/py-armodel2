"""AtpType AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class AtpType(Identifiable, ABC):
    """AUTOSAR AtpType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AtpType."""
        super().__init__()


class AtpTypeBuilder:
    """Builder for AtpType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpType = AtpType()

    def build(self) -> AtpType:
        """Build and return AtpType object.

        Returns:
            AtpType instance
        """
        # TODO: Add validation
        return self._obj
