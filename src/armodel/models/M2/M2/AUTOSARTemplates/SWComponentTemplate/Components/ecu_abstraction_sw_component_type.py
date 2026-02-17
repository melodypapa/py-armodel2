"""EcuAbstractionSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 647)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2020)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    """AUTOSAR EcuAbstractionSwComponentType."""

    def __init__(self) -> None:
        """Initialize EcuAbstractionSwComponentType."""
        super().__init__()
        self.hardwares: list[HwDescriptionEntity] = []


class EcuAbstractionSwComponentTypeBuilder:
    """Builder for EcuAbstractionSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuAbstractionSwComponentType = EcuAbstractionSwComponentType()

    def build(self) -> EcuAbstractionSwComponentType:
        """Build and return EcuAbstractionSwComponentType object.

        Returns:
            EcuAbstractionSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
