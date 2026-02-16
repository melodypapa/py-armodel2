"""HwCategory AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_def import (
    HwAttributeDef,
)


class HwCategory(ARElement):
    """AUTOSAR HwCategory."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_attribute_defs", None, False, True, HwAttributeDef),  # hwAttributeDefs
    ]

    def __init__(self) -> None:
        """Initialize HwCategory."""
        super().__init__()
        self.hw_attribute_defs: list[HwAttributeDef] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwCategory to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwCategory":
        """Create HwCategory from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwCategory instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwCategory since parent returns ARObject
        return cast("HwCategory", obj)


class HwCategoryBuilder:
    """Builder for HwCategory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwCategory = HwCategory()

    def build(self) -> HwCategory:
        """Build and return HwCategory object.

        Returns:
            HwCategory instance
        """
        # TODO: Add validation
        return self._obj
