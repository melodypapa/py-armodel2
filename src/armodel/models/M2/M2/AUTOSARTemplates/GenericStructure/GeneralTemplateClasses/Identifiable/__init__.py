"""Identifiable module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
        Describable,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
        Identifiable,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
        Referrable,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
        MultilanguageReferrable,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
        SingleLanguageReferrable,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.short_name_fragment import (
        ShortNameFragment,
    )

__all__ = [
    "Describable",
    "Identifiable",
    "MultilanguageReferrable",
    "Referrable",
    "ShortNameFragment",
    "SingleLanguageReferrable",
]
