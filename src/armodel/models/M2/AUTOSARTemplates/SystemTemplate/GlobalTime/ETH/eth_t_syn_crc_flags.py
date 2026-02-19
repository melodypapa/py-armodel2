"""EthTSynCrcFlags AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 868)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EthTSynCrcFlags(ARObject):
    """AUTOSAR EthTSynCrcFlags."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crc_correction: Optional[Boolean]
    crc_domain: Optional[Boolean]
    crc_message: Optional[Boolean]
    crc_precise: Optional[Boolean]
    crc_sequence_id: Optional[Boolean]
    crc_source_port: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EthTSynCrcFlags."""
        super().__init__()
        self.crc_correction: Optional[Boolean] = None
        self.crc_domain: Optional[Boolean] = None
        self.crc_message: Optional[Boolean] = None
        self.crc_precise: Optional[Boolean] = None
        self.crc_sequence_id: Optional[Boolean] = None
        self.crc_source_port: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize EthTSynCrcFlags to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize crc_correction
        if self.crc_correction is not None:
            serialized = ARObject._serialize_item(self.crc_correction, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_domain
        if self.crc_domain is not None:
            serialized = ARObject._serialize_item(self.crc_domain, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-DOMAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_message
        if self.crc_message is not None:
            serialized = ARObject._serialize_item(self.crc_message, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-MESSAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_precise
        if self.crc_precise is not None:
            serialized = ARObject._serialize_item(self.crc_precise, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-PRECISE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_sequence_id
        if self.crc_sequence_id is not None:
            serialized = ARObject._serialize_item(self.crc_sequence_id, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-SEQUENCE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_source_port
        if self.crc_source_port is not None:
            serialized = ARObject._serialize_item(self.crc_source_port, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-SOURCE-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTSynCrcFlags":
        """Deserialize XML element to EthTSynCrcFlags object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTSynCrcFlags object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse crc_correction
        child = ARObject._find_child_element(element, "CRC-CORRECTION")
        if child is not None:
            crc_correction_value = child.text
            obj.crc_correction = crc_correction_value

        # Parse crc_domain
        child = ARObject._find_child_element(element, "CRC-DOMAIN")
        if child is not None:
            crc_domain_value = child.text
            obj.crc_domain = crc_domain_value

        # Parse crc_message
        child = ARObject._find_child_element(element, "CRC-MESSAGE")
        if child is not None:
            crc_message_value = child.text
            obj.crc_message = crc_message_value

        # Parse crc_precise
        child = ARObject._find_child_element(element, "CRC-PRECISE")
        if child is not None:
            crc_precise_value = child.text
            obj.crc_precise = crc_precise_value

        # Parse crc_sequence_id
        child = ARObject._find_child_element(element, "CRC-SEQUENCE-ID")
        if child is not None:
            crc_sequence_id_value = child.text
            obj.crc_sequence_id = crc_sequence_id_value

        # Parse crc_source_port
        child = ARObject._find_child_element(element, "CRC-SOURCE-PORT")
        if child is not None:
            crc_source_port_value = child.text
            obj.crc_source_port = crc_source_port_value

        return obj



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
