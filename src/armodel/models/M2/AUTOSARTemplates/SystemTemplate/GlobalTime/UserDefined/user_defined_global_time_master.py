"""UserDefinedGlobalTimeMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 879)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_UserDefined.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)


class UserDefinedGlobalTimeMaster(GlobalTimeMaster):
    """AUTOSAR UserDefinedGlobalTimeMaster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize UserDefinedGlobalTimeMaster."""
        super().__init__()


class UserDefinedGlobalTimeMasterBuilder:
    """Builder for UserDefinedGlobalTimeMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedGlobalTimeMaster = UserDefinedGlobalTimeMaster()

    def build(self) -> UserDefinedGlobalTimeMaster:
        """Build and return UserDefinedGlobalTimeMaster object.

        Returns:
            UserDefinedGlobalTimeMaster instance
        """
        # TODO: Add validation
        return self._obj
