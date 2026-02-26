"""ARPackage module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
        ARElement,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
        PackageableElement,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.reference_base import (
        ReferenceBase,
    )

__all__ = [
    "ARElement",
    "ARPackage",
    "PackageableElement",
    "ReferenceBase",
]
