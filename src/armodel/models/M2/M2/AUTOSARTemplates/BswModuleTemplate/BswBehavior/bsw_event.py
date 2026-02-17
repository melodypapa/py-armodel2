"""BswEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 87)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class BswEvent(AbstractEvent):
    """AUTOSAR BswEvent."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "contexts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswDistinguishedPartition,
        ),  # contexts
        "disabled_in_mode_description_instance_refs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeDeclaration,
        ),  # disabledInModeDescriptionInstanceRefs
        "starts_on_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntity,
        ),  # startsOnEvent
    }

    def __init__(self) -> None:
        """Initialize BswEvent."""
        super().__init__()
        self.contexts: list[BswDistinguishedPartition] = []
        self.disabled_in_mode_description_instance_refs: list[ModeDeclaration] = []
        self.starts_on_event: Optional[BswModuleEntity] = None


class BswEventBuilder:
    """Builder for BswEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEvent = BswEvent()

    def build(self) -> BswEvent:
        """Build and return BswEvent object.

        Returns:
            BswEvent instance
        """
        # TODO: Add validation
        return self._obj
