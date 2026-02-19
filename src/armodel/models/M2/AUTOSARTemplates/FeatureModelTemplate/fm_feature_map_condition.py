"""FMFeatureMapCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 55)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class FMFeatureMapCondition(Identifiable):
    """AUTOSAR FMFeatureMapCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    fm_cond_and_attributes: Optional[Any]
    def __init__(self) -> None:
        """Initialize FMFeatureMapCondition."""
        super().__init__()
        self.fm_cond_and_attributes: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMapCondition":
        """Deserialize XML element to FMFeatureMapCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureMapCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse fm_cond_and_attributes
        child = ARObject._find_child_element(element, "FM-COND-AND-ATTRIBUTES")
        if child is not None:
            fm_cond_and_attributes_value = child.text
            obj.fm_cond_and_attributes = fm_cond_and_attributes_value

        return obj



class FMFeatureMapConditionBuilder:
    """Builder for FMFeatureMapCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapCondition = FMFeatureMapCondition()

    def build(self) -> FMFeatureMapCondition:
        """Build and return FMFeatureMapCondition object.

        Returns:
            FMFeatureMapCondition instance
        """
        # TODO: Add validation
        return self._obj
