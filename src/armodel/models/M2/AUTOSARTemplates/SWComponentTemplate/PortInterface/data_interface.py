"""DataInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class DataInterface(PortInterface):
    """AUTOSAR DataInterface."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DataInterface."""
        super().__init__()


class DataInterfaceBuilder:
    """Builder for DataInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataInterface = DataInterface()

    def build(self) -> DataInterface:
        """Build and return DataInterface object.

        Returns:
            DataInterface instance
        """
        # TODO: Add validation
        return self._obj
