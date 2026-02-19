"""FMFeatureMapElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map import (
        FMFeatureMap,
    )



class FMFeatureMapElement(Identifiable):
    """AUTOSAR FMFeatureMapElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assertions: list[FMFeatureMap]
    conditions: list[FMFeatureMap]
    post_build_variants: list[Any]
    sw_value_sets: list[SwSystemconstantValueSet]
    def __init__(self) -> None:
        """Initialize FMFeatureMapElement."""
        super().__init__()
        self.assertions: list[FMFeatureMap] = []
        self.conditions: list[FMFeatureMap] = []
        self.post_build_variants: list[Any] = []
        self.sw_value_sets: list[SwSystemconstantValueSet] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMapElement":
        """Deserialize XML element to FMFeatureMapElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureMapElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse assertions (list)
        obj.assertions = []
        for child in ARObject._find_all_child_elements(element, "ASSERTIONS"):
            assertions_value = ARObject._deserialize_by_tag(child, "FMFeatureMap")
            obj.assertions.append(assertions_value)

        # Parse conditions (list)
        obj.conditions = []
        for child in ARObject._find_all_child_elements(element, "CONDITIONS"):
            conditions_value = ARObject._deserialize_by_tag(child, "FMFeatureMap")
            obj.conditions.append(conditions_value)

        # Parse post_build_variants (list)
        obj.post_build_variants = []
        for child in ARObject._find_all_child_elements(element, "POST-BUILD-VARIANTS"):
            post_build_variants_value = child.text
            obj.post_build_variants.append(post_build_variants_value)

        # Parse sw_value_sets (list)
        obj.sw_value_sets = []
        for child in ARObject._find_all_child_elements(element, "SW-VALUE-SETS"):
            sw_value_sets_value = ARObject._deserialize_by_tag(child, "SwSystemconstantValueSet")
            obj.sw_value_sets.append(sw_value_sets_value)

        return obj



class FMFeatureMapElementBuilder:
    """Builder for FMFeatureMapElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapElement = FMFeatureMapElement()

    def build(self) -> FMFeatureMapElement:
        """Build and return FMFeatureMapElement object.

        Returns:
            FMFeatureMapElement instance
        """
        # TODO: Add validation
        return self._obj
