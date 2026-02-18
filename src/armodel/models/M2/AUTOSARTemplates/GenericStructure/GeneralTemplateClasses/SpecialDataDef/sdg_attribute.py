"""SdgAttribute AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class SdgAttribute(Identifiable, ABC):
    """AUTOSAR SdgAttribute."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize SdgAttribute."""
        super().__init__()


class SdgAttributeBuilder:
    """Builder for SdgAttribute."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAttribute = SdgAttribute()

    def build(self) -> SdgAttribute:
        """Build and return SdgAttribute object.

        Returns:
            SdgAttribute instance
        """
        # TODO: Add validation
        return self._obj
