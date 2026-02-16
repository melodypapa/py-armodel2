"""SenderReceiverCompositeElementToSignalMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverCompositeElementToSignalMapping(DataMapping):
    """AUTOSAR SenderReceiverCompositeElementToSignalMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_element", None, False, False, VariableDataPrototype),  # dataElement
        ("system_signal", None, False, False, SystemSignal),  # systemSignal
        ("type_mapping", None, False, False, SenderRecCompositeTypeMapping),  # typeMapping
    ]

    def __init__(self) -> None:
        """Initialize SenderReceiverCompositeElementToSignalMapping."""
        super().__init__()
        self.data_element: Optional[VariableDataPrototype] = None
        self.system_signal: Optional[SystemSignal] = None
        self.type_mapping: Optional[SenderRecCompositeTypeMapping] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SenderReceiverCompositeElementToSignalMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverCompositeElementToSignalMapping":
        """Create SenderReceiverCompositeElementToSignalMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SenderReceiverCompositeElementToSignalMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SenderReceiverCompositeElementToSignalMapping since parent returns ARObject
        return cast("SenderReceiverCompositeElementToSignalMapping", obj)


class SenderReceiverCompositeElementToSignalMappingBuilder:
    """Builder for SenderReceiverCompositeElementToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverCompositeElementToSignalMapping = SenderReceiverCompositeElementToSignalMapping()

    def build(self) -> SenderReceiverCompositeElementToSignalMapping:
        """Build and return SenderReceiverCompositeElementToSignalMapping object.

        Returns:
            SenderReceiverCompositeElementToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
