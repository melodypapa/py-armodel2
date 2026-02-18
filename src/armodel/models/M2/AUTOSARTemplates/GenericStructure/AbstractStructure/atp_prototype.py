"""AtpPrototype AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_type import (
    AtpType,
)
from abc import ABC, abstractmethod


class AtpPrototype(Identifiable, ABC):
    """AUTOSAR AtpPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_type: AtpType
    def __init__(self) -> None:
        """Initialize AtpPrototype."""
        super().__init__()
        self.atp_type: AtpType = None


class AtpPrototypeBuilder:
    """Builder for AtpPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpPrototype = AtpPrototype()

    def build(self) -> AtpPrototype:
        """Build and return AtpPrototype object.

        Returns:
            AtpPrototype instance
        """
        # TODO: Add validation
        return self._obj
