"""IPduMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 840)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "introduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # introduction
        "pdu_max_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pduMaxLength
        "pdur_tp_chunk": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pdurTpChunk
        "source_i_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # sourceIPdu
        "target_i_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TargetIPduRef,
        ),  # targetIPdu
    }

    def __init__(self) -> None:
        """Initialize IPduMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.pdu_max_length: Optional[PositiveInteger] = None
        self.pdur_tp_chunk: Optional[PositiveInteger] = None
        self.source_i_pdu: Optional[PduTriggering] = None
        self.target_i_pdu: Optional[TargetIPduRef] = None


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
