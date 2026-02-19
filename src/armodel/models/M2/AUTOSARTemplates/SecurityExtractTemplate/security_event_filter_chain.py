"""SecurityEventFilterChain AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_one_every_n_filter import (
    SecurityEventOneEveryNFilter,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_state_filter import (
    SecurityEventStateFilter,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_threshold_filter import (
    SecurityEventThresholdFilter,
)


class SecurityEventFilterChain(IdsCommonElement):
    """AUTOSAR SecurityEventFilterChain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aggregation: Optional[Any]
    one_every_n: Optional[SecurityEventOneEveryNFilter]
    state: Optional[SecurityEventStateFilter]
    threshold: Optional[SecurityEventThresholdFilter]
    def __init__(self) -> None:
        """Initialize SecurityEventFilterChain."""
        super().__init__()
        self.aggregation: Optional[Any] = None
        self.one_every_n: Optional[SecurityEventOneEveryNFilter] = None
        self.state: Optional[SecurityEventStateFilter] = None
        self.threshold: Optional[SecurityEventThresholdFilter] = None

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventFilterChain to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventFilterChain, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aggregation
        if self.aggregation is not None:
            serialized = ARObject._serialize_item(self.aggregation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGGREGATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize one_every_n
        if self.one_every_n is not None:
            serialized = ARObject._serialize_item(self.one_every_n, "SecurityEventOneEveryNFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONE-EVERY-N")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize state
        if self.state is not None:
            serialized = ARObject._serialize_item(self.state, "SecurityEventStateFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize threshold
        if self.threshold is not None:
            serialized = ARObject._serialize_item(self.threshold, "SecurityEventThresholdFilter")
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
    def deserialize(cls, element: ET.Element) -> "SecurityEventFilterChain":
        """Deserialize XML element to SecurityEventFilterChain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventFilterChain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventFilterChain, cls).deserialize(element)

        # Parse aggregation
        child = ARObject._find_child_element(element, "AGGREGATION")
        if child is not None:
            aggregation_value = child.text
            obj.aggregation = aggregation_value

        # Parse one_every_n
        child = ARObject._find_child_element(element, "ONE-EVERY-N")
        if child is not None:
            one_every_n_value = ARObject._deserialize_by_tag(child, "SecurityEventOneEveryNFilter")
            obj.one_every_n = one_every_n_value

        # Parse state
        child = ARObject._find_child_element(element, "STATE")
        if child is not None:
            state_value = ARObject._deserialize_by_tag(child, "SecurityEventStateFilter")
            obj.state = state_value

        # Parse threshold
        child = ARObject._find_child_element(element, "THRESHOLD")
        if child is not None:
            threshold_value = ARObject._deserialize_by_tag(child, "SecurityEventThresholdFilter")
            obj.threshold = threshold_value

        return obj



class SecurityEventFilterChainBuilder:
    """Builder for SecurityEventFilterChain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventFilterChain = SecurityEventFilterChain()

    def build(self) -> SecurityEventFilterChain:
        """Build and return SecurityEventFilterChain object.

        Returns:
            SecurityEventFilterChain instance
        """
        # TODO: Add validation
        return self._obj
