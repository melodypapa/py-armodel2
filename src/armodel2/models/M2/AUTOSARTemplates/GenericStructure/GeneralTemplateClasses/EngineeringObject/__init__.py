"""EngineeringObject module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
        AutosarEngineeringObject,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
        EngineeringObject,
    )

__all__ = [
    "AutosarEngineeringObject",
    "EngineeringObject",
]
