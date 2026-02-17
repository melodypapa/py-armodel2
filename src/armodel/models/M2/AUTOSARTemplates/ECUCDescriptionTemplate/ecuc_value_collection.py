"""EcucValueCollection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 108)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2022)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class EcucValueCollection(ARElement):
    """AUTOSAR EcucValueCollection."""

    ecuc_values: list[Any]
    ecu_extract: Optional[System]
    def __init__(self) -> None:
        """Initialize EcucValueCollection."""
        super().__init__()
        self.ecuc_values: list[Any] = []
        self.ecu_extract: Optional[System] = None


class EcucValueCollectionBuilder:
    """Builder for EcucValueCollection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValueCollection = EcucValueCollection()

    def build(self) -> EcucValueCollection:
        """Build and return EcucValueCollection object.

        Returns:
            EcucValueCollection instance
        """
        # TODO: Add validation
        return self._obj
