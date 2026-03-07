"""TDEventCycleStart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import TDEventComBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "CYCLE-REPETITION": lambda obj, elem: setattr(obj, "cycle_repetition", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize TDEventCycleStart."""
        super().__init__()
        self.cycle_repetition: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventCycleStart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventCycleStart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cycle_repetition
        if self.cycle_repetition is not None:
            serialized = SerializationHelper.serialize_item(self.cycle_repetition, "Integer")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CYCLE-REPETITION":
                setattr(obj, "cycle_repetition", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class TDEventCycleStartBuilder(TDEventComBuilder):
    """Builder for TDEventCycleStart with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventCycleStart = TDEventCycleStart()


    def with_cycle_repetition(self, value: Optional[Integer]) -> "TDEventCycleStartBuilder":
        """Set cycle_repetition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'cycle_repetition' is required and cannot be None")
        self._obj.cycle_repetition = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "cycleRepetition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> TDEventCycleStart:
        """Build and return the TDEventCycleStart instance (abstract)."""
        raise NotImplementedError