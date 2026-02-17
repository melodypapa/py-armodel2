"""SecurityEventThresholdFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class SecurityEventThresholdFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventThresholdFilter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "interval_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # intervalLength
        "threshold": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # threshold
    }

    def __init__(self) -> None:
        """Initialize SecurityEventThresholdFilter."""
        super().__init__()
        self.interval_length: Optional[TimeValue] = None
        self.threshold: Optional[PositiveInteger] = None


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
