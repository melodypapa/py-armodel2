"""ISignalToIPduMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 325)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    TransferPropertyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)


class ISignalToIPduMapping(Identifiable):
    """AUTOSAR ISignalToIPduMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_signal_ref: Optional[ARRef]
    i_signal_group_ref: Optional[ARRef]
    packing_byte: Optional[ByteOrderEnum]
    start_position: Optional[UnlimitedInteger]
    transfer_property_enum: Optional[TransferPropertyEnum]
    update: Optional[UnlimitedInteger]
    def __init__(self) -> None:
        """Initialize ISignalToIPduMapping."""
        super().__init__()
        self.i_signal_ref: Optional[ARRef] = None
        self.i_signal_group_ref: Optional[ARRef] = None
        self.packing_byte: Optional[ByteOrderEnum] = None
        self.start_position: Optional[UnlimitedInteger] = None
        self.transfer_property_enum: Optional[TransferPropertyEnum] = None
        self.update: Optional[UnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ISignalToIPduMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalToIPduMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_signal_ref
        if self.i_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_ref, "ISignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_group_ref
        if self.i_signal_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_group_ref, "ISignalGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize packing_byte
        if self.packing_byte is not None:
            serialized = SerializationHelper.serialize_item(self.packing_byte, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKING-BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize start_position
        if self.start_position is not None:
            serialized = SerializationHelper.serialize_item(self.start_position, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("START-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transfer_property_enum
        if self.transfer_property_enum is not None:
            serialized = SerializationHelper.serialize_item(self.transfer_property_enum, "TransferPropertyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFER-PROPERTY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update
        if self.update is not None:
            serialized = SerializationHelper.serialize_item(self.update, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalToIPduMapping":
        """Deserialize XML element to ISignalToIPduMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalToIPduMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalToIPduMapping, cls).deserialize(element)

        # Parse i_signal_ref
        child = SerializationHelper.find_child_element(element, "I-SIGNAL-REF")
        if child is not None:
            i_signal_ref_value = ARRef.deserialize(child)
            obj.i_signal_ref = i_signal_ref_value

        # Parse i_signal_group_ref
        child = SerializationHelper.find_child_element(element, "I-SIGNAL-GROUP-REF")
        if child is not None:
            i_signal_group_ref_value = ARRef.deserialize(child)
            obj.i_signal_group_ref = i_signal_group_ref_value

        # Parse packing_byte
        child = SerializationHelper.find_child_element(element, "PACKING-BYTE")
        if child is not None:
            packing_byte_value = ByteOrderEnum.deserialize(child)
            obj.packing_byte = packing_byte_value

        # Parse start_position
        child = SerializationHelper.find_child_element(element, "START-POSITION")
        if child is not None:
            start_position_value = child.text
            obj.start_position = start_position_value

        # Parse transfer_property_enum
        child = SerializationHelper.find_child_element(element, "TRANSFER-PROPERTY-ENUM")
        if child is not None:
            transfer_property_enum_value = TransferPropertyEnum.deserialize(child)
            obj.transfer_property_enum = transfer_property_enum_value

        # Parse update
        child = SerializationHelper.find_child_element(element, "UPDATE")
        if child is not None:
            update_value = child.text
            obj.update = update_value

        return obj



class ISignalToIPduMappingBuilder:
    """Builder for ISignalToIPduMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalToIPduMapping = ISignalToIPduMapping()

    def build(self) -> ISignalToIPduMapping:
        """Build and return ISignalToIPduMapping object.

        Returns:
            ISignalToIPduMapping instance
        """
        # TODO: Add validation
        return self._obj
