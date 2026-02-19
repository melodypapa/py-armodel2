"""IEEE1722TpAafConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 642)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAafAes3DataTypeEnum,
    IEEE1722TpAafFormatEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpAafConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpAafConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aaf_aes3_data: Optional[IEEE1722TpAafAes3DataTypeEnum]
    aaf_format_enum: Optional[IEEE1722TpAafFormatEnum]
    aaf_nominal_rate: Optional[Any]
    aes3_data_type_h: Optional[PositiveInteger]
    aes3_data_type_l: Optional[PositiveInteger]
    channels_per: Optional[PositiveInteger]
    event_default: Optional[PositiveInteger]
    pcm_bit_depth: Optional[PositiveInteger]
    sparse: Optional[Boolean]
    streams_per: Optional[PositiveInteger]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAafConnection":
        """Deserialize XML element to IEEE1722TpAafConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAafConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAafConnection, cls).deserialize(element)

        # Parse aaf_aes3_data
        child = ARObject._find_child_element(element, "AAF-AES3-DATA")
        if child is not None:
            aaf_aes3_data_value = IEEE1722TpAafAes3DataTypeEnum.deserialize(child)
            obj.aaf_aes3_data = aaf_aes3_data_value

        # Parse aaf_format_enum
        child = ARObject._find_child_element(element, "AAF-FORMAT-ENUM")
        if child is not None:
            aaf_format_enum_value = IEEE1722TpAafFormatEnum.deserialize(child)
            obj.aaf_format_enum = aaf_format_enum_value

        # Parse aaf_nominal_rate
        child = ARObject._find_child_element(element, "AAF-NOMINAL-RATE")
        if child is not None:
            aaf_nominal_rate_value = child.text
            obj.aaf_nominal_rate = aaf_nominal_rate_value

        # Parse aes3_data_type_h
        child = ARObject._find_child_element(element, "AES3-DATA-TYPE-H")
        if child is not None:
            aes3_data_type_h_value = child.text
            obj.aes3_data_type_h = aes3_data_type_h_value

        # Parse aes3_data_type_l
        child = ARObject._find_child_element(element, "AES3-DATA-TYPE-L")
        if child is not None:
            aes3_data_type_l_value = child.text
            obj.aes3_data_type_l = aes3_data_type_l_value

        # Parse channels_per
        child = ARObject._find_child_element(element, "CHANNELS-PER")
        if child is not None:
            channels_per_value = child.text
            obj.channels_per = channels_per_value

        # Parse event_default
        child = ARObject._find_child_element(element, "EVENT-DEFAULT")
        if child is not None:
            event_default_value = child.text
            obj.event_default = event_default_value

        # Parse pcm_bit_depth
        child = ARObject._find_child_element(element, "PCM-BIT-DEPTH")
        if child is not None:
            pcm_bit_depth_value = child.text
            obj.pcm_bit_depth = pcm_bit_depth_value

        # Parse sparse
        child = ARObject._find_child_element(element, "SPARSE")
        if child is not None:
            sparse_value = child.text
            obj.sparse = sparse_value

        # Parse streams_per
        child = ARObject._find_child_element(element, "STREAMS-PER")
        if child is not None:
            streams_per_value = child.text
            obj.streams_per = streams_per_value

        return obj



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
