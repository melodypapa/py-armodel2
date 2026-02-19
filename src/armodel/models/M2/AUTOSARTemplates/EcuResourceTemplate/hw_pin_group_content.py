"""HwPinGroupContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
        HwPinGroup,
    )



class HwPinGroupContent(ARObject):
    """AUTOSAR HwPinGroupContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_pin: Optional[HwPin]
    hw_pin_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize HwPinGroupContent."""
        super().__init__()
        self.hw_pin: Optional[HwPin] = None
        self.hw_pin_group_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinGroupContent":
        """Deserialize XML element to HwPinGroupContent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinGroupContent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse hw_pin
        child = ARObject._find_child_element(element, "HW-PIN")
        if child is not None:
            hw_pin_value = ARObject._deserialize_by_tag(child, "HwPin")
            obj.hw_pin = hw_pin_value

        # Parse hw_pin_group_ref
        child = ARObject._find_child_element(element, "HW-PIN-GROUP")
        if child is not None:
            hw_pin_group_ref_value = ARObject._deserialize_by_tag(child, "HwPinGroup")
            obj.hw_pin_group_ref = hw_pin_group_ref_value

        return obj



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
