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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    event_source_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataWriteCompletedEvent."""
        super().__init__()
        self.event_source_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataWriteCompletedEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataWriteCompletedEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_source_ref
        if self.event_source_ref is not None:
            serialized = ARObject._serialize_item(self.event_source_ref, "VariableAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-SOURCE-REF")
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

        # Parse event_source_ref
        child = ARObject._find_child_element(element, "EVENT-SOURCE-REF")
        if child is not None:
            event_source_ref_value = ARRef.deserialize(child)
            obj.event_source_ref = event_source_ref_value

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
