"""NmPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class NmPdu(Pdu):
    """AUTOSAR NmPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_signal_to_i_pdus", None, False, True, ISignalToIPduMapping),  # iSignalToIPdus
        ("nm_data", None, True, False, None),  # nmData
        ("nm_vote_information", None, True, False, None),  # nmVoteInformation
        ("unused_bit", None, True, False, None),  # unusedBit
    ]

    def __init__(self) -> None:
        """Initialize NmPdu."""
        super().__init__()
        self.i_signal_to_i_pdus: list[ISignalToIPduMapping] = []
        self.nm_data: Optional[Boolean] = None
        self.nm_vote_information: Optional[Boolean] = None
        self.unused_bit: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NmPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmPdu":
        """Create NmPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NmPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NmPdu since parent returns ARObject
        return cast("NmPdu", obj)


class NmPduBuilder:
    """Builder for NmPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmPdu = NmPdu()

    def build(self) -> NmPdu:
        """Build and return NmPdu object.

        Returns:
            NmPdu instance
        """
        # TODO: Add validation
        return self._obj
