"""HwElementConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 21)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_connector import (
    HwPinGroupConnector,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
        HwElement,
    )



class HwElementConnector(Describable):
    """AUTOSAR HwElementConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_elements: list[HwElement]
    hw_pins: list[HwPinConnector]
    hw_pin_groups: list[HwPinGroupConnector]
    def __init__(self) -> None:
        """Initialize HwElementConnector."""
        super().__init__()
        self.hw_elements: list[HwElement] = []
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_groups: list[HwPinGroupConnector] = []


class HwElementConnectorBuilder:
    """Builder for HwElementConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwElementConnector = HwElementConnector()

    def build(self) -> HwElementConnector:
        """Build and return HwElementConnector object.

        Returns:
            HwElementConnector instance
        """
        # TODO: Add validation
        return self._obj
