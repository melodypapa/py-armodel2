"""IdsmRateLimitation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)


class IdsmRateLimitation(Identifiable):
    """AUTOSAR IdsmRateLimitation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_events_in: PositiveInteger
    time_interval: Float
    def __init__(self) -> None:
        """Initialize IdsmRateLimitation."""
        super().__init__()
        self.max_events_in: PositiveInteger = None
        self.time_interval: Float = None

    def serialize(self) -> ET.Element:
        """Serialize IdsmRateLimitation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsmRateLimitation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_events_in
        if self.max_events_in is not None:
            serialized = SerializationHelper.serialize_item(self.max_events_in, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-EVENTS-IN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_interval
        if self.time_interval is not None:
            serialized = SerializationHelper.serialize_item(self.time_interval, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-INTERVAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmRateLimitation":
        """Deserialize XML element to IdsmRateLimitation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmRateLimitation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmRateLimitation, cls).deserialize(element)

        # Parse max_events_in
        child = SerializationHelper.find_child_element(element, "MAX-EVENTS-IN")
        if child is not None:
            max_events_in_value = child.text
            obj.max_events_in = max_events_in_value

        # Parse time_interval
        child = SerializationHelper.find_child_element(element, "TIME-INTERVAL")
        if child is not None:
            time_interval_value = child.text
            obj.time_interval = time_interval_value

        return obj



class IdsmRateLimitationBuilder:
    """Builder for IdsmRateLimitation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmRateLimitation = IdsmRateLimitation()

    def build(self) -> IdsmRateLimitation:
        """Build and return IdsmRateLimitation object.

        Returns:
            IdsmRateLimitation instance
        """
        # TODO: Add validation
        return self._obj
