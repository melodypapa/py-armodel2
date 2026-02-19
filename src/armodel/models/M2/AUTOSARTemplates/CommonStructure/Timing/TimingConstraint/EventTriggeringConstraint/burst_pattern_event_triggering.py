"""BurstPatternEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class BurstPatternEventTriggering(EventTriggeringConstraint):
    """AUTOSAR BurstPatternEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of: Optional[PositiveInteger]
    minimum_inter: Optional[MultidimensionalTime]
    min_number_of: Optional[PositiveInteger]
    pattern_jitter: Optional[MultidimensionalTime]
    pattern_length: Optional[MultidimensionalTime]
    pattern_period: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize BurstPatternEventTriggering."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.min_number_of: Optional[PositiveInteger] = None
        self.pattern_jitter: Optional[MultidimensionalTime] = None
        self.pattern_length: Optional[MultidimensionalTime] = None
        self.pattern_period: Optional[MultidimensionalTime] = None
    def serialize(self) -> ET.Element:
        """Serialize BurstPatternEventTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BurstPatternEventTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = ARObject._serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
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

        # Serialize min_number_of
        if self.min_number_of is not None:
            serialized = ARObject._serialize_item(self.min_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern_jitter
        if self.pattern_jitter is not None:
            serialized = ARObject._serialize_item(self.pattern_jitter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-JITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern_length
        if self.pattern_length is not None:
            serialized = ARObject._serialize_item(self.pattern_length, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern_period
        if self.pattern_period is not None:
            serialized = ARObject._serialize_item(self.pattern_period, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BurstPatternEventTriggering":
        """Deserialize XML element to BurstPatternEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BurstPatternEventTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BurstPatternEventTriggering, cls).deserialize(element)

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse minimum_inter
        child = ARObject._find_child_element(element, "MINIMUM-INTER")
        if child is not None:
            minimum_inter_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum_inter = minimum_inter_value

        # Parse min_number_of
        child = ARObject._find_child_element(element, "MIN-NUMBER-OF")
        if child is not None:
            min_number_of_value = child.text
            obj.min_number_of = min_number_of_value

        # Parse pattern_jitter
        child = ARObject._find_child_element(element, "PATTERN-JITTER")
        if child is not None:
            pattern_jitter_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_jitter = pattern_jitter_value

        # Parse pattern_length
        child = ARObject._find_child_element(element, "PATTERN-LENGTH")
        if child is not None:
            pattern_length_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_length = pattern_length_value

        # Parse pattern_period
        child = ARObject._find_child_element(element, "PATTERN-PERIOD")
        if child is not None:
            pattern_period_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_period = pattern_period_value

        return obj



class BurstPatternEventTriggeringBuilder:
    """Builder for BurstPatternEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BurstPatternEventTriggering = BurstPatternEventTriggering()

    def build(self) -> BurstPatternEventTriggering:
        """Build and return BurstPatternEventTriggering object.

        Returns:
            BurstPatternEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
