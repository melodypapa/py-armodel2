"""FibexElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2026)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 445)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)
from abc import ABC, abstractmethod


class FibexElement(PackageableElement, ABC):
    """AUTOSAR FibexElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize FibexElement."""
        super().__init__()


class FibexElementBuilder:
    """Builder for FibexElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FibexElement = FibexElement()

    def build(self) -> FibexElement:
        """Build and return FibexElement object.

        Returns:
            FibexElement instance
        """
        # TODO: Add validation
        return self._obj
