"""TDEventSLLETPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_sllet import (
    TDEventSLLET,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class TDEventSLLETPort(TDEventSLLET):
    """AUTOSAR TDEventSLLETPort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortPrototype,
        ),  # port
    }

    def __init__(self) -> None:
        """Initialize TDEventSLLETPort."""
        super().__init__()
        self.port: Optional[PortPrototype] = None


class TDEventSLLETPortBuilder:
    """Builder for TDEventSLLETPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSLLETPort = TDEventSLLETPort()

    def build(self) -> TDEventSLLETPort:
        """Build and return TDEventSLLETPort object.

        Returns:
            TDEventSLLETPort instance
        """
        # TODO: Add validation
        return self._obj
