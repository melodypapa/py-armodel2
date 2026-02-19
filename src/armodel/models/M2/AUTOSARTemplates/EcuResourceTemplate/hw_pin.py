"""HwPin AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)


class HwPin(Identifiable):
    """AUTOSAR HwPin."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function_names: list[String]
    packaging_pin: Optional[String]
    pin_number: Optional[Integer]
    def __init__(self) -> None:
        """Initialize HwPin."""
        super().__init__()
        self.function_names: list[String] = []
        self.packaging_pin: Optional[String] = None
        self.pin_number: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPin":
        """Deserialize XML element to HwPin object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPin object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse function_names (list)
        obj.function_names = []
        for child in ARObject._find_all_child_elements(element, "FUNCTION-NAMES"):
            function_names_value = child.text
            obj.function_names.append(function_names_value)

        # Parse packaging_pin
        child = ARObject._find_child_element(element, "PACKAGING-PIN")
        if child is not None:
            packaging_pin_value = child.text
            obj.packaging_pin = packaging_pin_value

        # Parse pin_number
        child = ARObject._find_child_element(element, "PIN-NUMBER")
        if child is not None:
            pin_number_value = child.text
            obj.pin_number = pin_number_value

        return obj



class HwPinBuilder:
    """Builder for HwPin."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPin = HwPin()

    def build(self) -> HwPin:
        """Build and return HwPin object.

        Returns:
            HwPin instance
        """
        # TODO: Add validation
        return self._obj
