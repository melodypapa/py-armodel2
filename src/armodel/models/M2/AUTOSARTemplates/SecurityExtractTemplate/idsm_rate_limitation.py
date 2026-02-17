"""IdsmRateLimitation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)


class IdsmRateLimitation(Identifiable):
    """AUTOSAR IdsmRateLimitation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_events_in": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # maxEventsIn
        "time_interval": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # timeInterval
    }

    def __init__(self) -> None:
        """Initialize IdsmRateLimitation."""
        super().__init__()
        self.max_events_in: PositiveInteger = None
        self.time_interval: Float = None


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
