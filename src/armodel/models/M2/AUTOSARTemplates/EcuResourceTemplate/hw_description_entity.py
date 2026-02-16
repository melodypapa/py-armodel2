"""HwDescriptionEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_value import (
    HwAttributeValue,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_category import (
    HwCategory,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_type import (
    HwType,
)


class HwDescriptionEntity(Referrable):
    """AUTOSAR HwDescriptionEntity."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_attributes", None, False, True, HwAttributeValue),  # hwAttributes
        ("hw_categories", None, False, True, HwCategory),  # hwCategories
        ("hw_type", None, False, False, HwType),  # hwType
    ]

    def __init__(self) -> None:
        """Initialize HwDescriptionEntity."""
        super().__init__()
        self.hw_attributes: list[HwAttributeValue] = []
        self.hw_categories: list[HwCategory] = []
        self.hw_type: Optional[HwType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwDescriptionEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwDescriptionEntity":
        """Create HwDescriptionEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwDescriptionEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwDescriptionEntity since parent returns ARObject
        return cast("HwDescriptionEntity", obj)


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
