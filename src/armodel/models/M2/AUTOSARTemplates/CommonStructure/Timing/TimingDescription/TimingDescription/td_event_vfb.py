"""TDEventVfb AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 51)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class TDEventVfb(TimingDescriptionEvent, ABC):
    """AUTOSAR TDEventVfb."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    component: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventVfb."""
        super().__init__()
        self.component: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventVfb to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventVfb, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize component
        if self.component is not None:
            serialized = SerializationHelper.serialize_item(self.component, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVfb":
        """Deserialize XML element to TDEventVfb object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventVfb object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventVfb, cls).deserialize(element)

        # Parse component
        child = SerializationHelper.find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = child.text
            obj.component = component_value

        return obj



class TDEventVfbBuilder:
    """Builder for TDEventVfb."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfb = TDEventVfb()

    def build(self) -> TDEventVfb:
        """Build and return TDEventVfb object.

        Returns:
            TDEventVfb instance
        """
        # TODO: Add validation
        return self._obj
