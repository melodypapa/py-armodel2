"""ConditionalChangeNad AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 438)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)


class ConditionalChangeNad(LinConfigurationEntry):
    """AUTOSAR ConditionalChangeNad."""

    byte: Optional[Integer]
    id: Optional[PositiveInteger]
    invert: Optional[Integer]
    mask: Optional[Integer]
    new_nad: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ConditionalChangeNad."""
        super().__init__()
        self.byte: Optional[Integer] = None
        self.id: Optional[PositiveInteger] = None
        self.invert: Optional[Integer] = None
        self.mask: Optional[Integer] = None
        self.new_nad: Optional[Integer] = None


class ConditionalChangeNadBuilder:
    """Builder for ConditionalChangeNad."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConditionalChangeNad = ConditionalChangeNad()

    def build(self) -> ConditionalChangeNad:
        """Build and return ConditionalChangeNad object.

        Returns:
            ConditionalChangeNad instance
        """
        # TODO: Add validation
        return self._obj
