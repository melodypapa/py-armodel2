"""GeneralPurposeConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 388)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GeneralPurposeConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class GeneralPurposeConnection(ARElement):
    """AUTOSAR GeneralPurposeConnection."""

    pdu_triggerings: list[PduTriggering]
    def __init__(self) -> None:
        """Initialize GeneralPurposeConnection."""
        super().__init__()
        self.pdu_triggerings: list[PduTriggering] = []


class GeneralPurposeConnectionBuilder:
    """Builder for GeneralPurposeConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralPurposeConnection = GeneralPurposeConnection()

    def build(self) -> GeneralPurposeConnection:
        """Build and return GeneralPurposeConnection object.

        Returns:
            GeneralPurposeConnection instance
        """
        # TODO: Add validation
        return self._obj
