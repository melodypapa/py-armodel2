"""UserDefinedPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 314)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 345)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class UserDefinedPdu(Pdu):
    """AUTOSAR UserDefinedPdu."""

    def __init__(self) -> None:
        """Initialize UserDefinedPdu."""
        super().__init__()
        self.cdd_type: Optional[String] = None


class UserDefinedPduBuilder:
    """Builder for UserDefinedPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedPdu = UserDefinedPdu()

    def build(self) -> UserDefinedPdu:
        """Build and return UserDefinedPdu object.

        Returns:
            UserDefinedPdu instance
        """
        # TODO: Add validation
        return self._obj
