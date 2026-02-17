"""PduToFrameMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 346)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)


class PduToFrameMapping(ARObject):
    """AUTOSAR PduToFrameMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "packing_byte": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ByteOrderEnum,
        ),  # packingByte
        "pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Pdu,
        ),  # pdu
        "start_position": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # startPosition
        "update": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # update
    }

    def __init__(self) -> None:
        """Initialize PduToFrameMapping."""
        super().__init__()
        self.packing_byte: Optional[ByteOrderEnum] = None
        self.pdu: Optional[Pdu] = None
        self.start_position: Optional[Integer] = None
        self.update: Optional[Integer] = None


class PduToFrameMappingBuilder:
    """Builder for PduToFrameMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduToFrameMapping = PduToFrameMapping()

    def build(self) -> PduToFrameMapping:
        """Build and return PduToFrameMapping object.

        Returns:
            PduToFrameMapping instance
        """
        # TODO: Add validation
        return self._obj
