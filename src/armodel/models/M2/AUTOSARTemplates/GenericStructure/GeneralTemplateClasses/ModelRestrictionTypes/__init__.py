"""ModelRestrictionTypes module."""
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.abstract_value_restriction import (
    AbstractValueRestriction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.abstract_variation_restriction import (
    AbstractVariationRestriction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.abstract_multiplicity_restriction import (
    AbstractMultiplicityRestriction,
)

__all__ = [
    "AbstractMultiplicityRestriction",
    "AbstractValueRestriction",
    "AbstractVariationRestriction",
]
