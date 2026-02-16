"""SenderRecArrayElementMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.indexed_array_element import (
    IndexedArrayElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SenderRecArrayElementMapping(ARObject):
    """AUTOSAR SenderRecArrayElementMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("complex_type", None, False, False, SenderRecCompositeTypeMapping),  # complexType
        ("indexed_array", None, False, False, IndexedArrayElement),  # indexedArray
        ("system_signal", None, False, False, SystemSignal),  # systemSignal
    ]

    def __init__(self) -> None:
        """Initialize SenderRecArrayElementMapping."""
        super().__init__()
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.indexed_array: Optional[IndexedArrayElement] = None
        self.system_signal: Optional[SystemSignal] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SenderRecArrayElementMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecArrayElementMapping":
        """Create SenderRecArrayElementMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SenderRecArrayElementMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SenderRecArrayElementMapping since parent returns ARObject
        return cast("SenderRecArrayElementMapping", obj)


class SenderRecArrayElementMappingBuilder:
    """Builder for SenderRecArrayElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayElementMapping = SenderRecArrayElementMapping()

    def build(self) -> SenderRecArrayElementMapping:
        """Build and return SenderRecArrayElementMapping object.

        Returns:
            SenderRecArrayElementMapping instance
        """
        # TODO: Add validation
        return self._obj
