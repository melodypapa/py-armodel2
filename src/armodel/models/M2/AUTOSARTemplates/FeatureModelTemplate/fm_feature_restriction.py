"""FMFeatureRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class FMFeatureRestriction(Identifiable):
    """AUTOSAR FMFeatureRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    restriction_and_attributes: Optional[Any]
    def __init__(self) -> None:
        """Initialize FMFeatureRestriction."""
        super().__init__()
        self.restriction_and_attributes: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureRestriction":
        """Deserialize XML element to FMFeatureRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureRestriction object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse restriction_and_attributes
        child = ARObject._find_child_element(element, "RESTRICTION-AND-ATTRIBUTES")
        if child is not None:
            restriction_and_attributes_value = child.text
            obj.restriction_and_attributes = restriction_and_attributes_value

        return obj



class FMFeatureRestrictionBuilder:
    """Builder for FMFeatureRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureRestriction = FMFeatureRestriction()

    def build(self) -> FMFeatureRestriction:
        """Build and return FMFeatureRestriction object.

        Returns:
            FMFeatureRestriction instance
        """
        # TODO: Add validation
        return self._obj
