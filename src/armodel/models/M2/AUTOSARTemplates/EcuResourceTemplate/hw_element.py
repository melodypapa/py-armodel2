"""HwElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 296)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 18)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 991)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2026)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element_connector import (
        HwElementConnector,
    )



class HwElement(HwDescriptionEntity):
    """AUTOSAR HwElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_elements: list[HwElementConnector]
    hw_pin_group_refs: list[ARRef]
    nested_elements: list[HwElement]
    def __init__(self) -> None:
        """Initialize HwElement."""
        super().__init__()
        self.hw_elements: list[HwElementConnector] = []
        self.hw_pin_group_refs: list[ARRef] = []
        self.nested_elements: list[HwElement] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwElement":
        """Deserialize XML element to HwElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse hw_elements (list)
        obj.hw_elements = []
        for child in ARObject._find_all_child_elements(element, "HW-ELEMENTS"):
            hw_elements_value = ARObject._deserialize_by_tag(child, "HwElementConnector")
            obj.hw_elements.append(hw_elements_value)

        # Parse hw_pin_group_refs (list)
        obj.hw_pin_group_refs = []
        for child in ARObject._find_all_child_elements(element, "HW-PIN-GROUPS"):
            hw_pin_group_refs_value = ARObject._deserialize_by_tag(child, "HwPinGroup")
            obj.hw_pin_group_refs.append(hw_pin_group_refs_value)

        # Parse nested_elements (list)
        obj.nested_elements = []
        for child in ARObject._find_all_child_elements(element, "NESTED-ELEMENTS"):
            nested_elements_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.nested_elements.append(nested_elements_value)

        return obj



class HwElementBuilder:
    """Builder for HwElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwElement = HwElement()

    def build(self) -> HwElement:
        """Build and return HwElement object.

        Returns:
            HwElement instance
        """
        # TODO: Add validation
        return self._obj
