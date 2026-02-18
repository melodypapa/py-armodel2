"""AtpBlueprintable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 424)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 162)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class AtpBlueprintable(Identifiable, ABC):
    """AUTOSAR AtpBlueprintable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AtpBlueprintable."""
        super().__init__()


class AtpBlueprintableBuilder:
    """Builder for AtpBlueprintable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpBlueprintable = AtpBlueprintable()

    def build(self) -> AtpBlueprintable:
        """Build and return AtpBlueprintable object.

        Returns:
            AtpBlueprintable instance
        """
        # TODO: Add validation
        return self._obj
