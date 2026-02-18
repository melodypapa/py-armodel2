"""HwPinGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 19)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2027)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_content import (
        HwPinGroupContent,
    )



class HwPinGroup(Identifiable):
    """AUTOSAR HwPinGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_pin_group_content: Optional[HwPinGroupContent]
    def __init__(self) -> None:
        """Initialize HwPinGroup."""
        super().__init__()
        self.hw_pin_group_content: Optional[HwPinGroupContent] = None


class HwPinGroupBuilder:
    """Builder for HwPinGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroup = HwPinGroup()

    def build(self) -> HwPinGroup:
        """Build and return HwPinGroup object.

        Returns:
            HwPinGroup instance
        """
        # TODO: Add validation
        return self._obj
