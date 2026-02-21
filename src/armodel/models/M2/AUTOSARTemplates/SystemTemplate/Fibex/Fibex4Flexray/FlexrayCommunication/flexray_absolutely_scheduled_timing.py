"""FlexrayAbsolutelyScheduledTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)


class FlexrayAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR FlexrayAbsolutelyScheduledTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication_cycle_cycle: Optional[CommunicationCycle]
    slot_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize FlexrayAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.slot_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayAbsolutelyScheduledTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize communication_cycle_cycle
        if self.communication_cycle_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.communication_cycle_cycle, "CommunicationCycle")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CYCLE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slot_id
        if self.slot_id is not None:
            serialized = SerializationHelper.serialize_item(self.slot_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLOT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayAbsolutelyScheduledTiming":
        """Deserialize XML element to FlexrayAbsolutelyScheduledTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayAbsolutelyScheduledTiming object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication_cycle_cycle
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CYCLE-CYCLE")
        if child is not None:
            communication_cycle_cycle_value = SerializationHelper.deserialize_by_tag(child, "CommunicationCycle")
            obj.communication_cycle_cycle = communication_cycle_cycle_value

        # Parse slot_id
        child = SerializationHelper.find_child_element(element, "SLOT-ID")
        if child is not None:
            slot_id_value = child.text
            obj.slot_id = slot_id_value

        return obj



class FlexrayAbsolutelyScheduledTimingBuilder:
    """Builder for FlexrayAbsolutelyScheduledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayAbsolutelyScheduledTiming = FlexrayAbsolutelyScheduledTiming()

    def build(self) -> FlexrayAbsolutelyScheduledTiming:
        """Build and return FlexrayAbsolutelyScheduledTiming object.

        Returns:
            FlexrayAbsolutelyScheduledTiming instance
        """
        # TODO: Add validation
        return self._obj
