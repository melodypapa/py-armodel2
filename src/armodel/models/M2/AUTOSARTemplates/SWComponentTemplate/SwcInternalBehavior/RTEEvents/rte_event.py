"""RTEEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 327)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 208)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 238)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
        RunnableEntity,
    )

from abc import ABC, abstractmethod


class RTEEvent(AbstractEvent, ABC):
    """AUTOSAR RTEEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    disabled_mode_instance_refs: list[ModeDeclaration]
    start_on_event: Optional[RunnableEntity]
    def __init__(self) -> None:
        """Initialize RTEEvent."""
        super().__init__()
        self.disabled_mode_instance_refs: list[ModeDeclaration] = []
        self.start_on_event: Optional[RunnableEntity] = None

    def serialize(self) -> ET.Element:
        """Serialize RTEEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RTEEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize disabled_mode_instance_refs (list to container "DISABLED-MODE-INSTANCE-REFS")
        if self.disabled_mode_instance_refs:
            wrapper = ET.Element("DISABLED-MODE-INSTANCE-REFS")
            for item in self.disabled_mode_instance_refs:
                serialized = ARObject._serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize start_on_event
        if self.start_on_event is not None:
            serialized = ARObject._serialize_item(self.start_on_event, "RunnableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("START-ON-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RTEEvent":
        """Deserialize XML element to RTEEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RTEEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RTEEvent, cls).deserialize(element)

        # Parse disabled_mode_instance_refs (list from container "DISABLED-MODE-INSTANCE-REFS")
        obj.disabled_mode_instance_refs = []
        container = ARObject._find_child_element(element, "DISABLED-MODE-INSTANCE-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.disabled_mode_instance_refs.append(child_value)

        # Parse start_on_event
        child = ARObject._find_child_element(element, "START-ON-EVENT")
        if child is not None:
            start_on_event_value = ARObject._deserialize_by_tag(child, "RunnableEntity")
            obj.start_on_event = start_on_event_value

        return obj



class RTEEventBuilder:
    """Builder for RTEEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RTEEvent = RTEEvent()

    def build(self) -> RTEEvent:
        """Build and return RTEEvent object.

        Returns:
            RTEEvent instance
        """
        # TODO: Add validation
        return self._obj
