"""FeatureModelTemplate module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_model import (
        FMFeatureModel,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
        FMFeature,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
        FMAttributeDef,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_decomposition import (
        FMFeatureDecomposition,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_restriction import (
        FMFeatureRestriction,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_relation import (
        FMFeatureRelation,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection import (
        FMFeatureSelection,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_value import (
        FMAttributeValue,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection_set import (
        FMFeatureSelectionSet,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map import (
        FMFeatureMap,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map_element import (
        FMFeatureMapElement,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map_condition import (
        FMFeatureMapCondition,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map_assertion import (
        FMFeatureMapAssertion,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_formula_by_features_and_attributes import (
        FMFormulaByFeaturesAndAttributes,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_condition_by_features_and_attributes import (
        FMConditionByFeaturesAndAttributes,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_formula_by_features_and_sw_systemconsts import (
        FMFormulaByFeaturesAndSwSystemconsts,
    )
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_condition_by_features_and_sw_systemconsts import (
        FMConditionByFeaturesAndSwSystemconsts,
    )

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection_state import (
    FMFeatureSelectionState,
)

__all__ = [
    "FMAttributeDef",
    "FMAttributeValue",
    "FMConditionByFeaturesAndAttributes",
    "FMConditionByFeaturesAndSwSystemconsts",
    "FMFeature",
    "FMFeatureDecomposition",
    "FMFeatureMap",
    "FMFeatureMapAssertion",
    "FMFeatureMapCondition",
    "FMFeatureMapElement",
    "FMFeatureModel",
    "FMFeatureRelation",
    "FMFeatureRestriction",
    "FMFeatureSelection",
    "FMFeatureSelectionSet",
    "FMFeatureSelectionState",
    "FMFormulaByFeaturesAndAttributes",
    "FMFormulaByFeaturesAndSwSystemconsts",
]
