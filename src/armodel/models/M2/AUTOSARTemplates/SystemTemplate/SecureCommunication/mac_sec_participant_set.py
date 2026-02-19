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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecParticipantSet":
        """Deserialize XML element to MacSecParticipantSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecParticipantSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecParticipantSet, cls).deserialize(element)

        # Parse ethernet_cluster
        child = ARObject._find_child_element(element, "ETHERNET-CLUSTER")
        if child is not None:
            ethernet_cluster_value = ARObject._deserialize_by_tag(child, "EthernetCluster")
            obj.ethernet_cluster = ethernet_cluster_value

        # Parse mka_participants (list from container "MKA-PARTICIPANTS")
        obj.mka_participants = []
        container = ARObject._find_child_element(element, "MKA-PARTICIPANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mka_participants.append(child_value)

        return obj



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
