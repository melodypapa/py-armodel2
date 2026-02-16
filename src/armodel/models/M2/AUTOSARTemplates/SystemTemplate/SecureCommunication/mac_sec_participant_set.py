"""MacSecParticipantSet AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ethernet_cluster", None, False, False, EthernetCluster),  # ethernetCluster
        ("mka_participants", None, False, True, MacSecKayParticipant),  # mkaParticipants
    ]

    def __init__(self) -> None:
        """Initialize MacSecParticipantSet."""
        super().__init__()
        self.ethernet_cluster: Optional[EthernetCluster] = None
        self.mka_participants: list[MacSecKayParticipant] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacSecParticipantSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecParticipantSet":
        """Create MacSecParticipantSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacSecParticipantSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacSecParticipantSet since parent returns ARObject
        return cast("MacSecParticipantSet", obj)


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
