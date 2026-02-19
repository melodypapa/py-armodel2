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
    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverCompositeElementToSignalMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverCompositeElementToSignalMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = ARObject._serialize_item(self.data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT")
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

        # Serialize type_mapping
        if self.type_mapping is not None:
            serialized = ARObject._serialize_item(self.type_mapping, "SenderRecCompositeTypeMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-MAPPING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverCompositeElementToSignalMapping":
        """Deserialize XML element to SenderReceiverCompositeElementToSignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverCompositeElementToSignalMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverCompositeElementToSignalMapping, cls).deserialize(element)

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
