"""UserDefinedGlobalTimeMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 879)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_UserDefined.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)


class UserDefinedGlobalTimeMaster(GlobalTimeMaster):
    """AUTOSAR UserDefinedGlobalTimeMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
