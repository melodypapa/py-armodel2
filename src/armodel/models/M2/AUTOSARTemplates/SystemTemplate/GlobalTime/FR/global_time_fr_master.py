"""GlobalTimeFrMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 877)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_FR.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)


class GlobalTimeFrMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeFrMaster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "crc_secured": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=GlobalTimeCrcSupportEnum,
        ),  # crcSecured
    }

    def __init__(self) -> None:
        """Initialize GlobalTimeFrMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None


class GlobalTimeFrMasterBuilder:
    """Builder for GlobalTimeFrMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeFrMaster = GlobalTimeFrMaster()

    def build(self) -> GlobalTimeFrMaster:
        """Build and return GlobalTimeFrMaster object.

        Returns:
            GlobalTimeFrMaster instance
        """
        # TODO: Add validation
        return self._obj
