"""SenderReceiverToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1005)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverToSignalMapping(DataMapping):
    """AUTOSAR SenderReceiverToSignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_system_instance_ref: Optional[ARRef]
    sender_to_signal_ref: Optional[ARRef]
    signal_to_ref: Optional[ARRef]
    system_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SenderReceiverToSignalMapping."""
        super().__init__()
        self.data_element_system_instance_ref: Optional[ARRef] = None
        self.sender_to_signal_ref: Optional[ARRef] = None
        self.signal_to_ref: Optional[ARRef] = None
        self.system_signal: Optional[SystemSignal] = None
    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverToSignalMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverToSignalMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_system_instance_ref
        if self.data_element_system_instance_ref is not None:
            serialized = ARObject._serialize_item(self.data_element_system_instance_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-SYSTEM-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sender_to_signal_ref
        if self.sender_to_signal_ref is not None:
            serialized = ARObject._serialize_item(self.sender_to_signal_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENDER-TO-SIGNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signal_to_ref
        if self.signal_to_ref is not None:
            serialized = ARObject._serialize_item(self.signal_to_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNAL-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize system_signal
        if self.system_signal is not None:
            serialized = ARObject._serialize_item(self.system_signal, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverToSignalMapping":
        """Deserialize XML element to SenderReceiverToSignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverToSignalMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverToSignalMapping, cls).deserialize(element)

        # Parse data_element_system_instance_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT-SYSTEM-INSTANCE-REF")
        if child is not None:
            data_element_system_instance_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_system_instance_ref = data_element_system_instance_ref_value

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



class SenderReceiverToSignalMappingBuilder:
    """Builder for SenderReceiverToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverToSignalMapping = SenderReceiverToSignalMapping()

    def build(self) -> SenderReceiverToSignalMapping:
        """Build and return SenderReceiverToSignalMapping object.

        Returns:
            SenderReceiverToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
