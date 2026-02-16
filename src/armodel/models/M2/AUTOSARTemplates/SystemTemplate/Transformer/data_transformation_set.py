"""DataTransformationSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_technology import (
    TransformationTechnology,
)


class DataTransformationSet(ARElement):
    """AUTOSAR DataTransformationSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("datas", None, False, True, DataTransformation),  # datas
        ("transformation_technologies", None, False, True, TransformationTechnology),  # transformationTechnologies
    ]

    def __init__(self) -> None:
        """Initialize DataTransformationSet."""
        super().__init__()
        self.datas: list[DataTransformation] = []
        self.transformation_technologies: list[TransformationTechnology] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataTransformationSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTransformationSet":
        """Create DataTransformationSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataTransformationSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataTransformationSet since parent returns ARObject
        return cast("DataTransformationSet", obj)


class DataTransformationSetBuilder:
    """Builder for DataTransformationSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTransformationSet = DataTransformationSet()

    def build(self) -> DataTransformationSet:
        """Build and return DataTransformationSet object.

        Returns:
            DataTransformationSet instance
        """
        # TODO: Add validation
        return self._obj
