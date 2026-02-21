"""GlobalTimeEthMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 866)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeCrcSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_t_syn_sub_tlv_config import (
    EthTSynSubTlvConfig,
)


class GlobalTimeEthMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeEthMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crc_secured: Optional[GlobalTimeCrcSupportEnum]
    hold_over_time: Optional[TimeValue]
    sub_tlv_config: Optional[EthTSynSubTlvConfig]
    def __init__(self) -> None:
        """Initialize GlobalTimeEthMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None
        self.hold_over_time: Optional[TimeValue] = None
        self.sub_tlv_config: Optional[EthTSynSubTlvConfig] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeEthMaster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeEthMaster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crc_secured
        if self.crc_secured is not None:
            serialized = SerializationHelper.serialize_item(self.crc_secured, "GlobalTimeCrcSupportEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-SECURED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hold_over_time
        if self.hold_over_time is not None:
            serialized = SerializationHelper.serialize_item(self.hold_over_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HOLD-OVER-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_tlv_config
        if self.sub_tlv_config is not None:
            serialized = SerializationHelper.serialize_item(self.sub_tlv_config, "EthTSynSubTlvConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB-TLV-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeEthMaster":
        """Deserialize XML element to GlobalTimeEthMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeEthMaster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeEthMaster, cls).deserialize(element)

        # Parse crc_secured
        child = SerializationHelper.find_child_element(element, "CRC-SECURED")
        if child is not None:
            crc_secured_value = GlobalTimeCrcSupportEnum.deserialize(child)
            obj.crc_secured = crc_secured_value

        # Parse hold_over_time
        child = SerializationHelper.find_child_element(element, "HOLD-OVER-TIME")
        if child is not None:
            hold_over_time_value = child.text
            obj.hold_over_time = hold_over_time_value

        # Parse sub_tlv_config
        child = SerializationHelper.find_child_element(element, "SUB-TLV-CONFIG")
        if child is not None:
            sub_tlv_config_value = SerializationHelper.deserialize_by_tag(child, "EthTSynSubTlvConfig")
            obj.sub_tlv_config = sub_tlv_config_value

        return obj



class GlobalTimeEthMasterBuilder:
    """Builder for GlobalTimeEthMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeEthMaster = GlobalTimeEthMaster()

    def build(self) -> GlobalTimeEthMaster:
        """Build and return GlobalTimeEthMaster object.

        Returns:
            GlobalTimeEthMaster instance
        """
        # TODO: Add validation
        return self._obj
