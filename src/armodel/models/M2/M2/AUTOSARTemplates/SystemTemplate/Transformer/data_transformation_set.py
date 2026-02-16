"""DataTransformationSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataTransformation,
        ),  # datas
        "transformation_technologies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TransformationTechnology,
        ),  # transformationTechnologies
    }

    def __init__(self) -> None:
        """Initialize DataTransformationSet."""
        super().__init__()
        self.datas: list[DataTransformation] = []
        self.transformation_technologies: list[TransformationTechnology] = []


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
