"""HwPinGroupConnector AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPinGroupConnector(Describable):
    """AUTOSAR HwPinGroupConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_pins: list[HwPinConnector]
    hw_pin_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize HwPinGroupConnector."""
        super().__init__()
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_group_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinGroupConnector":
        """Deserialize XML element to HwPinGroupConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinGroupConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse hw_pins (list)
        obj.hw_pins = []
        for child in ARObject._find_all_child_elements(element, "HW-PINS"):
            hw_pins_value = ARObject._deserialize_by_tag(child, "HwPinConnector")
            obj.hw_pins.append(hw_pins_value)

        # Parse hw_pin_group_refs (list)
        obj.hw_pin_group_refs = []
        for child in ARObject._find_all_child_elements(element, "HW-PIN-GROUPS"):
            hw_pin_group_refs_value = ARObject._deserialize_by_tag(child, "HwPinGroup")
            obj.hw_pin_group_refs.append(hw_pin_group_refs_value)

        return obj



class HwPinGroupConnectorBuilder:
    """Builder for HwPinGroupConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroupConnector = HwPinGroupConnector()

    def build(self) -> HwPinGroupConnector:
        """Build and return HwPinGroupConnector object.

        Returns:
            HwPinGroupConnector instance
        """
        # TODO: Add validation
        return self._obj
