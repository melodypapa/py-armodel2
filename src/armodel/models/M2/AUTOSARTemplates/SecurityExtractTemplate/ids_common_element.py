"""IdsCommonElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)


class IdsCommonElement(ARElement):
    """AUTOSAR IdsCommonElement."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize IdsCommonElement."""
        super().__init__()


class IdsCommonElementBuilder:
    """Builder for IdsCommonElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsCommonElement = IdsCommonElement()

    def build(self) -> IdsCommonElement:
        """Build and return IdsCommonElement object.

        Returns:
            IdsCommonElement instance
        """
        # TODO: Add validation
        return self._obj
