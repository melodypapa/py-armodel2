"""TriggerInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 109)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2076)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerInterface(PortInterface):
    """AUTOSAR TriggerInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "triggers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Trigger,
        ),  # triggers
    }

    def __init__(self) -> None:
        """Initialize TriggerInterface."""
        super().__init__()
        self.triggers: list[Trigger] = []


class TriggerInterfaceBuilder:
    """Builder for TriggerInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerInterface = TriggerInterface()

    def build(self) -> TriggerInterface:
        """Build and return TriggerInterface object.

        Returns:
            TriggerInterface instance
        """
        # TODO: Add validation
        return self._obj
