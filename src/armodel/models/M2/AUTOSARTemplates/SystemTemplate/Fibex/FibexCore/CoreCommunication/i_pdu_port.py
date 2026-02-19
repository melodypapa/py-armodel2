"""IPduPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 304)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPduSignalProcessingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)


class IPduPort(CommConnectorPort):
    """AUTOSAR IPduPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_signal: Optional[IPduSignalProcessingEnum]
    rx_security: Optional[Boolean]
    timestamp_rx: Optional[TimeValue]
    use_auth_data: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize IPduPort."""
        super().__init__()
        self.i_pdu_signal: Optional[IPduSignalProcessingEnum] = None
        self.rx_security: Optional[Boolean] = None
        self.timestamp_rx: Optional[TimeValue] = None
        self.use_auth_data: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize IPduPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPduPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_signal
        if self.i_pdu_signal is not None:
            serialized = ARObject._serialize_item(self.i_pdu_signal, "IPduSignalProcessingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-SIGNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_security
        if self.rx_security is not None:
            serialized = ARObject._serialize_item(self.rx_security, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-SECURITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timestamp_rx
        if self.timestamp_rx is not None:
            serialized = ARObject._serialize_item(self.timestamp_rx, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMESTAMP-RX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_auth_data
        if self.use_auth_data is not None:
            serialized = ARObject._serialize_item(self.use_auth_data, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-AUTH-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduPort":
        """Deserialize XML element to IPduPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPduPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPduPort, cls).deserialize(element)

        # Parse i_pdu_signal
        child = ARObject._find_child_element(element, "I-PDU-SIGNAL")
        if child is not None:
            i_pdu_signal_value = IPduSignalProcessingEnum.deserialize(child)
            obj.i_pdu_signal = i_pdu_signal_value

        # Parse rx_security
        child = ARObject._find_child_element(element, "RX-SECURITY")
        if child is not None:
            rx_security_value = child.text
            obj.rx_security = rx_security_value

        # Parse timestamp_rx
        child = ARObject._find_child_element(element, "TIMESTAMP-RX")
        if child is not None:
            timestamp_rx_value = child.text
            obj.timestamp_rx = timestamp_rx_value

        # Parse use_auth_data
        child = ARObject._find_child_element(element, "USE-AUTH-DATA")
        if child is not None:
            use_auth_data_value = child.text
            obj.use_auth_data = use_auth_data_value

        return obj



class IPduPortBuilder:
    """Builder for IPduPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPduPort = IPduPort()

    def build(self) -> IPduPort:
        """Build and return IPduPort object.

        Returns:
            IPduPort instance
        """
        # TODO: Add validation
        return self._obj
