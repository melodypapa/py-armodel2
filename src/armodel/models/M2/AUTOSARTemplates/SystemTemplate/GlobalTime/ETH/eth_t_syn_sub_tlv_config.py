"""EthTSynSubTlvConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 867)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EthTSynSubTlvConfig(ARObject):
    """AUTOSAR EthTSynSubTlvConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ofs_sub_tlv: Optional[Boolean]
    status_sub_tlv: Optional[Boolean]
    time_sub_tlv: Optional[Boolean]
    user_data_sub_tlv: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EthTSynSubTlvConfig."""
        super().__init__()
        self.ofs_sub_tlv: Optional[Boolean] = None
        self.status_sub_tlv: Optional[Boolean] = None
        self.time_sub_tlv: Optional[Boolean] = None
        self.user_data_sub_tlv: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EthTSynSubTlvConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize ofs_sub_tlv
        if self.ofs_sub_tlv is not None:
            serialized = ARObject._serialize_item(self.ofs_sub_tlv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFS-SUB-TLV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize status_sub_tlv
        if self.status_sub_tlv is not None:
            serialized = ARObject._serialize_item(self.status_sub_tlv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATUS-SUB-TLV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sub_tlv
        if self.time_sub_tlv is not None:
            serialized = ARObject._serialize_item(self.time_sub_tlv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SUB-TLV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize user_data_sub_tlv
        if self.user_data_sub_tlv is not None:
            serialized = ARObject._serialize_item(self.user_data_sub_tlv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USER-DATA-SUB-TLV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTSynSubTlvConfig":
        """Deserialize XML element to EthTSynSubTlvConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTSynSubTlvConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ofs_sub_tlv
        child = ARObject._find_child_element(element, "OFS-SUB-TLV")
        if child is not None:
            ofs_sub_tlv_value = child.text
            obj.ofs_sub_tlv = ofs_sub_tlv_value

        # Parse status_sub_tlv
        child = ARObject._find_child_element(element, "STATUS-SUB-TLV")
        if child is not None:
            status_sub_tlv_value = child.text
            obj.status_sub_tlv = status_sub_tlv_value

        # Parse time_sub_tlv
        child = ARObject._find_child_element(element, "TIME-SUB-TLV")
        if child is not None:
            time_sub_tlv_value = child.text
            obj.time_sub_tlv = time_sub_tlv_value

        # Parse user_data_sub_tlv
        child = ARObject._find_child_element(element, "USER-DATA-SUB-TLV")
        if child is not None:
            user_data_sub_tlv_value = child.text
            obj.user_data_sub_tlv = user_data_sub_tlv_value

        return obj



class EthTSynSubTlvConfigBuilder:
    """Builder for EthTSynSubTlvConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTSynSubTlvConfig = EthTSynSubTlvConfig()

    def build(self) -> EthTSynSubTlvConfig:
        """Build and return EthTSynSubTlvConfig object.

        Returns:
            EthTSynSubTlvConfig instance
        """
        # TODO: Add validation
        return self._obj
