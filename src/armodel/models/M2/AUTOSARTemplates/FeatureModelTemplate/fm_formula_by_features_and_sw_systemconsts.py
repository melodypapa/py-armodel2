"""FMFormulaByFeaturesAndSwSystemconsts AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFormulaByFeaturesAndSwSystemconsts(ARObject):
    """AUTOSAR FMFormulaByFeaturesAndSwSystemconsts."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("feature", None, False, False, FMFeature),  # feature
    ]

    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndSwSystemconsts."""
        super().__init__()
        self.feature: Optional[FMFeature] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFormulaByFeaturesAndSwSystemconsts to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFormulaByFeaturesAndSwSystemconsts":
        """Create FMFormulaByFeaturesAndSwSystemconsts from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFormulaByFeaturesAndSwSystemconsts instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFormulaByFeaturesAndSwSystemconsts since parent returns ARObject
        return cast("FMFormulaByFeaturesAndSwSystemconsts", obj)


class FMFormulaByFeaturesAndSwSystemconstsBuilder:
    """Builder for FMFormulaByFeaturesAndSwSystemconsts."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFormulaByFeaturesAndSwSystemconsts = FMFormulaByFeaturesAndSwSystemconsts()

    def build(self) -> FMFormulaByFeaturesAndSwSystemconsts:
        """Build and return FMFormulaByFeaturesAndSwSystemconsts object.

        Returns:
            FMFormulaByFeaturesAndSwSystemconsts instance
        """
        # TODO: Add validation
        return self._obj
