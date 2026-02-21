"""RteEventInSystemSeparation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 214)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInSystemSeparation(Identifiable):
    """AUTOSAR RteEventInSystemSeparation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rte_event_instance_refs: list[RTEEvent]
    def __init__(self) -> None:
        """Initialize RteEventInSystemSeparation."""
        super().__init__()
        self.rte_event_instance_refs: list[RTEEvent] = []

    def serialize(self) -> ET.Element:
        """Serialize RteEventInSystemSeparation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RteEventInSystemSeparation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rte_event_instance_refs (list to container "RTE-EVENT-INSTANCE-REFS")
        if self.rte_event_instance_refs:
            wrapper = ET.Element("RTE-EVENT-INSTANCE-REFS")
            for item in self.rte_event_instance_refs:
                serialized = ARObject._serialize_item(item, "RTEEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RteEventInSystemSeparation":
        """Deserialize XML element to RteEventInSystemSeparation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RteEventInSystemSeparation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RteEventInSystemSeparation, cls).deserialize(element)

        # Parse rte_event_instance_refs (list from container "RTE-EVENT-INSTANCE-REFS")
        obj.rte_event_instance_refs = []
        container = ARObject._find_child_element(element, "RTE-EVENT-INSTANCE-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_instance_refs.append(child_value)

        return obj



class RteEventInSystemSeparationBuilder:
    """Builder for RteEventInSystemSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInSystemSeparation = RteEventInSystemSeparation()

    def build(self) -> RteEventInSystemSeparation:
        """Build and return RteEventInSystemSeparation object.

        Returns:
            RteEventInSystemSeparation instance
        """
        # TODO: Add validation
        return self._obj
