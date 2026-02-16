"""SecurityEventAggregationFilter AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class SecurityEventAggregationFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventAggregationFilter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SecurityEventContext),
        ),  # contextData
        "minimum": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minimum
    }

    def __init__(self) -> None:
        """Initialize SecurityEventAggregationFilter."""
        super().__init__()
        self.context_data: Optional[Any] = None
        self.minimum: Optional[TimeValue] = None


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
