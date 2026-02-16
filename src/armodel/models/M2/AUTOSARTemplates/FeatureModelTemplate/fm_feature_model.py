"""FMFeatureModel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureModel(ARElement):
    """AUTOSAR FMFeatureModel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("features", None, False, True, FMFeature),  # features
        ("root", None, False, False, FMFeature),  # root
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureModel."""
        super().__init__()
        self.features: list[FMFeature] = []
        self.root: Optional[FMFeature] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureModel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureModel":
        """Create FMFeatureModel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureModel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureModel since parent returns ARObject
        return cast("FMFeatureModel", obj)


class FMFeatureModelBuilder:
    """Builder for FMFeatureModel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureModel = FMFeatureModel()

    def build(self) -> FMFeatureModel:
        """Build and return FMFeatureModel object.

        Returns:
            FMFeatureModel instance
        """
        # TODO: Add validation
        return self._obj
