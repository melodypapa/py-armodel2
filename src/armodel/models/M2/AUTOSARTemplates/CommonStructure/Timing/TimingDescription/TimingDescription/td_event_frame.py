"""TDEventFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 67)

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
    TDEventFrameTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventFrame(TDEventCom):
    """AUTOSAR TDEventFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    frame_ref: Optional[ARRef]
    physical_channel_ref: Optional[ARRef]
    td_event_type_enum: Optional[TDEventFrameTypeEnum]
    def __init__(self) -> None:
        """Initialize TDEventFrame."""
        super().__init__()
        self.frame_ref: Optional[ARRef] = None
        self.physical_channel_ref: Optional[ARRef] = None
        self.td_event_type_enum: Optional[TDEventFrameTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize frame_ref
        if self.frame_ref is not None:
            serialized = ARObject._serialize_item(self.frame_ref, "Frame")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-REF")
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

        # Serialize td_event_type_enum
        if self.td_event_type_enum is not None:
            serialized = ARObject._serialize_item(self.td_event_type_enum, "TDEventFrameTypeEnum")
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
    def deserialize(cls, element: ET.Element) -> "TDEventFrame":
        """Deserialize XML element to TDEventFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventFrame, cls).deserialize(element)

        # Parse frame_ref
        child = ARObject._find_child_element(element, "FRAME-REF")
        if child is not None:
            frame_ref_value = ARRef.deserialize(child)
            obj.frame_ref = frame_ref_value

        # Parse physical_channel_ref
        child = ARObject._find_child_element(element, "PHYSICAL-CHANNEL-REF")
        if child is not None:
            physical_channel_ref_value = ARRef.deserialize(child)
            obj.physical_channel_ref = physical_channel_ref_value

        # Parse td_event_type_enum
        child = ARObject._find_child_element(element, "TD-EVENT-TYPE-ENUM")
        if child is not None:
            td_event_type_enum_value = TDEventFrameTypeEnum.deserialize(child)
            obj.td_event_type_enum = td_event_type_enum_value

        return obj



class TDEventFrameBuilder:
    """Builder for TDEventFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventFrame = TDEventFrame()

    def build(self) -> TDEventFrame:
        """Build and return TDEventFrame object.

        Returns:
            TDEventFrame instance
        """
        # TODO: Add validation
        return self._obj
