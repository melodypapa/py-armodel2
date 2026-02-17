"""GeneralPurposePdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)


class GeneralPurposePdu(Pdu):
    """AUTOSAR GeneralPurposePdu."""

    def __init__(self) -> None:
        """Initialize GeneralPurposePdu."""
        super().__init__()


class GeneralPurposePduBuilder:
    """Builder for GeneralPurposePdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralPurposePdu = GeneralPurposePdu()

    def build(self) -> GeneralPurposePdu:
        """Build and return GeneralPurposePdu object.

        Returns:
            GeneralPurposePdu instance
        """
        # TODO: Add validation
        return self._obj
