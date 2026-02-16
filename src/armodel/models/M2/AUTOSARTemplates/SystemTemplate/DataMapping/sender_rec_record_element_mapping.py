"""SenderRecRecordElementMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SenderRecRecordElementMapping(ARObject):
    """AUTOSAR SenderRecRecordElementMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("application_record", None, False, False, any (ApplicationRecord)),  # applicationRecord
        ("complex_type", None, False, False, SenderRecCompositeTypeMapping),  # complexType
        ("implementation", None, False, False, any (ImplementationData)),  # implementation
        ("sender_to_signal", None, False, False, TextTableMapping),  # senderToSignal
        ("signal_to", None, False, False, TextTableMapping),  # signalTo
        ("system_signal", None, False, False, SystemSignal),  # systemSignal
    ]

    def __init__(self) -> None:
        """Initialize SenderRecRecordElementMapping."""
        super().__init__()
        self.application_record: Optional[Any] = None
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.implementation: Optional[Any] = None
        self.sender_to_signal: Optional[TextTableMapping] = None
        self.signal_to: Optional[TextTableMapping] = None
        self.system_signal: Optional[SystemSignal] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SenderRecRecordElementMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecRecordElementMapping":
        """Create SenderRecRecordElementMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SenderRecRecordElementMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SenderRecRecordElementMapping since parent returns ARObject
        return cast("SenderRecRecordElementMapping", obj)


class SenderRecRecordElementMappingBuilder:
    """Builder for SenderRecRecordElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecRecordElementMapping = SenderRecRecordElementMapping()

    def build(self) -> SenderRecRecordElementMapping:
        """Build and return SenderRecRecordElementMapping object.

        Returns:
            SenderRecRecordElementMapping instance
        """
        # TODO: Add validation
        return self._obj
