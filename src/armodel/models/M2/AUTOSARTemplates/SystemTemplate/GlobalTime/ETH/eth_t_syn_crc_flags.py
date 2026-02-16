"""EthTSynCrcFlags AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EthTSynCrcFlags(ARObject):
    """AUTOSAR EthTSynCrcFlags."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crc_correction", None, True, False, None),  # crcCorrection
        ("crc_domain", None, True, False, None),  # crcDomain
        ("crc_message", None, True, False, None),  # crcMessage
        ("crc_precise", None, True, False, None),  # crcPrecise
        ("crc_sequence_id", None, True, False, None),  # crcSequenceId
        ("crc_source_port", None, True, False, None),  # crcSourcePort
    ]

    def __init__(self) -> None:
        """Initialize EthTSynCrcFlags."""
        super().__init__()
        self.crc_correction: Optional[Boolean] = None
        self.crc_domain: Optional[Boolean] = None
        self.crc_message: Optional[Boolean] = None
        self.crc_precise: Optional[Boolean] = None
        self.crc_sequence_id: Optional[Boolean] = None
        self.crc_source_port: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthTSynCrcFlags to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTSynCrcFlags":
        """Create EthTSynCrcFlags from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthTSynCrcFlags instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthTSynCrcFlags since parent returns ARObject
        return cast("EthTSynCrcFlags", obj)


class EthTSynCrcFlagsBuilder:
    """Builder for EthTSynCrcFlags."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTSynCrcFlags = EthTSynCrcFlags()

    def build(self) -> EthTSynCrcFlags:
        """Build and return EthTSynCrcFlags object.

        Returns:
            EthTSynCrcFlags instance
        """
        # TODO: Add validation
        return self._obj
