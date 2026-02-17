"""SwitchStreamFilterActionDestPortModification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class SwitchStreamFilterActionDestPortModification(Identifiable):
    """AUTOSAR SwitchStreamFilterActionDestPortModification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "egress_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CouplingPort,
        ),  # egressPorts
        "modification": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwitchStreamFilter),
        ),  # modification
    }

    def __init__(self) -> None:
        """Initialize SwitchStreamFilterActionDestPortModification."""
        super().__init__()
        self.egress_ports: list[CouplingPort] = []
        self.modification: Optional[Any] = None


class SwitchStreamFilterActionDestPortModificationBuilder:
    """Builder for SwitchStreamFilterActionDestPortModification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamFilterActionDestPortModification = SwitchStreamFilterActionDestPortModification()

    def build(self) -> SwitchStreamFilterActionDestPortModification:
        """Build and return SwitchStreamFilterActionDestPortModification object.

        Returns:
            SwitchStreamFilterActionDestPortModification instance
        """
        # TODO: Add validation
        return self._obj
