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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureMapElement, cls).deserialize(element)

        # Parse assertions (list from container "ASSERTIONS")
        obj.assertions = []
        container = ARObject._find_child_element(element, "ASSERTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assertions.append(child_value)

        # Parse conditions (list from container "CONDITIONS")
        obj.conditions = []
        container = ARObject._find_child_element(element, "CONDITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.conditions.append(child_value)

        # Parse post_build_variants (list from container "POST-BUILD-VARIANTS")
        obj.post_build_variants = []
        container = ARObject._find_child_element(element, "POST-BUILD-VARIANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.post_build_variants.append(child_value)

        # Parse sw_value_sets (list from container "SW-VALUE-SETS")
        obj.sw_value_sets = []
        container = ARObject._find_child_element(element, "SW-VALUE-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_value_sets.append(child_value)

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
