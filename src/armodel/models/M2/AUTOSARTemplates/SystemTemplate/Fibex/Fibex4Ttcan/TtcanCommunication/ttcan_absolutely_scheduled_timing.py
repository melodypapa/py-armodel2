"""TtcanAbsolutelyScheduledTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 450)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication import (
    TtcanTriggerType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)


class TtcanAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR TtcanAbsolutelyScheduledTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication_cycle_cycle: Optional[CommunicationCycle]
    time_mark: Optional[Integer]
    trigger_ref: Optional[TtcanTriggerType]
    def __init__(self) -> None:
        """Initialize TtcanAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.time_mark: Optional[Integer] = None
        self.trigger_ref: Optional[TtcanTriggerType] = None

    def serialize(self) -> ET.Element:
        """Serialize TtcanAbsolutelyScheduledTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TtcanAbsolutelyScheduledTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize time_mark
        if self.time_mark is not None:
            serialized = SerializationHelper.serialize_item(self.time_mark, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-MARK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.trigger_ref, "TtcanTriggerType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanAbsolutelyScheduledTiming":
        """Deserialize XML element to TtcanAbsolutelyScheduledTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanAbsolutelyScheduledTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TtcanAbsolutelyScheduledTiming, cls).deserialize(element)

        # Parse communication_cycle_cycle
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CYCLE-CYCLE")
        if child is not None:
            communication_cycle_cycle_value = SerializationHelper.deserialize_by_tag(child, "CommunicationCycle")
            obj.communication_cycle_cycle = communication_cycle_cycle_value

        # Parse time_mark
        child = SerializationHelper.find_child_element(element, "TIME-MARK")
        if child is not None:
            time_mark_value = child.text
            obj.time_mark = time_mark_value

        # Parse trigger_ref
        child = SerializationHelper.find_child_element(element, "TRIGGER-REF")
        if child is not None:
            trigger_ref_value = ARRef.deserialize(child)
            obj.trigger_ref = trigger_ref_value

        return obj



class TtcanAbsolutelyScheduledTimingBuilder:
    """Builder for TtcanAbsolutelyScheduledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanAbsolutelyScheduledTiming = TtcanAbsolutelyScheduledTiming()

    def build(self) -> TtcanAbsolutelyScheduledTiming:
        """Build and return TtcanAbsolutelyScheduledTiming object.

        Returns:
            TtcanAbsolutelyScheduledTiming instance
        """
        # TODO: Add validation
        return self._obj
