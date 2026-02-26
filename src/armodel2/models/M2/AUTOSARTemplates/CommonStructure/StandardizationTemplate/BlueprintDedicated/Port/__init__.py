"""Port module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.Port.port_prototype_blueprint import (
        PortPrototypeBlueprint,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.Port.port_prototype_blueprint_init_value import (
        PortPrototypeBlueprintInitValue,
    )

__all__ = [
    "PortPrototypeBlueprint",
    "PortPrototypeBlueprintInitValue",
]
