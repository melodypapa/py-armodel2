"""FMFeatureSelection AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_value import (
    FMAttributeValue,
)


class FMFeatureSelection(Identifiable):
    """AUTOSAR FMFeatureSelection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute_values: list[FMAttributeValue]
    def __init__(self) -> None:
        """Initialize FMFeatureSelection."""
        super().__init__()
        self.attribute_values: list[FMAttributeValue] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureSelection":
        """Deserialize XML element to FMFeatureSelection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureSelection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse attribute_values (list)
        obj.attribute_values = []
        for child in ARObject._find_all_child_elements(element, "ATTRIBUTE-VALUES"):
            attribute_values_value = ARObject._deserialize_by_tag(child, "FMAttributeValue")
            obj.attribute_values.append(attribute_values_value)

        return obj



class FMFeatureSelectionBuilder:
    """Builder for FMFeatureSelection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureSelection = FMFeatureSelection()

    def build(self) -> FMFeatureSelection:
        """Build and return FMFeatureSelection object.

        Returns:
            FMFeatureSelection instance
        """
        # TODO: Add validation
        return self._obj
