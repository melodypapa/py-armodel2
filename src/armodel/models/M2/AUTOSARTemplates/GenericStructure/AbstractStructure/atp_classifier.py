"""AtpClassifier AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from abc import ABC, abstractmethod


class AtpClassifier(Identifiable, ABC):
    """AUTOSAR AtpClassifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_features: list[AtpFeature]
    def __init__(self) -> None:
        """Initialize AtpClassifier."""
        super().__init__()
        self.atp_features: list[AtpFeature] = []


class AtpClassifierBuilder:
    """Builder for AtpClassifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpClassifier = AtpClassifier()

    def build(self) -> AtpClassifier:
        """Build and return AtpClassifier object.

        Returns:
            AtpClassifier instance
        """
        # TODO: Add validation
        return self._obj
