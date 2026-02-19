"""NmPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 302)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class NmPdu(Pdu):
    """AUTOSAR NmPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_signal_to_i_pdu_refs: list[ARRef]
    nm_data: Optional[Boolean]
    nm_vote_information: Optional[Boolean]
    unused_bit: Optional[Integer]
    def __init__(self) -> None:
        """Initialize NmPdu."""
        super().__init__()
        self.i_signal_to_i_pdu_refs: list[ARRef] = []
        self.nm_data: Optional[Boolean] = None
        self.nm_vote_information: Optional[Boolean] = None
        self.unused_bit: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize NmPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_signal_to_i_pdu_refs (list to container "I-SIGNAL-TO-I-PDUS")
        if self.i_signal_to_i_pdu_refs:
            wrapper = ET.Element("I-SIGNAL-TO-I-PDUS")
            for item in self.i_signal_to_i_pdu_refs:
                serialized = ARObject._serialize_item(item, "ISignalToIPduMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_data
        if self.nm_data is not None:
            serialized = ARObject._serialize_item(self.nm_data, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_vote_information
        if self.nm_vote_information is not None:
            serialized = ARObject._serialize_item(self.nm_vote_information, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-VOTE-INFORMATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unused_bit
        if self.unused_bit is not None:
            serialized = ARObject._serialize_item(self.unused_bit, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNUSED-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmPdu":
        """Deserialize XML element to NmPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmPdu, cls).deserialize(element)

        # Parse i_signal_to_i_pdu_refs (list from container "I-SIGNAL-TO-I-PDUS")
        obj.i_signal_to_i_pdu_refs = []
        container = ARObject._find_child_element(element, "I-SIGNAL-TO-I-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_to_i_pdu_refs.append(child_value)

        # Parse nm_data
        child = ARObject._find_child_element(element, "NM-DATA")
        if child is not None:
            nm_data_value = child.text
            obj.nm_data = nm_data_value

        # Parse nm_vote_information
        child = ARObject._find_child_element(element, "NM-VOTE-INFORMATION")
        if child is not None:
            nm_vote_information_value = child.text
            obj.nm_vote_information = nm_vote_information_value

        # Parse unused_bit
        child = ARObject._find_child_element(element, "UNUSED-BIT")
        if child is not None:
            unused_bit_value = child.text
            obj.unused_bit = unused_bit_value

        return obj



class NmPduBuilder:
    """Builder for NmPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmPdu = NmPdu()

    def build(self) -> NmPdu:
        """Build and return NmPdu object.

        Returns:
            NmPdu instance
        """
        # TODO: Add validation
        return self._obj
