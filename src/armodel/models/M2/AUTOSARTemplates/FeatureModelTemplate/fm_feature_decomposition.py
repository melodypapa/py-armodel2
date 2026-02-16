"""FMFeatureDecomposition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureDecomposition(ARObject):
    """AUTOSAR FMFeatureDecomposition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, True, False, None),  # category
        ("features", None, False, True, FMFeature),  # features
        ("max", None, True, False, None),  # max
        ("min", None, True, False, None),  # min
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureDecomposition."""
        super().__init__()
        self.category: Optional[CategoryString] = None
        self.features: list[FMFeature] = []
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureDecomposition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureDecomposition":
        """Create FMFeatureDecomposition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureDecomposition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureDecomposition since parent returns ARObject
        return cast("FMFeatureDecomposition", obj)


class FMFeatureDecompositionBuilder:
    """Builder for FMFeatureDecomposition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureDecomposition = FMFeatureDecomposition()

    def build(self) -> FMFeatureDecomposition:
        """Build and return FMFeatureDecomposition object.

        Returns:
            FMFeatureDecomposition instance
        """
        # TODO: Add validation
        return self._obj
