"""SenderReceiverToSignalGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverToSignalGroupMapping(DataMapping):
    """AUTOSAR SenderReceiverToSignalGroupMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # dataElement
        "signal_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SystemSignalGroup,
        ),  # signalGroup
        "type_mapping": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SenderRecCompositeTypeMapping,
        ),  # typeMapping
    }

    def __init__(self) -> None:
        """Initialize SenderReceiverToSignalGroupMapping."""
        super().__init__()
        self.data_element: Optional[VariableDataPrototype] = None
        self.signal_group: Optional[SystemSignalGroup] = None
        self.type_mapping: Optional[SenderRecCompositeTypeMapping] = None


class SenderReceiverToSignalGroupMappingBuilder:
    """Builder for SenderReceiverToSignalGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverToSignalGroupMapping = SenderReceiverToSignalGroupMapping()

    def build(self) -> SenderReceiverToSignalGroupMapping:
        """Build and return SenderReceiverToSignalGroupMapping object.

        Returns:
            SenderReceiverToSignalGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
