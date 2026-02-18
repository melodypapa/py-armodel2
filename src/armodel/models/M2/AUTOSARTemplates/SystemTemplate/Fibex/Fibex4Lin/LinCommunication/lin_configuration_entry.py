"""LinConfigurationEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 434)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave import (
    LinSlave,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config_ident import (
    LinSlaveConfigIdent,
)
from abc import ABC, abstractmethod


class LinConfigurationEntry(ScheduleTableEntry, ABC):
    """AUTOSAR LinConfigurationEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    assigned: Optional[LinSlave]
    assigned_lin: Optional[LinSlaveConfigIdent]
    def __init__(self) -> None:
        """Initialize LinConfigurationEntry."""
        super().__init__()
        self.assigned: Optional[LinSlave] = None
        self.assigned_lin: Optional[LinSlaveConfigIdent] = None


class LinConfigurationEntryBuilder:
    """Builder for LinConfigurationEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinConfigurationEntry = LinConfigurationEntry()

    def build(self) -> LinConfigurationEntry:
        """Build and return LinConfigurationEntry object.

        Returns:
            LinConfigurationEntry instance
        """
        # TODO: Add validation
        return self._obj
