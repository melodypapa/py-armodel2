"""EndToEndProtectionISignalIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 987)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 384)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    i_signal_i_pdu: Optional[ISignalIPdu]
    def __init__(self) -> None:
        """Initialize EndToEndProtectionISignalIPdu."""
        super().__init__()
        self.data_offset: Optional[Integer] = None
        self.i_signal_group_ref: Optional[ARRef] = None
        self.i_signal_i_pdu: Optional[ISignalIPdu] = None
    def serialize(self) -> ET.Element:
        """Serialize EndToEndProtectionISignalIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize data_offset
        if self.data_offset is not None:
            serialized = ARObject._serialize_item(self.data_offset, "Integer")
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
            serialized = ARObject._serialize_item(self.i_signal_group_ref, "ISignalGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_i_pdu
        if self.i_signal_i_pdu is not None:
            serialized = ARObject._serialize_item(self.i_signal_i_pdu, "ISignalIPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-I-PDU")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_offset
        child = ARObject._find_child_element(element, "DATA-OFFSET")
        if child is not None:
            data_offset_value = child.text
            obj.data_offset = data_offset_value

        # Parse i_signal_group_ref
        child = ARObject._find_child_element(element, "I-SIGNAL-GROUP")
        if child is not None:
            i_signal_group_ref_value = ARObject._deserialize_by_tag(child, "ISignalGroup")
            obj.i_signal_group_ref = i_signal_group_ref_value

        # Parse i_signal_i_pdu
        child = ARObject._find_child_element(element, "I-SIGNAL-I-PDU")
        if child is not None:
            i_signal_i_pdu_value = ARObject._deserialize_by_tag(child, "ISignalIPdu")
            obj.i_signal_i_pdu = i_signal_i_pdu_value

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
