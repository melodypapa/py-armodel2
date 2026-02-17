"""SecurityEventContextData AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SecurityEventContextData(ARObject):
    """AUTOSAR SecurityEventContextData."""

    def __init__(self) -> None:
        """Initialize SecurityEventContextData."""
        super().__init__()


class SecurityEventContextDataBuilder:
    """Builder for SecurityEventContextData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextData = SecurityEventContextData()

    def build(self) -> SecurityEventContextData:
        """Build and return SecurityEventContextData object.

        Returns:
            SecurityEventContextData instance
        """
        # TODO: Add validation
        return self._obj
