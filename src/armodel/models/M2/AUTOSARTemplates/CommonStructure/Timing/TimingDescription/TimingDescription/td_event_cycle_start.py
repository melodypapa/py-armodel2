"""TDEventCycleStart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from abc import ABC, abstractmethod


class TDEventCycleStart(TDEventCom, ABC):
    """AUTOSAR TDEventCycleStart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    cycle_repetition: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TDEventCycleStart."""
        super().__init__()
        self.cycle_repetition: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize TDEventCycleStart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventCycleStart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cycle_repetition
        if self.cycle_repetition is not None:
            serialized = ARObject._serialize_item(self.cycle_repetition, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE-REPETITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventCycleStart":
        """Deserialize XML element to TDEventCycleStart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventCycleStart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventCycleStart, cls).deserialize(element)

        # Parse cycle_repetition
        child = ARObject._find_child_element(element, "CYCLE-REPETITION")
        if child is not None:
            cycle_repetition_value = child.text
            obj.cycle_repetition = cycle_repetition_value

        return obj



class TDEventCycleStartBuilder:
    """Builder for TDEventCycleStart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventCycleStart = TDEventCycleStart()

    def build(self) -> TDEventCycleStart:
        """Build and return TDEventCycleStart object.

        Returns:
            TDEventCycleStart instance
        """
        # TODO: Add validation
        return self._obj
