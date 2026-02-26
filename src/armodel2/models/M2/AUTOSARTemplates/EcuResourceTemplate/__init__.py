"""EcuResourceTemplate module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
        HwElement,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
        HwDescriptionEntity,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
        HwPinGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_content import (
        HwPinGroupContent,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
        HwPin,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element_connector import (
        HwElementConnector,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_connector import (
        HwPinGroupConnector,
    )
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
        HwPinConnector,
    )

__all__ = [
    "HwDescriptionEntity",
    "HwElement",
    "HwElementConnector",
    "HwPin",
    "HwPinConnector",
    "HwPinGroup",
    "HwPinGroupConnector",
    "HwPinGroupContent",
]
