"""FMFeature AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 24)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_restriction import (
    FMFeatureRestriction,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_relation import (
        FMFeatureRelation,
    )



class FMFeature(ARElement):
    """AUTOSAR FMFeature."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute_defs: list[FMAttributeDef]
    decomposition_decompositions: list[FMFeature]
    maximum: Optional[BindingTimeEnum]
    minimum: Optional[BindingTimeEnum]
    relations: list[FMFeatureRelation]
    restrictions: list[FMFeatureRestriction]
    def __init__(self) -> None:
        """Initialize FMFeature."""
        super().__init__()
        self.attribute_defs: list[FMAttributeDef] = []
        self.decomposition_decompositions: list[FMFeature] = []
        self.maximum: Optional[BindingTimeEnum] = None
        self.minimum: Optional[BindingTimeEnum] = None
        self.relations: list[FMFeatureRelation] = []
        self.restrictions: list[FMFeatureRestriction] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeature":
        """Deserialize XML element to FMFeature object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeature object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse attribute_defs (list)
        obj.attribute_defs = []
        for child in ARObject._find_all_child_elements(element, "ATTRIBUTE-DEFS"):
            attribute_defs_value = ARObject._deserialize_by_tag(child, "FMAttributeDef")
            obj.attribute_defs.append(attribute_defs_value)

        # Parse decomposition_decompositions (list)
        obj.decomposition_decompositions = []
        for child in ARObject._find_all_child_elements(element, "DECOMPOSITION-DECOMPOSITIONS"):
            decomposition_decompositions_value = ARObject._deserialize_by_tag(child, "FMFeature")
            obj.decomposition_decompositions.append(decomposition_decompositions_value)

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse minimum
        child = ARObject._find_child_element(element, "MINIMUM")
        if child is not None:
            minimum_value = child.text
            obj.minimum = minimum_value

        # Parse relations (list)
        obj.relations = []
        for child in ARObject._find_all_child_elements(element, "RELATIONS"):
            relations_value = ARObject._deserialize_by_tag(child, "FMFeatureRelation")
            obj.relations.append(relations_value)

        # Parse restrictions (list)
        obj.restrictions = []
        for child in ARObject._find_all_child_elements(element, "RESTRICTIONS"):
            restrictions_value = ARObject._deserialize_by_tag(child, "FMFeatureRestriction")
            obj.restrictions.append(restrictions_value)

        return obj



class FMFeatureBuilder:
    """Builder for FMFeature."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeature = FMFeature()

    def build(self) -> FMFeature:
        """Build and return FMFeature object.

        Returns:
            FMFeature instance
        """
        # TODO: Add validation
        return self._obj
