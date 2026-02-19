"""SporadicEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class SporadicEventTriggering(EventTriggeringConstraint):
    """AUTOSAR SporadicEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    jitter: Optional[MultidimensionalTime]
    maximum_inter: Optional[MultidimensionalTime]
    minimum_inter: Optional[MultidimensionalTime]
    period: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize SporadicEventTriggering."""
        super().__init__()
        self.jitter: Optional[MultidimensionalTime] = None
        self.maximum_inter: Optional[MultidimensionalTime] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.period: Optional[MultidimensionalTime] = None
    def serialize(self) -> ET.Element:
        """Serialize SporadicEventTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SporadicEventTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize jitter
        if self.jitter is not None:
            serialized = ARObject._serialize_item(self.jitter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("JITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum_inter
        if self.maximum_inter is not None:
            serialized = ARObject._serialize_item(self.maximum_inter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM-INTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_inter
        if self.minimum_inter is not None:
            serialized = ARObject._serialize_item(self.minimum_inter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-INTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period
        if self.period is not None:
            serialized = ARObject._serialize_item(self.period, "MultidimensionalTime")
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
    def deserialize(cls, element: ET.Element) -> "SporadicEventTriggering":
        """Deserialize XML element to SporadicEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SporadicEventTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SporadicEventTriggering, cls).deserialize(element)

        # Parse jitter
        child = ARObject._find_child_element(element, "JITTER")
        if child is not None:
            jitter_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.jitter = jitter_value

        # Parse maximum_inter
        child = ARObject._find_child_element(element, "MAXIMUM-INTER")
        if child is not None:
            maximum_inter_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximum_inter = maximum_inter_value

        # Parse minimum_inter
        child = ARObject._find_child_element(element, "MINIMUM-INTER")
        if child is not None:
            minimum_inter_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum_inter = minimum_inter_value

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.period = period_value

        return obj



class SporadicEventTriggeringBuilder:
    """Builder for SporadicEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SporadicEventTriggering = SporadicEventTriggering()

    def build(self) -> SporadicEventTriggering:
        """Build and return SporadicEventTriggering object.

        Returns:
            SporadicEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
