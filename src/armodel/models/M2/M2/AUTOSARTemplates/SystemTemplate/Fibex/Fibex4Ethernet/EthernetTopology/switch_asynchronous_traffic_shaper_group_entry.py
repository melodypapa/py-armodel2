"""SwitchAsynchronousTrafficShaperGroupEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SwitchAsynchronousTrafficShaperGroupEntry(Identifiable):
    """AUTOSAR SwitchAsynchronousTrafficShaperGroupEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "maximum": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maximum
    }

    def __init__(self) -> None:
        """Initialize SwitchAsynchronousTrafficShaperGroupEntry."""
        super().__init__()
        self.maximum: Optional[PositiveInteger] = None


class SwitchAsynchronousTrafficShaperGroupEntryBuilder:
    """Builder for SwitchAsynchronousTrafficShaperGroupEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchAsynchronousTrafficShaperGroupEntry = SwitchAsynchronousTrafficShaperGroupEntry()

    def build(self) -> SwitchAsynchronousTrafficShaperGroupEntry:
        """Build and return SwitchAsynchronousTrafficShaperGroupEntry object.

        Returns:
            SwitchAsynchronousTrafficShaperGroupEntry instance
        """
        # TODO: Add validation
        return self._obj
