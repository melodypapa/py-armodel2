"""EcucAbstractReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class EcucAbstractReferenceDef(EcucCommonAttributes, ABC):
    """AUTOSAR EcucAbstractReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    with_auto: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceDef."""
        super().__init__()
        self.with_auto: Optional[Boolean] = None


class EcucAbstractReferenceDefBuilder:
    """Builder for EcucAbstractReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractReferenceDef = EcucAbstractReferenceDef()

    def build(self) -> EcucAbstractReferenceDef:
        """Build and return EcucAbstractReferenceDef object.

        Returns:
            EcucAbstractReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
