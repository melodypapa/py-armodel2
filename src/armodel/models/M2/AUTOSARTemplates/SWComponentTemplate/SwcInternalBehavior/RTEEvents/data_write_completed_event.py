"""DataWriteCompletedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 542)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class DataWriteCompletedEvent(RTEEvent):
    """AUTOSAR DataWriteCompletedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source: Optional[VariableAccess]
    def __init__(self) -> None:
        """Initialize DataWriteCompletedEvent."""
        super().__init__()
        self.event_source: Optional[VariableAccess] = None
    def serialize(self) -> ET.Element:
        """Serialize DataWriteCompletedEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataWriteCompletedEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_source
        if self.event_source is not None:
            serialized = ARObject._serialize_item(self.event_source, "VariableAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataWriteCompletedEvent":
        """Deserialize XML element to DataWriteCompletedEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataWriteCompletedEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataWriteCompletedEvent, cls).deserialize(element)

        # Parse event_source
        child = ARObject._find_child_element(element, "EVENT-SOURCE")
        if child is not None:
            event_source_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.event_source = event_source_value

        return obj



class DataWriteCompletedEventBuilder:
    """Builder for DataWriteCompletedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataWriteCompletedEvent = DataWriteCompletedEvent()

    def build(self) -> DataWriteCompletedEvent:
        """Build and return DataWriteCompletedEvent object.

        Returns:
            DataWriteCompletedEvent instance
        """
        # TODO: Add validation
        return self._obj
