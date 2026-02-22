"""TimingClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_domain import (
    GlobalTimeDomain,
)
from abc import ABC, abstractmethod


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
    def __init__(self) -> None:
        """Initialize TimingClock."""
        super().__init__()
        self.platform_time_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingClock to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse platform_time_ref
        child = SerializationHelper.find_child_element(element, "PLATFORM-TIME-REF")
        if child is not None:
            platform_time_ref_value = ARRef.deserialize(child)
            obj.platform_time_ref = platform_time_ref_value

        return obj



