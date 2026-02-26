"""HwElementCategory module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_value import (
        HwAttributeValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_type import (
        HwType,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_category import (
        HwCategory,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_def import (
        HwAttributeDef,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_literal_def import (
        HwAttributeLiteralDef,
    )

__all__ = [
    "HwAttributeDef",
    "HwAttributeLiteralDef",
    "HwAttributeValue",
    "HwCategory",
    "HwType",
]
