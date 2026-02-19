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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFormatTailoring":
        """Deserialize XML element to DataFormatTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataFormatTailoring object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse class_tailorings (list from container "CLASS-TAILORINGS")
        obj.class_tailorings = []
        container = ARObject._find_child_element(element, "CLASS-TAILORINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.class_tailorings.append(child_value)

        # Parse constraints (list from container "CONSTRAINTS")
        obj.constraints = []
        container = ARObject._find_child_element(element, "CONSTRAINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constraints.append(child_value)

        return obj



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
