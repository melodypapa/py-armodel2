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


class EcucIndexableValue(ARObject):
    """AUTOSAR EcucIndexableValue."""
    """Abstract base class - do not instantiate directly."""

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
