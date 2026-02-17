"""GeneralPurposeIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 345)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)


class GeneralPurposeIPdu(IPdu):
    """AUTOSAR GeneralPurposeIPdu."""

    def __init__(self) -> None:
        """Initialize GeneralPurposeIPdu."""
        super().__init__()


class GeneralPurposeIPduBuilder:
    """Builder for GeneralPurposeIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralPurposeIPdu = GeneralPurposeIPdu()

    def build(self) -> GeneralPurposeIPdu:
        """Build and return GeneralPurposeIPdu object.

        Returns:
            GeneralPurposeIPdu instance
        """
        # TODO: Add validation
        return self._obj
