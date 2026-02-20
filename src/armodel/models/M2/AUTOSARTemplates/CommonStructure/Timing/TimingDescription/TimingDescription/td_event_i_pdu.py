"""TDEventIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventIPduTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventIPdu(TDEventCom):
    """AUTOSAR TDEventIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_ref: Optional[ARRef]
    physical_channel_ref: Optional[ARRef]
    td_event_type: Optional[TDEventIPduTypeEnum]
    def __init__(self) -> None:
        """Initialize TDEventIPdu."""
        super().__init__()
        self.i_pdu_ref: Optional[ARRef] = None
        self.physical_channel_ref: Optional[ARRef] = None
        self.td_event_type: Optional[TDEventIPduTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_ref
        if self.i_pdu_ref is not None:
            serialized = ARObject._serialize_item(self.i_pdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_channel_ref
        if self.physical_channel_ref is not None:
            serialized = ARObject._serialize_item(self.physical_channel_ref, "PhysicalChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_type
        if self.td_event_type is not None:
            serialized = ARObject._serialize_item(self.td_event_type, "TDEventIPduTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventIPdu":
        """Deserialize XML element to TDEventIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventIPdu, cls).deserialize(element)

        # Parse i_pdu_ref
        child = ARObject._find_child_element(element, "I-PDU-REF")
        if child is not None:
            i_pdu_ref_value = ARRef.deserialize(child)
            obj.i_pdu_ref = i_pdu_ref_value

        # Parse physical_channel_ref
        child = ARObject._find_child_element(element, "PHYSICAL-CHANNEL-REF")
        if child is not None:
            physical_channel_ref_value = ARRef.deserialize(child)
            obj.physical_channel_ref = physical_channel_ref_value

        # Parse td_event_type
        child = ARObject._find_child_element(element, "TD-EVENT-TYPE")
        if child is not None:
            td_event_type_value = TDEventIPduTypeEnum.deserialize(child)
            obj.td_event_type = td_event_type_value

        return obj



class TDEventIPduBuilder:
    """Builder for TDEventIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventIPdu = TDEventIPdu()

    def build(self) -> TDEventIPdu:
        """Build and return TDEventIPdu object.

        Returns:
            TDEventIPdu instance
        """
        # TODO: Add validation
        return self._obj
