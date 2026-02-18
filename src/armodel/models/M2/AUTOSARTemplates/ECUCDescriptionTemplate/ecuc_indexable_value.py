"""EcucIndexableValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from abc import ABC, abstractmethod


class EcucIndexableValue(ARObject, ABC):
    """AUTOSAR EcucIndexableValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    index: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EcucIndexableValue."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None


class EcucIndexableValueBuilder:
    """Builder for EcucIndexableValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucIndexableValue = EcucIndexableValue()

    def build(self) -> EcucIndexableValue:
        """Build and return EcucIndexableValue object.

        Returns:
            EcucIndexableValue instance
        """
        # TODO: Add validation
        return self._obj
