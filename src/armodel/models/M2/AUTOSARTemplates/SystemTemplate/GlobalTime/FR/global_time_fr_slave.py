"""GlobalTimeFrSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 878)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_FR.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class GlobalTimeFrSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeFrSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crc_validated: Optional[Any]
    sequence: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize GlobalTimeFrSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None
        self.sequence: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeFrSlave":
        """Deserialize XML element to GlobalTimeFrSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeFrSlave object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse crc_validated
        child = ARObject._find_child_element(element, "CRC-VALIDATED")
        if child is not None:
            crc_validated_value = child.text
            obj.crc_validated = crc_validated_value

        # Parse sequence
        child = ARObject._find_child_element(element, "SEQUENCE")
        if child is not None:
            sequence_value = child.text
            obj.sequence = sequence_value

        return obj



class GlobalTimeFrSlaveBuilder:
    """Builder for GlobalTimeFrSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeFrSlave = GlobalTimeFrSlave()

    def build(self) -> GlobalTimeFrSlave:
        """Build and return GlobalTimeFrSlave object.

        Returns:
            GlobalTimeFrSlave instance
        """
        # TODO: Add validation
        return self._obj
