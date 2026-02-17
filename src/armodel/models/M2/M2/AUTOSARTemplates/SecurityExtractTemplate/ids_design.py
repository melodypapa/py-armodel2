"""IdsDesign AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 16)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)


class IdsDesign(ARElement):
    """AUTOSAR IdsDesign."""

    def __init__(self) -> None:
        """Initialize IdsDesign."""
        super().__init__()
        self.elements: list[IdsCommonElement] = []


class IdsDesignBuilder:
    """Builder for IdsDesign."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsDesign = IdsDesign()

    def build(self) -> IdsDesign:
        """Build and return IdsDesign object.

        Returns:
            IdsDesign instance
        """
        # TODO: Add validation
        return self._obj
