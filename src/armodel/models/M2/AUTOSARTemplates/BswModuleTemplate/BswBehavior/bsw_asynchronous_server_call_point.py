"""BswAsynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)


class BswAsynchronousServerCallPoint(BswModuleCallPoint):
    """AUTOSAR BswAsynchronousServerCallPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "called_entry_entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleClientServerEntry,
        ),  # calledEntryEntry
    }

    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallPoint."""
        super().__init__()
        self.called_entry_entry: Optional[BswModuleClientServerEntry] = None


class BswAsynchronousServerCallPointBuilder:
    """Builder for BswAsynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallPoint = BswAsynchronousServerCallPoint()

    def build(self) -> BswAsynchronousServerCallPoint:
        """Build and return BswAsynchronousServerCallPoint object.

        Returns:
            BswAsynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
