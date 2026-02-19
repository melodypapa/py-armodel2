"""TimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from abc import ABC, abstractmethod


class TimingConstraint(Traceable, ABC):
    """AUTOSAR TimingConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    timing_condition: Optional[TimingCondition]
    def __init__(self) -> None:
        """Initialize TimingConstraint."""
        super().__init__()
        self.timing_condition: Optional[TimingCondition] = None
    def serialize(self) -> ET.Element:
        """Serialize TimingConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timing_condition
        if self.timing_condition is not None:
            serialized = ARObject._serialize_item(self.timing_condition, "TimingCondition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-CONDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingConstraint":
        """Deserialize XML element to TimingConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingConstraint, cls).deserialize(element)

        # Parse timing_condition
        child = ARObject._find_child_element(element, "TIMING-CONDITION")
        if child is not None:
            timing_condition_value = ARObject._deserialize_by_tag(child, "TimingCondition")
            obj.timing_condition = timing_condition_value

        return obj



class TimingConstraintBuilder:
    """Builder for TimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingConstraint = TimingConstraint()

    def build(self) -> TimingConstraint:
        """Build and return TimingConstraint object.

        Returns:
            TimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
