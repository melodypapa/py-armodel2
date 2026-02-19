"""SecurityEventThresholdFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class SecurityEventThresholdFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventThresholdFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interval_length: Optional[TimeValue]
    threshold: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecurityEventThresholdFilter."""
        super().__init__()
        self.interval_length: Optional[TimeValue] = None
        self.threshold: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize SecurityEventThresholdFilter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventThresholdFilter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize interval_length
        if self.interval_length is not None:
            serialized = ARObject._serialize_item(self.interval_length, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERVAL-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize threshold
        if self.threshold is not None:
            serialized = ARObject._serialize_item(self.threshold, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("THRESHOLD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventThresholdFilter":
        """Deserialize XML element to SecurityEventThresholdFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventThresholdFilter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventThresholdFilter, cls).deserialize(element)

        # Parse interval_length
        child = ARObject._find_child_element(element, "INTERVAL-LENGTH")
        if child is not None:
            interval_length_value = child.text
            obj.interval_length = interval_length_value

        # Parse threshold
        child = ARObject._find_child_element(element, "THRESHOLD")
        if child is not None:
            threshold_value = child.text
            obj.threshold = threshold_value

        return obj



class SecurityEventThresholdFilterBuilder:
    """Builder for SecurityEventThresholdFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventThresholdFilter = SecurityEventThresholdFilter()

    def build(self) -> SecurityEventThresholdFilter:
        """Build and return SecurityEventThresholdFilter object.

        Returns:
            SecurityEventThresholdFilter instance
        """
        # TODO: Add validation
        return self._obj
