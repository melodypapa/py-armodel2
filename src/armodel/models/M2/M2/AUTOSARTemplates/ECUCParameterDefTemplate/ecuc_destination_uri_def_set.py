"""EcucDestinationUriDefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)


class EcucDestinationUriDefSet(ARElement):
    """AUTOSAR EcucDestinationUriDefSet."""

    def __init__(self) -> None:
        """Initialize EcucDestinationUriDefSet."""
        super().__init__()
        self.destination_uri_defs: list[EcucDestinationUriDef] = []


class EcucDestinationUriDefSetBuilder:
    """Builder for EcucDestinationUriDefSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriDefSet = EcucDestinationUriDefSet()

    def build(self) -> EcucDestinationUriDefSet:
        """Build and return EcucDestinationUriDefSet object.

        Returns:
            EcucDestinationUriDefSet instance
        """
        # TODO: Add validation
        return self._obj
