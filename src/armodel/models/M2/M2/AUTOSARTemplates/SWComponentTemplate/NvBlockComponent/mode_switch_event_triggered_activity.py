"""ModeSwitchEventTriggeredActivity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.swc_mode_switch_event import (
    SwcModeSwitchEvent,
)


class ModeSwitchEventTriggeredActivity(ARObject):
    """AUTOSAR ModeSwitchEventTriggeredActivity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
        "swc_mode_switch_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwcModeSwitchEvent,
        ),  # swcModeSwitchEvent
    }

    def __init__(self) -> None:
        """Initialize ModeSwitchEventTriggeredActivity."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.swc_mode_switch_event: Optional[SwcModeSwitchEvent] = None


class ModeSwitchEventTriggeredActivityBuilder:
    """Builder for ModeSwitchEventTriggeredActivity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchEventTriggeredActivity = ModeSwitchEventTriggeredActivity()

    def build(self) -> ModeSwitchEventTriggeredActivity:
        """Build and return ModeSwitchEventTriggeredActivity object.

        Returns:
            ModeSwitchEventTriggeredActivity instance
        """
        # TODO: Add validation
        return self._obj
