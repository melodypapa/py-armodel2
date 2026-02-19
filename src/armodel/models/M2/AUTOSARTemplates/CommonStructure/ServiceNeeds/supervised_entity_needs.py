"""SupervisedEntityNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 234)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 707)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class SupervisedEntityNeeds(ServiceNeeds):
    """AUTOSAR SupervisedEntityNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    activate_at_start: Optional[Boolean]
    checkpointses: list[Any]
    enable: Optional[Boolean]
    expected_alive: Optional[TimeValue]
    max_alive_cycle: Optional[TimeValue]
    min_alive_cycle: Optional[TimeValue]
    tolerated_failed: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SupervisedEntityNeeds."""
        super().__init__()
        self.activate_at_start: Optional[Boolean] = None
        self.checkpointses: list[Any] = []
        self.enable: Optional[Boolean] = None
        self.expected_alive: Optional[TimeValue] = None
        self.max_alive_cycle: Optional[TimeValue] = None
        self.min_alive_cycle: Optional[TimeValue] = None
        self.tolerated_failed: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SupervisedEntityNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SupervisedEntityNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize activate_at_start
        if self.activate_at_start is not None:
            serialized = ARObject._serialize_item(self.activate_at_start, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTIVATE-AT-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize checkpointses (list to container "CHECKPOINTSES")
        if self.checkpointses:
            wrapper = ET.Element("CHECKPOINTSES")
            for item in self.checkpointses:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize enable
        if self.enable is not None:
            serialized = ARObject._serialize_item(self.enable, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize expected_alive
        if self.expected_alive is not None:
            serialized = ARObject._serialize_item(self.expected_alive, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXPECTED-ALIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_alive_cycle
        if self.max_alive_cycle is not None:
            serialized = ARObject._serialize_item(self.max_alive_cycle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-ALIVE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_alive_cycle
        if self.min_alive_cycle is not None:
            serialized = ARObject._serialize_item(self.min_alive_cycle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-ALIVE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tolerated_failed
        if self.tolerated_failed is not None:
            serialized = ARObject._serialize_item(self.tolerated_failed, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOLERATED-FAILED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SupervisedEntityNeeds":
        """Deserialize XML element to SupervisedEntityNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SupervisedEntityNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SupervisedEntityNeeds, cls).deserialize(element)

        # Parse activate_at_start
        child = ARObject._find_child_element(element, "ACTIVATE-AT-START")
        if child is not None:
            activate_at_start_value = child.text
            obj.activate_at_start = activate_at_start_value

        # Parse checkpointses (list from container "CHECKPOINTSES")
        obj.checkpointses = []
        container = ARObject._find_child_element(element, "CHECKPOINTSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.checkpointses.append(child_value)

        # Parse enable
        child = ARObject._find_child_element(element, "ENABLE")
        if child is not None:
            enable_value = child.text
            obj.enable = enable_value

        # Parse expected_alive
        child = ARObject._find_child_element(element, "EXPECTED-ALIVE")
        if child is not None:
            expected_alive_value = child.text
            obj.expected_alive = expected_alive_value

        # Parse max_alive_cycle
        child = ARObject._find_child_element(element, "MAX-ALIVE-CYCLE")
        if child is not None:
            max_alive_cycle_value = child.text
            obj.max_alive_cycle = max_alive_cycle_value

        # Parse min_alive_cycle
        child = ARObject._find_child_element(element, "MIN-ALIVE-CYCLE")
        if child is not None:
            min_alive_cycle_value = child.text
            obj.min_alive_cycle = min_alive_cycle_value

        # Parse tolerated_failed
        child = ARObject._find_child_element(element, "TOLERATED-FAILED")
        if child is not None:
            tolerated_failed_value = child.text
            obj.tolerated_failed = tolerated_failed_value

        return obj



class SupervisedEntityNeedsBuilder:
    """Builder for SupervisedEntityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SupervisedEntityNeeds = SupervisedEntityNeeds()

    def build(self) -> SupervisedEntityNeeds:
        """Build and return SupervisedEntityNeeds object.

        Returns:
            SupervisedEntityNeeds instance
        """
        # TODO: Add validation
        return self._obj
