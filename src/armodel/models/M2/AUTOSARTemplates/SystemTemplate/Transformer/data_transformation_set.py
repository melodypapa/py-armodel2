"""DataTransformationSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 762)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_technology import (
    TransformationTechnology,
)


class DataTransformationSet(ARElement):
    """AUTOSAR DataTransformationSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    datas: list[DataTransformation]
    transformation_technologies: list[TransformationTechnology]
    def __init__(self) -> None:
        """Initialize DataTransformationSet."""
        super().__init__()
        self.datas: list[DataTransformation] = []
        self.transformation_technologies: list[TransformationTechnology] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTransformationSet":
        """Deserialize XML element to DataTransformationSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTransformationSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataTransformationSet, cls).deserialize(element)

        # Parse datas (list from container "DATAS")
        obj.datas = []
        container = ARObject._find_child_element(element, "DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.datas.append(child_value)

        # Parse transformation_technologies (list from container "TRANSFORMATION-TECHNOLOGIES")
        obj.transformation_technologies = []
        container = ARObject._find_child_element(element, "TRANSFORMATION-TECHNOLOGIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_technologies.append(child_value)

        return obj



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
