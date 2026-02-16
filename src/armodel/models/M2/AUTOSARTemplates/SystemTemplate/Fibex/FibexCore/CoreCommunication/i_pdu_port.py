"""IPduPort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)


class IPduPort(CommConnectorPort):
    """AUTOSAR IPduPort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_pdu_signal", None, False, False, IPduSignalProcessingEnum),  # iPduSignal
        ("rx_security", None, True, False, None),  # rxSecurity
        ("timestamp_rx", None, True, False, None),  # timestampRx
        ("use_auth_data", None, True, False, None),  # useAuthData
    ]

    def __init__(self) -> None:
        """Initialize IPduPort."""
        super().__init__()
        self.i_pdu_signal: Optional[IPduSignalProcessingEnum] = None
        self.rx_security: Optional[Boolean] = None
        self.timestamp_rx: Optional[TimeValue] = None
        self.use_auth_data: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IPduPort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduPort":
        """Create IPduPort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IPduPort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IPduPort since parent returns ARObject
        return cast("IPduPort", obj)


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
