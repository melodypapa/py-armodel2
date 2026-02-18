"""HwType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 17)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 991)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class HwType(HwDescriptionEntity):
    """AUTOSAR HwType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize HwType."""
        super().__init__()


class HwTypeBuilder:
    """Builder for HwType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwType = HwType()

    def build(self) -> HwType:
        """Build and return HwType object.

        Returns:
            HwType instance
        """
        # TODO: Add validation
        return self._obj
