"""ModelRestrictionTypes module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.abstract_value_restriction import (
        AbstractValueRestriction,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.abstract_variation_restriction import (
        AbstractVariationRestriction,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.abstract_multiplicity_restriction import (
        AbstractMultiplicityRestriction,
    )

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.full_binding_time_enum import (
    FullBindingTimeEnum,
)

__all__ = [
    "AbstractMultiplicityRestriction",
    "AbstractValueRestriction",
    "AbstractVariationRestriction",
    "FullBindingTimeEnum",
]
