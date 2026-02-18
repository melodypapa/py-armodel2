"""CanNmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 683)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)


class CanNmEcu(BusspecificNmEcu):
    """AUTOSAR CanNmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CanNmEcu."""
        super().__init__()


class CanNmEcuBuilder:
    """Builder for CanNmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmEcu = CanNmEcu()

    def build(self) -> CanNmEcu:
        """Build and return CanNmEcu object.

        Returns:
            CanNmEcu instance
        """
        # TODO: Add validation
        return self._obj
