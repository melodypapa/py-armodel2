"""GlobalTimeCanMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 864)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_CAN.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeCrcSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class GlobalTimeCanMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeCanMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crc_secured: Optional[GlobalTimeCrcSupportEnum]
    sync: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeCanMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None
        self.sync: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCanMaster":
        """Deserialize XML element to GlobalTimeCanMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeCanMaster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeCanMaster, cls).deserialize(element)

        # Parse crc_secured
        child = ARObject._find_child_element(element, "CRC-SECURED")
        if child is not None:
            crc_secured_value = GlobalTimeCrcSupportEnum.deserialize(child)
            obj.crc_secured = crc_secured_value

        # Parse sync
        child = ARObject._find_child_element(element, "SYNC")
        if child is not None:
            sync_value = child.text
            obj.sync = sync_value

        return obj



class GlobalTimeCanMasterBuilder:
    """Builder for GlobalTimeCanMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCanMaster = GlobalTimeCanMaster()

    def build(self) -> GlobalTimeCanMaster:
        """Build and return GlobalTimeCanMaster object.

        Returns:
            GlobalTimeCanMaster instance
        """
        # TODO: Add validation
        return self._obj
