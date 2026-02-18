"""MacSecParticipantSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_cluster import (
    EthernetCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_kay_participant import (
    MacSecKayParticipant,
)


class MacSecParticipantSet(ARElement):
    """AUTOSAR MacSecParticipantSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ethernet_cluster: Optional[EthernetCluster]
    mka_participants: list[MacSecKayParticipant]
    def __init__(self) -> None:
        """Initialize MacSecParticipantSet."""
        super().__init__()
        self.ethernet_cluster: Optional[EthernetCluster] = None
        self.mka_participants: list[MacSecKayParticipant] = []


class MacSecParticipantSetBuilder:
    """Builder for MacSecParticipantSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecParticipantSet = MacSecParticipantSet()

    def build(self) -> MacSecParticipantSet:
        """Build and return MacSecParticipantSet object.

        Returns:
            MacSecParticipantSet instance
        """
        # TODO: Add validation
        return self._obj
