"""SoAdRoutingGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ObsoleteModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventGroupControlTypeEnum,
)


class SoAdRoutingGroup(FibexElement):
    """AUTOSAR SoAdRoutingGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EventGroupControlTypeEnum,
        ),  # eventGroup
    }

    def __init__(self) -> None:
        """Initialize SoAdRoutingGroup."""
        super().__init__()
        self.event_group: Optional[EventGroupControlTypeEnum] = None


class SoAdRoutingGroupBuilder:
    """Builder for SoAdRoutingGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoAdRoutingGroup = SoAdRoutingGroup()

    def build(self) -> SoAdRoutingGroup:
        """Build and return SoAdRoutingGroup object.

        Returns:
            SoAdRoutingGroup instance
        """
        # TODO: Add validation
        return self._obj
