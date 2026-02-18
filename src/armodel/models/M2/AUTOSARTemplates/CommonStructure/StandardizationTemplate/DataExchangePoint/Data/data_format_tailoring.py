"""DataFormatTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
    ConstraintTailoring,
)


class DataFormatTailoring(ARObject):
    """AUTOSAR DataFormatTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    class_tailorings: list[ClassTailoring]
    constraints: list[ConstraintTailoring]
    def __init__(self) -> None:
        """Initialize DataFormatTailoring."""
        super().__init__()
        self.class_tailorings: list[ClassTailoring] = []
        self.constraints: list[ConstraintTailoring] = []


class DataFormatTailoringBuilder:
    """Builder for DataFormatTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataFormatTailoring = DataFormatTailoring()

    def build(self) -> DataFormatTailoring:
        """Build and return DataFormatTailoring object.

        Returns:
            DataFormatTailoring instance
        """
        # TODO: Add validation
        return self._obj
