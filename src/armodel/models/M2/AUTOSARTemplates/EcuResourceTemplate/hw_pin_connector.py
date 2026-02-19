"""HwPinConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)


class HwPinConnector(Describable):
    """AUTOSAR HwPinConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_pins: list[HwPin]
    def __init__(self) -> None:
        """Initialize HwPinConnector."""
        super().__init__()
        self.hw_pins: list[HwPin] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinConnector":
        """Deserialize XML element to HwPinConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse hw_pins (list)
        obj.hw_pins = []
        for child in ARObject._find_all_child_elements(element, "HW-PINS"):
            hw_pins_value = ARObject._deserialize_by_tag(child, "HwPin")
            obj.hw_pins.append(hw_pins_value)

        return obj



class HwPinConnectorBuilder:
    """Builder for HwPinConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinConnector = HwPinConnector()

    def build(self) -> HwPinConnector:
        """Build and return HwPinConnector object.

        Returns:
            HwPinConnector instance
        """
        # TODO: Add validation
        return self._obj
