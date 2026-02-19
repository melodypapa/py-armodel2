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
