"""UserDefinedIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 346)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class UserDefinedIPdu(IPdu):
    """AUTOSAR UserDefinedIPdu."""

    def __init__(self) -> None:
        """Initialize UserDefinedIPdu."""
        super().__init__()
        self.cdd_type: Optional[String] = None


class UserDefinedIPduBuilder:
    """Builder for UserDefinedIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedIPdu = UserDefinedIPdu()

    def build(self) -> UserDefinedIPdu:
        """Build and return UserDefinedIPdu object.

        Returns:
            UserDefinedIPdu instance
        """
        # TODO: Add validation
        return self._obj
