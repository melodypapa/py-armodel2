"""EndToEndProtectionISignalIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 987)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 384)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class EndToEndProtectionISignalIPdu(ARObject):
    """AUTOSAR EndToEndProtectionISignalIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_offset: Optional[Integer]
    i_signal_group_ref: Optional[ARRef]
    i_signal_i_pdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EndToEndProtectionISignalIPdu."""
        super().__init__()
        self.data_offset: Optional[Integer] = None
        self.i_signal_group_ref: Optional[ARRef] = None
        self.i_signal_i_pdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndProtectionISignalIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndProtectionISignalIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_offset
        if self.data_offset is not None:
            serialized = SerializationHelper.serialize_item(self.data_offset, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-OFFSET")
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

        # Serialize i_signal_i_pdu_ref
        if self.i_signal_i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_i_pdu_ref, "ISignalIPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtectionISignalIPdu":
        """Deserialize XML element to EndToEndProtectionISignalIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndProtectionISignalIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndProtectionISignalIPdu, cls).deserialize(element)

        # Parse data_offset
        child = SerializationHelper.find_child_element(element, "DATA-OFFSET")
        if child is not None:
            data_offset_value = child.text
            obj.data_offset = data_offset_value

        # Parse i_signal_group_ref
        child = SerializationHelper.find_child_element(element, "I-SIGNAL-GROUP-REF")
        if child is not None:
            i_signal_group_ref_value = ARRef.deserialize(child)
            obj.i_signal_group_ref = i_signal_group_ref_value

        # Parse i_signal_i_pdu_ref
        child = SerializationHelper.find_child_element(element, "I-SIGNAL-I-PDU-REF")
        if child is not None:
            i_signal_i_pdu_ref_value = ARRef.deserialize(child)
            obj.i_signal_i_pdu_ref = i_signal_i_pdu_ref_value

        return obj



class EndToEndProtectionISignalIPduBuilder:
    """Builder for EndToEndProtectionISignalIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionISignalIPdu = EndToEndProtectionISignalIPdu()

    def build(self) -> EndToEndProtectionISignalIPdu:
        """Build and return EndToEndProtectionISignalIPdu object.

        Returns:
            EndToEndProtectionISignalIPdu instance
        """
        # TODO: Add validation
        return self._obj
