"""GlobalTimeEthSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 867)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class GlobalTimeEthSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeEthSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crc_validated: Optional[Any]
    def __init__(self) -> None:
        """Initialize GlobalTimeEthSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeEthSlave":
        """Deserialize XML element to GlobalTimeEthSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeEthSlave object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse crc_validated
        child = ARObject._find_child_element(element, "CRC-VALIDATED")
        if child is not None:
            crc_validated_value = child.text
            obj.crc_validated = crc_validated_value

        return obj



class GlobalTimeEthSlaveBuilder:
    """Builder for GlobalTimeEthSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeEthSlave = GlobalTimeEthSlave()

    def build(self) -> GlobalTimeEthSlave:
        """Build and return GlobalTimeEthSlave object.

        Returns:
            GlobalTimeEthSlave instance
        """
        # TODO: Add validation
        return self._obj
