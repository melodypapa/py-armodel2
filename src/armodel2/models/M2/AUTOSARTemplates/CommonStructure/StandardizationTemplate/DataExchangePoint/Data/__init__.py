"""Data module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.value_restriction_with_severity import (
        ValueRestrictionWithSeverity,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.multiplicity_restriction_with_severity import (
        MultiplicityRestrictionWithSeverity,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
        VariationRestrictionWithSeverity,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_element_scope import (
        DataFormatElementScope,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_class_tailoring import (
        AbstractClassTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
        AbstractCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.aggregation_condition import (
        AggregationCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
        AttributeCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
        ClassTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_content_conditional import (
        ClassContentConditional,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.concrete_class_tailoring import (
        ConcreteClassTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.invert_condition import (
        InvertCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.primitive_attribute_condition import (
        PrimitiveAttributeCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.reference_condition import (
        ReferenceCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.textual_condition import (
        TextualCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
        AttributeTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.primitive_attribute_tailoring import (
        PrimitiveAttributeTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.aggregation_tailoring import (
        AggregationTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.reference_tailoring import (
        ReferenceTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
        ConstraintTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.sdg_tailoring import (
        SdgTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_tailoring import (
        DataFormatTailoring,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.unresolved_reference_restriction_with_severity import (
        UnresolvedReferenceRestrictionWithSeverity,
    )

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.default_value_application_strategy_enum import (
    DefaultValueApplicationStrategyEnum,
)

__all__ = [
    "AbstractClassTailoring",
    "AbstractCondition",
    "AggregationCondition",
    "AggregationTailoring",
    "AttributeCondition",
    "AttributeTailoring",
    "ClassContentConditional",
    "ClassTailoring",
    "ConcreteClassTailoring",
    "ConstraintTailoring",
    "DataFormatElementScope",
    "DataFormatTailoring",
    "DefaultValueApplicationStrategyEnum",
    "InvertCondition",
    "MultiplicityRestrictionWithSeverity",
    "PrimitiveAttributeCondition",
    "PrimitiveAttributeTailoring",
    "ReferenceCondition",
    "ReferenceTailoring",
    "SdgTailoring",
    "TextualCondition",
    "UnresolvedReferenceRestrictionWithSeverity",
    "ValueRestrictionWithSeverity",
    "VariationRestrictionWithSeverity",
]
