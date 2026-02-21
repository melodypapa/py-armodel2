"""BswInternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
    BswInternalTriggeringPoint,
)


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    """AUTOSAR BswInternalTriggerOccurredEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source_point_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswInternalTriggerOccurredEvent."""
        super().__init__()
        self.event_source_point_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswInternalTriggerOccurredEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswInternalTriggerOccurredEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_source_point_ref
        if self.event_source_point_ref is not None:
            serialized = ARObject._serialize_item(self.event_source_point_ref, "BswInternalTriggeringPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-SOURCE-POINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInternalTriggerOccurredEvent":
        """Deserialize XML element to BswInternalTriggerOccurredEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInternalTriggerOccurredEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswInternalTriggerOccurredEvent, cls).deserialize(element)

        # Parse event_source_point_ref
        child = ARObject._find_child_element(element, "EVENT-SOURCE-POINT-REF")
        if child is not None:
            event_source_point_ref_value = ARRef.deserialize(child)
            obj.event_source_point_ref = event_source_point_ref_value

        return obj



class BswInternalTriggerOccurredEventBuilder:
    """Builder for BswInternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInternalTriggerOccurredEvent = BswInternalTriggerOccurredEvent()

    def build(self) -> BswInternalTriggerOccurredEvent:
        """Build and return BswInternalTriggerOccurredEvent object.

        Returns:
            BswInternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
