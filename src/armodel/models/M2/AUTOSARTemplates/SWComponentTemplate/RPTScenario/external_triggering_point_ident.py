"""ExternalTriggeringPointIdent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 852)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.ident_caption import (
    IdentCaption,
)


class ExternalTriggeringPointIdent(IdentCaption):
    """AUTOSAR ExternalTriggeringPointIdent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ExternalTriggeringPointIdent."""
        super().__init__()


class ExternalTriggeringPointIdentBuilder:
    """Builder for ExternalTriggeringPointIdent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExternalTriggeringPointIdent = ExternalTriggeringPointIdent()

    def build(self) -> ExternalTriggeringPointIdent:
        """Build and return ExternalTriggeringPointIdent object.

        Returns:
            ExternalTriggeringPointIdent instance
        """
        # TODO: Add validation
        return self._obj
