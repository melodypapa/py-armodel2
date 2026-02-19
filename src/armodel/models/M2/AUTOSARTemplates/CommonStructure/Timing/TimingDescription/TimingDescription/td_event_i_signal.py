"""TDEventISignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventISignalTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventISignal(TDEventCom):
    """AUTOSAR TDEventISignal."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_signal: Optional[ISignal]
    physical_channel: Optional[PhysicalChannel]
    td_event_type_enum: Optional[TDEventISignalTypeEnum]
    def __init__(self) -> None:
        """Initialize TDEventISignal."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type_enum: Optional[TDEventISignalTypeEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize TDEventISignal to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventISignal, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_signal
        if self.i_signal is not None:
            serialized = ARObject._serialize_item(self.i_signal, "ISignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_channel
        if self.physical_channel is not None:
            serialized = ARObject._serialize_item(self.physical_channel, "PhysicalChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_type_enum
        if self.td_event_type_enum is not None:
            serialized = ARObject._serialize_item(self.td_event_type_enum, "TDEventISignalTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventISignal":
        """Deserialize XML element to TDEventISignal object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventISignal object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventISignal, cls).deserialize(element)

        # Parse i_signal
        child = ARObject._find_child_element(element, "I-SIGNAL")
        if child is not None:
            i_signal_value = ARObject._deserialize_by_tag(child, "ISignal")
            obj.i_signal = i_signal_value

        # Parse physical_channel
        child = ARObject._find_child_element(element, "PHYSICAL-CHANNEL")
        if child is not None:
            physical_channel_value = ARObject._deserialize_by_tag(child, "PhysicalChannel")
            obj.physical_channel = physical_channel_value

        # Parse td_event_type_enum
        child = ARObject._find_child_element(element, "TD-EVENT-TYPE-ENUM")
        if child is not None:
            td_event_type_enum_value = TDEventISignalTypeEnum.deserialize(child)
            obj.td_event_type_enum = td_event_type_enum_value

        return obj



class TDEventISignalBuilder:
    """Builder for TDEventISignal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventISignal = TDEventISignal()

    def build(self) -> TDEventISignal:
        """Build and return TDEventISignal object.

        Returns:
            TDEventISignal instance
        """
        # TODO: Add validation
        return self._obj
