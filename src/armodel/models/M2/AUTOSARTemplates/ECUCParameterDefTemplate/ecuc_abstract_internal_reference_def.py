"""EcucAbstractInternalReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_reference_def import (
    EcucAbstractReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class EcucAbstractInternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """AUTOSAR EcucAbstractInternalReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    requires: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucAbstractInternalReferenceDef."""
        super().__init__()
        self.requires: Optional[Boolean] = None


class EcucAbstractInternalReferenceDefBuilder:
    """Builder for EcucAbstractInternalReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractInternalReferenceDef = EcucAbstractInternalReferenceDef()

    def build(self) -> EcucAbstractInternalReferenceDef:
        """Build and return EcucAbstractInternalReferenceDef object.

        Returns:
            EcucAbstractInternalReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
