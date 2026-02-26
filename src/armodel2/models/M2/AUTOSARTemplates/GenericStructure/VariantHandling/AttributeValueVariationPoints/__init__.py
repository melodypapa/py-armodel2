"""AttributeValueVariationPoints module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.numerical_value_variation_point import (
        NumericalValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.attribute_value_variation_point import (
        AttributeValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.abstract_numerical_variation_point import (
        AbstractNumericalVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.boolean_value_variation_point import (
        BooleanValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.float_value_variation_point import (
        FloatValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.integer_value_variation_point import (
        IntegerValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.limit_value_variation_point import (
        LimitValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.positive_integer_value_variation_point import (
        PositiveIntegerValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.unlimited_integer_value_variation_point import (
        UnlimitedIntegerValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.time_value_value_variation_point import (
        TimeValueValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.abstract_enumeration_value_variation_point import (
        AbstractEnumerationValueVariationPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.enumeration_mapping_entry import (
        EnumerationMappingEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints.enumeration_mapping_table import (
        EnumerationMappingTable,
    )

__all__ = [
    "AbstractEnumerationValueVariationPoint",
    "AbstractNumericalVariationPoint",
    "AttributeValueVariationPoint",
    "BooleanValueVariationPoint",
    "EnumerationMappingEntry",
    "EnumerationMappingTable",
    "FloatValueVariationPoint",
    "IntegerValueVariationPoint",
    "LimitValueVariationPoint",
    "NumericalValueVariationPoint",
    "PositiveIntegerValueVariationPoint",
    "TimeValueValueVariationPoint",
    "UnlimitedIntegerValueVariationPoint",
]
