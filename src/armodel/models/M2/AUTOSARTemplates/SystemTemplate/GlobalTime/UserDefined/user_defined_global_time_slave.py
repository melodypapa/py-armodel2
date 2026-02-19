"""UserDefinedGlobalTimeSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 879)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_UserDefined.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedGlobalTimeSlave(GlobalTimeSlave):
    """AUTOSAR UserDefinedGlobalTimeSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize UserDefinedGlobalTimeSlave."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedGlobalTimeSlave":
        """Deserialize XML element to UserDefinedGlobalTimeSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedGlobalTimeSlave object
        """
        # Delegate to parent class to handle inherited attributes
        return super(UserDefinedGlobalTimeSlave, cls).deserialize(element)



class UserDefinedGlobalTimeSlaveBuilder:
    """Builder for UserDefinedGlobalTimeSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedGlobalTimeSlave = UserDefinedGlobalTimeSlave()

    def build(self) -> UserDefinedGlobalTimeSlave:
        """Build and return UserDefinedGlobalTimeSlave object.

        Returns:
            UserDefinedGlobalTimeSlave instance
        """
        # TODO: Add validation
        return self._obj
