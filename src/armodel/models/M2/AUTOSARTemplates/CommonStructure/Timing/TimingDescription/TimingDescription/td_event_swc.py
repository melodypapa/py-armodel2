"""TDEventSwc AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class TDEventSwc(TimingDescriptionEvent, ABC):
    """AUTOSAR TDEventSwc."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    component: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventSwc."""
        super().__init__()
        self.component: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize TDEventSwc to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventSwc, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize component
        if self.component is not None:
            serialized = ARObject._serialize_item(self.component, "Any")
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
    def deserialize(cls, element: ET.Element) -> "TDEventSwc":
        """Deserialize XML element to TDEventSwc object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventSwc object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventSwc, cls).deserialize(element)

        # Parse component
        child = ARObject._find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = child.text
            obj.component = component_value

        return obj



class TDEventSwcBuilder:
    """Builder for TDEventSwc."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwc = TDEventSwc()

    def build(self) -> TDEventSwc:
        """Build and return TDEventSwc object.

        Returns:
            TDEventSwc instance
        """
        # TODO: Add validation
        return self._obj
