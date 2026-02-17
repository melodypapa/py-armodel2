"""LinErrorResponse AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)


class LinErrorResponse(ARObject):
    """AUTOSAR LinErrorResponse."""

    def __init__(self) -> None:
        """Initialize LinErrorResponse."""
        super().__init__()
        self.response_error: Optional[ISignalTriggering] = None


class LinErrorResponseBuilder:
    """Builder for LinErrorResponse."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinErrorResponse = LinErrorResponse()

    def build(self) -> LinErrorResponse:
        """Build and return LinErrorResponse object.

        Returns:
            LinErrorResponse instance
        """
        # TODO: Add validation
        return self._obj
