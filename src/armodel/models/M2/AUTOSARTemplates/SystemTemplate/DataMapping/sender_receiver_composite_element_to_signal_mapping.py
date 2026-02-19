"""SenderReceiverCompositeElementToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 247)

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverCompositeElementToSignalMapping(DataMapping):
    """AUTOSAR SenderReceiverCompositeElementToSignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_ref: Optional[ARRef]
    system_signal: Optional[SystemSignal]
    type_mapping: Optional[SenderRecCompositeTypeMapping]
    def __init__(self) -> None:
        """Initialize SenderReceiverCompositeElementToSignalMapping."""
        super().__init__()
        self.data_element_ref: Optional[ARRef] = None
        self.system_signal: Optional[SystemSignal] = None
        self.type_mapping: Optional[SenderRecCompositeTypeMapping] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverCompositeElementToSignalMapping":
        """Deserialize XML element to SenderReceiverCompositeElementToSignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverCompositeElementToSignalMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_ref = data_element_ref_value

        # Parse system_signal
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL")
        if child is not None:
            system_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.system_signal = system_signal_value

        # Parse type_mapping
        child = ARObject._find_child_element(element, "TYPE-MAPPING")
        if child is not None:
            type_mapping_value = ARObject._deserialize_by_tag(child, "SenderRecCompositeTypeMapping")
            obj.type_mapping = type_mapping_value

        return obj



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
