"""SenderReceiverToSignalMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverToSignalMapping(DataMapping):
    """AUTOSAR SenderReceiverToSignalMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_element_system_instance_ref", None, False, False, VariableDataPrototype),  # dataElementSystemInstanceRef
        ("sender_to_signal", None, False, False, TextTableMapping),  # senderToSignal
        ("signal_to", None, False, False, TextTableMapping),  # signalTo
        ("system_signal", None, False, False, SystemSignal),  # systemSignal
    ]

    def __init__(self) -> None:
        """Initialize SenderReceiverToSignalMapping."""
        super().__init__()
        self.data_element_system_instance_ref: Optional[VariableDataPrototype] = None
        self.sender_to_signal: Optional[TextTableMapping] = None
        self.signal_to: Optional[TextTableMapping] = None
        self.system_signal: Optional[SystemSignal] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SenderReceiverToSignalMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverToSignalMapping":
        """Create SenderReceiverToSignalMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SenderReceiverToSignalMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SenderReceiverToSignalMapping since parent returns ARObject
        return cast("SenderReceiverToSignalMapping", obj)


class SenderReceiverToSignalMappingBuilder:
    """Builder for SenderReceiverToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverToSignalMapping = SenderReceiverToSignalMapping()

    def build(self) -> SenderReceiverToSignalMapping:
        """Build and return SenderReceiverToSignalMapping object.

        Returns:
            SenderReceiverToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
