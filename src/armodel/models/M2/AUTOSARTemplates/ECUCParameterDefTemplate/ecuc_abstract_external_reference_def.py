"""EcucAbstractExternalReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_reference_def import (
    EcucAbstractReferenceDef,
)
from abc import ABC, abstractmethod


class EcucAbstractExternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """AUTOSAR EcucAbstractExternalReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize EcucAbstractExternalReferenceDef."""
        super().__init__()


class EcucAbstractExternalReferenceDefBuilder:
    """Builder for EcucAbstractExternalReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractExternalReferenceDef = EcucAbstractExternalReferenceDef()

    def build(self) -> EcucAbstractExternalReferenceDef:
        """Build and return EcucAbstractExternalReferenceDef object.

        Returns:
            EcucAbstractExternalReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
