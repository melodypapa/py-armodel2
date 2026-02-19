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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinConfigurationEntry":
        """Deserialize XML element to LinConfigurationEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinConfigurationEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinConfigurationEntry, cls).deserialize(element)

        # Parse assigned
        child = ARObject._find_child_element(element, "ASSIGNED")
        if child is not None:
            assigned_value = ARObject._deserialize_by_tag(child, "LinSlave")
            obj.assigned = assigned_value

        # Parse assigned_lin
        child = ARObject._find_child_element(element, "ASSIGNED-LIN")
        if child is not None:
            assigned_lin_value = ARObject._deserialize_by_tag(child, "LinSlaveConfigIdent")
            obj.assigned_lin = assigned_lin_value

        return obj



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
