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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    hw_pin_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize HwElementConnector."""
        super().__init__()
        self.hw_elements: list[HwElement] = []
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_group_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwElementConnector":
        """Deserialize XML element to HwElementConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwElementConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse hw_elements (list)
        obj.hw_elements = []
        for child in ARObject._find_all_child_elements(element, "HW-ELEMENTS"):
            hw_elements_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.hw_elements.append(hw_elements_value)

        # Parse hw_pins (list)
        obj.hw_pins = []
        for child in ARObject._find_all_child_elements(element, "HW-PINS"):
            hw_pins_value = ARObject._deserialize_by_tag(child, "HwPinConnector")
            obj.hw_pins.append(hw_pins_value)

        # Parse hw_pin_group_refs (list)
        obj.hw_pin_group_refs = []
        for child in ARObject._find_all_child_elements(element, "HW-PIN-GROUPS"):
            hw_pin_group_refs_value = ARObject._deserialize_by_tag(child, "HwPinGroupConnector")
            obj.hw_pin_group_refs.append(hw_pin_group_refs_value)

        return obj



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
