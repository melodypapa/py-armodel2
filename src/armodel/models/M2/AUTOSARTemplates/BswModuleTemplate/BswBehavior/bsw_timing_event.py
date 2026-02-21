"""BswTimingEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 88)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BswTimingEvent(BswScheduleEvent):
    """AUTOSAR BswTimingEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    period: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize BswTimingEvent."""
        super().__init__()
        self.period: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize BswTimingEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswTimingEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize period
        if self.period is not None:
            serialized = SerializationHelper.serialize_item(self.period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswTimingEvent":
        """Deserialize XML element to BswTimingEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswTimingEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswTimingEvent, cls).deserialize(element)

        # Parse period
        child = SerializationHelper.find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        return obj



class BswTimingEventBuilder:
    """Builder for BswTimingEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswTimingEvent = BswTimingEvent()

    def build(self) -> BswTimingEvent:
        """Build and return BswTimingEvent object.

        Returns:
            BswTimingEvent instance
        """
        # TODO: Add validation
        return self._obj
