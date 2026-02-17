"""DataTransformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 149)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 763)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataTransformationKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DataTransformation(Identifiable):
    """AUTOSAR DataTransformation."""

    data: Optional[DataTransformationKindEnum]
    execute_despite: Optional[Boolean]
    transformers: list[Any]
    def __init__(self) -> None:
        """Initialize DataTransformation."""
        super().__init__()
        self.data: Optional[DataTransformationKindEnum] = None
        self.execute_despite: Optional[Boolean] = None
        self.transformers: list[Any] = []


class DataTransformationBuilder:
    """Builder for DataTransformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTransformation = DataTransformation()

    def build(self) -> DataTransformation:
        """Build and return DataTransformation object.

        Returns:
            DataTransformation instance
        """
        # TODO: Add validation
        return self._obj
