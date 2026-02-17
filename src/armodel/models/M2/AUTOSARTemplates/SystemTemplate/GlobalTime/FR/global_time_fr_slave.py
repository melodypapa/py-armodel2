"""GlobalTimeFrSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 878)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_FR.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class GlobalTimeFrSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeFrSlave."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "crc_validated": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (GlobalTimeCrc),
        ),  # crcValidated
        "sequence": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sequence
    }

    def __init__(self) -> None:
        """Initialize GlobalTimeFrSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None
        self.sequence: Optional[PositiveInteger] = None


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
