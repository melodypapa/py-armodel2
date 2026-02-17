"""HwPinGroupContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
        HwPinGroup,
    )



class HwPinGroupContent(ARObject):
    """AUTOSAR HwPinGroupContent."""

    hw_pin: Optional[HwPin]
    hw_pin_group: Optional[HwPinGroup]
    def __init__(self) -> None:
        """Initialize HwPinGroupContent."""
        super().__init__()
        self.hw_pin: Optional[HwPin] = None
        self.hw_pin_group: Optional[HwPinGroup] = None


class HwPinGroupContentBuilder:
    """Builder for HwPinGroupContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroupContent = HwPinGroupContent()

    def build(self) -> HwPinGroupContent:
        """Build and return HwPinGroupContent object.

        Returns:
            HwPinGroupContent instance
        """
        # TODO: Add validation
        return self._obj
