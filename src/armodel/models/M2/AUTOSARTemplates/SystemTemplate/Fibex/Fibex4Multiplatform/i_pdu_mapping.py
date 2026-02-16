"""IPduMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.target_i_pdu_ref import (
    TargetIPduRef,
)


class IPduMapping(ARObject):
    """AUTOSAR IPduMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("introduction", None, False, False, DocumentationBlock),  # introduction
        ("pdu_max_length", None, True, False, None),  # pduMaxLength
        ("pdur_tp_chunk", None, True, False, None),  # pdurTpChunk
        ("source_i_pdu", None, False, False, PduTriggering),  # sourceIPdu
        ("target_i_pdu", None, False, False, TargetIPduRef),  # targetIPdu
    ]

    def __init__(self) -> None:
        """Initialize IPduMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.pdu_max_length: Optional[PositiveInteger] = None
        self.pdur_tp_chunk: Optional[PositiveInteger] = None
        self.source_i_pdu: Optional[PduTriggering] = None
        self.target_i_pdu: Optional[TargetIPduRef] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IPduMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduMapping":
        """Create IPduMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IPduMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IPduMapping since parent returns ARObject
        return cast("IPduMapping", obj)


class IPduMappingBuilder:
    """Builder for IPduMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPduMapping = IPduMapping()

    def build(self) -> IPduMapping:
        """Build and return IPduMapping object.

        Returns:
            IPduMapping instance
        """
        # TODO: Add validation
        return self._obj
