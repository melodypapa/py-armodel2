"""SenderReceiverToSignalGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_ref: Optional[ARRef]
    signal_group_ref: Optional[ARRef]
    type_mapping: Optional[SenderRecCompositeTypeMapping]
    def __init__(self) -> None:
        """Initialize SenderReceiverToSignalGroupMapping."""
        super().__init__()
        self.data_element_ref: Optional[ARRef] = None
        self.signal_group_ref: Optional[ARRef] = None
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
