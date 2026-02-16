"""SenderRecArrayTypeMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecArrayTypeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "array_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SenderRecArray),
        ),  # arrayElements
        "sender_to_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TextTableMapping,
        ),  # senderToSignal
        "signal_to": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TextTableMapping,
        ),  # signalTo
    }

    def __init__(self) -> None:
        """Initialize SenderRecArrayTypeMapping."""
        super().__init__()
        self.array_elements: list[Any] = []
        self.sender_to_signal: Optional[TextTableMapping] = None
        self.signal_to: Optional[TextTableMapping] = None


class SenderRecArrayTypeMappingBuilder:
    """Builder for SenderRecArrayTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayTypeMapping = SenderRecArrayTypeMapping()

    def build(self) -> SenderRecArrayTypeMapping:
        """Build and return SenderRecArrayTypeMapping object.

        Returns:
            SenderRecArrayTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
