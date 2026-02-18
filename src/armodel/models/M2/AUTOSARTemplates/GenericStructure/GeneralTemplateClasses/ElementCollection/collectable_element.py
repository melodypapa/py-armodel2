"""CollectableElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ElementCollection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class CollectableElement(Identifiable, ABC):
    """AUTOSAR CollectableElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize CollectableElement."""
        super().__init__()


class CollectableElementBuilder:
    """Builder for CollectableElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CollectableElement = CollectableElement()

    def build(self) -> CollectableElement:
        """Build and return CollectableElement object.

        Returns:
            CollectableElement instance
        """
        # TODO: Add validation
        return self._obj
