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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverToSignalGroupMapping":
        """Deserialize XML element to SenderReceiverToSignalGroupMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverToSignalGroupMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_ref = data_element_ref_value

        # Parse signal_group_ref
        child = ARObject._find_child_element(element, "SIGNAL-GROUP")
        if child is not None:
            signal_group_ref_value = ARObject._deserialize_by_tag(child, "SystemSignalGroup")
            obj.signal_group_ref = signal_group_ref_value

        # Parse type_mapping
        child = ARObject._find_child_element(element, "TYPE-MAPPING")
        if child is not None:
            type_mapping_value = ARObject._deserialize_by_tag(child, "SenderRecCompositeTypeMapping")
            obj.type_mapping = type_mapping_value

        return obj



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
