"""BswOsTaskExecutionEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswOsTaskExecutionEvent(BswScheduleEvent):
    """AUTOSAR BswOsTaskExecutionEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BswOsTaskExecutionEvent."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize BswOsTaskExecutionEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswOsTaskExecutionEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswOsTaskExecutionEvent":
        """Deserialize XML element to BswOsTaskExecutionEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswOsTaskExecutionEvent object
        """
        # Delegate to parent class to handle inherited attributes
        return super(BswOsTaskExecutionEvent, cls).deserialize(element)



class BswOsTaskExecutionEventBuilder:
    """Builder for BswOsTaskExecutionEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswOsTaskExecutionEvent = BswOsTaskExecutionEvent()

    def build(self) -> BswOsTaskExecutionEvent:
        """Build and return BswOsTaskExecutionEvent object.

        Returns:
            BswOsTaskExecutionEvent instance
        """
        # TODO: Add validation
        return self._obj
