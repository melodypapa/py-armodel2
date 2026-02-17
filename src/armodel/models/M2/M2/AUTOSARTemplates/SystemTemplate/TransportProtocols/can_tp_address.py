"""CanTpAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 610)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CanTpAddress(Identifiable):
    """AUTOSAR CanTpAddress."""

    def __init__(self) -> None:
        """Initialize CanTpAddress."""
        super().__init__()
        self.tp_address: Optional[Integer] = None


class CanTpAddressBuilder:
    """Builder for CanTpAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpAddress = CanTpAddress()

    def build(self) -> CanTpAddress:
        """Build and return CanTpAddress object.

        Returns:
            CanTpAddress instance
        """
        # TODO: Add validation
        return self._obj
