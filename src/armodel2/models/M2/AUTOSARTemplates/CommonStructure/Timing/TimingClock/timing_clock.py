"""TimingClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_domain import (
    GlobalTimeDomain,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TimingClock(Identifiable, ABC):
    """AUTOSAR TimingClock."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    platform_time_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PLATFORM-TIME-REF": lambda obj, elem: setattr(obj, "platform_time_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TimingClock."""
        super().__init__()
        self.platform_time_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingClock to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingClock, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize platform_time_ref
        if self.platform_time_ref is not None:
            serialized = SerializationHelper.serialize_item(self.platform_time_ref, "GlobalTimeDomain")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PLATFORM-TIME-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingClock":
        """Deserialize XML element to TimingClock object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingClock object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingClock, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PLATFORM-TIME-REF":
                setattr(obj, "platform_time_ref", ARRef.deserialize(child))

        return obj



class TimingClockBuilder(IdentifiableBuilder):
    """Builder for TimingClock with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimingClock = TimingClock()


    def with_platform_time(self, value: Optional[GlobalTimeDomain]) -> "TimingClockBuilder":
        """Set platform_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'platform_time' is required and cannot be None")
        self._obj.platform_time = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "platformTime",
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
    def build(self) -> TimingClock:
        """Build and return the TimingClock instance (abstract)."""
        raise NotImplementedError