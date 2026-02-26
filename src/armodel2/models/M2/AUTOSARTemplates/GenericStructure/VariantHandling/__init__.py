"""VariantHandling module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.post_build_variant_criterion import (
        PostBuildVariantCriterion,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.post_build_variant_criterion_value import (
        PostBuildVariantCriterionValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.predefined_variant import (
        PredefinedVariant,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
        SwSystemconstantValueSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.variation_point import (
        VariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
        ConditionByFormula,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.post_build_variant_condition import (
        PostBuildVariantCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.post_build_variant_criterion_value_set import (
        PostBuildVariantCriterionValueSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconst_dependent_formula import (
        SwSystemconstDependentFormula,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconst_value import (
        SwSystemconstValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.evaluated_variant_set import (
        EvaluatedVariantSet,
    )

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.additional_binding_time_enum import (
    AdditionalBindingTimeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.binding_time_enum import (
    BindingTimeEnum,
)

__all__ = [
    "AdditionalBindingTimeEnum",
    "BindingTimeEnum",
    "ConditionByFormula",
    "EvaluatedVariantSet",
    "PostBuildVariantCondition",
    "PostBuildVariantCriterion",
    "PostBuildVariantCriterionValue",
    "PostBuildVariantCriterionValueSet",
    "PredefinedVariant",
    "SwSystemconstDependentFormula",
    "SwSystemconstValue",
    "SwSystemconstantValueSet",
    "VariationPoint",
]
