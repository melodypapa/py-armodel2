"""InitEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 546)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class InitEvent(RTEEvent):
    """AUTOSAR InitEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize InitEvent."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize InitEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InitEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InitEvent":
        """Deserialize XML element to InitEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InitEvent object
        """
        # Delegate to parent class to handle inherited attributes
        return super(InitEvent, cls).deserialize(element)



class InitEventBuilder:
    """Builder for InitEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InitEvent = InitEvent()

    def build(self) -> InitEvent:
        """Build and return InitEvent object.

        Returns:
            InitEvent instance
        """
        # TODO: Add validation
        return self._obj
