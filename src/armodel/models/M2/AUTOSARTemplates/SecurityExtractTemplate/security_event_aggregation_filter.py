"""SecurityEventAggregationFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 24)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class SecurityEventAggregationFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventAggregationFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_data: Optional[Any]
    minimum: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize SecurityEventAggregationFilter."""
        super().__init__()
        self.context_data: Optional[Any] = None
        self.minimum: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventAggregationFilter":
        """Deserialize XML element to SecurityEventAggregationFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventAggregationFilter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventAggregationFilter, cls).deserialize(element)

        # Parse context_data
        child = ARObject._find_child_element(element, "CONTEXT-DATA")
        if child is not None:
            context_data_value = child.text
            obj.context_data = context_data_value

        # Parse minimum
        child = ARObject._find_child_element(element, "MINIMUM")
        if child is not None:
            minimum_value = child.text
            obj.minimum = minimum_value

        return obj



class SecurityEventAggregationFilterBuilder:
    """Builder for SecurityEventAggregationFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventAggregationFilter = SecurityEventAggregationFilter()

    def build(self) -> SecurityEventAggregationFilter:
        """Build and return SecurityEventAggregationFilter object.

        Returns:
            SecurityEventAggregationFilter instance
        """
        # TODO: Add validation
        return self._obj
