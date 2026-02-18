"""TriggerInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger_mapping import (
    TriggerMapping,
)


class TriggerInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR TriggerInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    trigger_mappings: list[TriggerMapping]
    def __init__(self) -> None:
        """Initialize TriggerInterfaceMapping."""
        super().__init__()
        self.trigger_mappings: list[TriggerMapping] = []


class TriggerInterfaceMappingBuilder:
    """Builder for TriggerInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerInterfaceMapping = TriggerInterfaceMapping()

    def build(self) -> TriggerInterfaceMapping:
        """Build and return TriggerInterfaceMapping object.

        Returns:
            TriggerInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
