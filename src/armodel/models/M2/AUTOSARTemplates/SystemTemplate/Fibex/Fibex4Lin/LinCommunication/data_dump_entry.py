"""DataDumpEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 439)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class DataDumpEntry(LinConfigurationEntry):
    """AUTOSAR DataDumpEntry."""

    def __init__(self) -> None:
        """Initialize DataDumpEntry."""
        super().__init__()
        self.byte_values: list[Integer] = []


class DataDumpEntryBuilder:
    """Builder for DataDumpEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataDumpEntry = DataDumpEntry()

    def build(self) -> DataDumpEntry:
        """Build and return DataDumpEntry object.

        Returns:
            DataDumpEntry instance
        """
        # TODO: Add validation
        return self._obj
