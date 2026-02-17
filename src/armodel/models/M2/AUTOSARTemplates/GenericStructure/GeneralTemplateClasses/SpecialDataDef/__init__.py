"""SpecialDataDef module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_def import (
        SdgDef,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
        SdgElementWithGid,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
        SdgClass,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
        SdgAttribute,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_primitive_attribute import (
        SdgAbstractPrimitiveAttribute,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_primitive_attribute import (
        SdgPrimitiveAttribute,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_primitive_attribute_with_variation import (
        SdgPrimitiveAttributeWithVariation,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_aggregation_with_variation import (
        SdgAggregationWithVariation,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_reference import (
        SdgReference,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_foreign_reference import (
        SdgAbstractForeignReference,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_foreign_reference import (
        SdgForeignReference,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_foreign_reference_with_variation import (
        SdgForeignReferenceWithVariation,
    )

__all__ = [
    "SdgAbstractForeignReference",
    "SdgAbstractPrimitiveAttribute",
    "SdgAggregationWithVariation",
    "SdgAttribute",
    "SdgClass",
    "SdgDef",
    "SdgElementWithGid",
    "SdgForeignReference",
    "SdgForeignReferenceWithVariation",
    "SdgPrimitiveAttribute",
    "SdgPrimitiveAttributeWithVariation",
    "SdgReference",
]
