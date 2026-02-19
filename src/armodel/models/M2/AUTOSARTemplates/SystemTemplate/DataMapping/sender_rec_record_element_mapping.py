"""SenderRecRecordElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 236)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_record: Optional[Any]
    complex_type: Optional[SenderRecCompositeTypeMapping]
    implementation: Optional[Any]
    sender_to_signal_ref: Optional[ARRef]
    signal_to_ref: Optional[ARRef]
    system_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SenderRecRecordElementMapping."""
        super().__init__()
        self.application_record: Optional[Any] = None
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.implementation: Optional[Any] = None
        self.sender_to_signal_ref: Optional[ARRef] = None
        self.signal_to_ref: Optional[ARRef] = None
        self.system_signal: Optional[SystemSignal] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecRecordElementMapping":
        """Deserialize XML element to SenderRecRecordElementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecRecordElementMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse application_record
        child = ARObject._find_child_element(element, "APPLICATION-RECORD")
        if child is not None:
            application_record_value = child.text
            obj.application_record = application_record_value

        # Parse complex_type
        child = ARObject._find_child_element(element, "COMPLEX-TYPE")
        if child is not None:
            complex_type_value = ARObject._deserialize_by_tag(child, "SenderRecCompositeTypeMapping")
            obj.complex_type = complex_type_value

        # Parse implementation
        child = ARObject._find_child_element(element, "IMPLEMENTATION")
        if child is not None:
            implementation_value = child.text
            obj.implementation = implementation_value

        # Parse sender_to_signal_ref
        child = ARObject._find_child_element(element, "SENDER-TO-SIGNAL")
        if child is not None:
            sender_to_signal_ref_value = ARObject._deserialize_by_tag(child, "TextTableMapping")
            obj.sender_to_signal_ref = sender_to_signal_ref_value

        # Parse signal_to_ref
        child = ARObject._find_child_element(element, "SIGNAL-TO")
        if child is not None:
            signal_to_ref_value = ARObject._deserialize_by_tag(child, "TextTableMapping")
            obj.signal_to_ref = signal_to_ref_value

        # Parse system_signal
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL")
        if child is not None:
            system_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.system_signal = system_signal_value

        return obj



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
