"""HwDescriptionEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 15)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 990)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_value import (
    HwAttributeValue,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_category import (
    HwCategory,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_type import (
    HwType,
)
from abc import ABC, abstractmethod


class HwDescriptionEntity(Referrable, ABC):
    """AUTOSAR HwDescriptionEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    hw_attributes: list[HwAttributeValue]
    hw_categories: list[HwCategory]
    hw_type: Optional[HwType]
    def __init__(self) -> None:
        """Initialize HwDescriptionEntity."""
        super().__init__()
        self.hw_attributes: list[HwAttributeValue] = []
        self.hw_categories: list[HwCategory] = []
        self.hw_type: Optional[HwType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwDescriptionEntity":
        """Deserialize XML element to HwDescriptionEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwDescriptionEntity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse hw_attributes (list)
        obj.hw_attributes = []
        for child in ARObject._find_all_child_elements(element, "HW-ATTRIBUTES"):
            hw_attributes_value = ARObject._deserialize_by_tag(child, "HwAttributeValue")
            obj.hw_attributes.append(hw_attributes_value)

        # Parse hw_categories (list)
        obj.hw_categories = []
        for child in ARObject._find_all_child_elements(element, "HW-CATEGORIES"):
            hw_categories_value = ARObject._deserialize_by_tag(child, "HwCategory")
            obj.hw_categories.append(hw_categories_value)

        # Parse hw_type
        child = ARObject._find_child_element(element, "HW-TYPE")
        if child is not None:
            hw_type_value = ARObject._deserialize_by_tag(child, "HwType")
            obj.hw_type = hw_type_value

        return obj



class HwDescriptionEntityBuilder:
    """Builder for HwDescriptionEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwDescriptionEntity = HwDescriptionEntity()

    def build(self) -> HwDescriptionEntity:
        """Build and return HwDescriptionEntity object.

        Returns:
            HwDescriptionEntity instance
        """
        # TODO: Add validation
        return self._obj
