"""EcucAbstractReferenceValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import (
    EcucIndexableValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from abc import ABC, abstractmethod


class EcucAbstractReferenceValue(EcucIndexableValue, ABC):
    """AUTOSAR EcucAbstractReferenceValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    annotations: list[Annotation]
    definition: Optional[Any]
    is_auto_value: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.definition: Optional[Any] = None
        self.is_auto_value: Optional[Boolean] = None


class EcucAbstractReferenceValueBuilder:
    """Builder for EcucAbstractReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractReferenceValue = EcucAbstractReferenceValue()

    def build(self) -> EcucAbstractReferenceValue:
        """Build and return EcucAbstractReferenceValue object.

        Returns:
            EcucAbstractReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
