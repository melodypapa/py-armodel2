"""FMAttributeDef AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)


class FMAttributeDef(Identifiable):
    """AUTOSAR FMAttributeDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[Numerical]
    max: Optional[Limit]
    min: Optional[Limit]
    def __init__(self) -> None:
        """Initialize FMAttributeDef."""
        super().__init__()
        self.default_value: Optional[Numerical] = None
        self.max: Optional[Limit] = None
        self.min: Optional[Limit] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMAttributeDef":
        """Deserialize XML element to FMAttributeDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMAttributeDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMAttributeDef, cls).deserialize(element)

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = child.text
            obj.default_value = default_value_value

        # Parse max
        child = ARObject._find_child_element(element, "MAX")
        if child is not None:
            max_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.max = max_value

        # Parse min
        child = ARObject._find_child_element(element, "MIN")
        if child is not None:
            min_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.min = min_value

        return obj



class FMAttributeDefBuilder:
    """Builder for FMAttributeDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMAttributeDef = FMAttributeDef()

    def build(self) -> FMAttributeDef:
        """Build and return FMAttributeDef object.

        Returns:
            FMAttributeDef instance
        """
        # TODO: Add validation
        return self._obj
