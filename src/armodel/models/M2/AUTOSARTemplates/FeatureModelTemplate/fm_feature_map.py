"""FMFeatureMap AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map_element import (
    FMFeatureMapElement,
)


class FMFeatureMap(ARElement):
    """AUTOSAR FMFeatureMap."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mappings", None, False, True, FMFeatureMapElement),  # mappings
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureMap."""
        super().__init__()
        self.mappings: list[FMFeatureMapElement] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureMap to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMap":
        """Create FMFeatureMap from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureMap instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureMap since parent returns ARObject
        return cast("FMFeatureMap", obj)


class FMFeatureMapBuilder:
    """Builder for FMFeatureMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMap = FMFeatureMap()

    def build(self) -> FMFeatureMap:
        """Build and return FMFeatureMap object.

        Returns:
            FMFeatureMap instance
        """
        # TODO: Add validation
        return self._obj
