"""IEEE1722TpAafConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpAafConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpAafConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("aaf_aes3_data", None, False, False, IEEE1722TpAafAes3DataTypeEnum),  # aafAes3Data
        ("aaf_format_enum", None, False, False, IEEE1722TpAafFormatEnum),  # aafFormatEnum
        ("aaf_nominal_rate", None, False, False, any (IEEE1722TpAaf)),  # aafNominalRate
        ("aes3_data_type_h", None, True, False, None),  # aes3DataTypeH
        ("aes3_data_type_l", None, True, False, None),  # aes3DataTypeL
        ("channels_per", None, True, False, None),  # channelsPer
        ("event_default", None, True, False, None),  # eventDefault
        ("pcm_bit_depth", None, True, False, None),  # pcmBitDepth
        ("sparse", None, True, False, None),  # sparse
        ("streams_per", None, True, False, None),  # streamsPer
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpAafConnection."""
        super().__init__()
        self.aaf_aes3_data: Optional[IEEE1722TpAafAes3DataTypeEnum] = None
        self.aaf_format_enum: Optional[IEEE1722TpAafFormatEnum] = None
        self.aaf_nominal_rate: Optional[Any] = None
        self.aes3_data_type_h: Optional[PositiveInteger] = None
        self.aes3_data_type_l: Optional[PositiveInteger] = None
        self.channels_per: Optional[PositiveInteger] = None
        self.event_default: Optional[PositiveInteger] = None
        self.pcm_bit_depth: Optional[PositiveInteger] = None
        self.sparse: Optional[Boolean] = None
        self.streams_per: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpAafConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAafConnection":
        """Create IEEE1722TpAafConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpAafConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpAafConnection since parent returns ARObject
        return cast("IEEE1722TpAafConnection", obj)


class IEEE1722TpAafConnectionBuilder:
    """Builder for IEEE1722TpAafConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAafConnection = IEEE1722TpAafConnection()

    def build(self) -> IEEE1722TpAafConnection:
        """Build and return IEEE1722TpAafConnection object.

        Returns:
            IEEE1722TpAafConnection instance
        """
        # TODO: Add validation
        return self._obj
