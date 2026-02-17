"""SaveConfigurationEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 439)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)


class SaveConfigurationEntry(LinConfigurationEntry):
    """AUTOSAR SaveConfigurationEntry."""

    def __init__(self) -> None:
        """Initialize SaveConfigurationEntry."""
        super().__init__()


class SaveConfigurationEntryBuilder:
    """Builder for SaveConfigurationEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SaveConfigurationEntry = SaveConfigurationEntry()

    def build(self) -> SaveConfigurationEntry:
        """Build and return SaveConfigurationEntry object.

        Returns:
            SaveConfigurationEntry instance
        """
        # TODO: Add validation
        return self._obj
