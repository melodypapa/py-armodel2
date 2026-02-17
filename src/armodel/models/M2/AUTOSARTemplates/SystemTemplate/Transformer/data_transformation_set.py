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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_technology import (
    TransformationTechnology,
)


class DataTransformationSet(ARElement):
    """AUTOSAR DataTransformationSet."""

    datas: list[DataTransformation]
    transformation_technologies: list[TransformationTechnology]
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
