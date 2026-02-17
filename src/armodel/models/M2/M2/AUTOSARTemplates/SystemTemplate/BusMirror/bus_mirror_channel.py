"""BusMirrorChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 698)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class BusMirrorChannel(ARObject):
    """AUTOSAR BusMirrorChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bus_mirror": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # busMirror
        "channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PhysicalChannel,
        ),  # channel
    }

    def __init__(self) -> None:
        """Initialize BusMirrorChannel."""
        super().__init__()
        self.bus_mirror: Optional[PositiveInteger] = None
        self.channel: Optional[PhysicalChannel] = None


class BusMirrorChannelBuilder:
    """Builder for BusMirrorChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannel = BusMirrorChannel()

    def build(self) -> BusMirrorChannel:
        """Build and return BusMirrorChannel object.

        Returns:
            BusMirrorChannel instance
        """
        # TODO: Add validation
        return self._obj
