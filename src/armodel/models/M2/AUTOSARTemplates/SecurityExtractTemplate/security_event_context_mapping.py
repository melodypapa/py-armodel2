"""SecurityEventContextMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_mapping import (
    IdsMapping,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_instance import (
    IdsmInstance,
)


class SecurityEventContextMapping(IdsMapping):
    """AUTOSAR SecurityEventContextMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "filter_chain": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SecurityEventFilter),
        ),  # filterChain
        "idsm_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IdsmInstance,
        ),  # idsmInstance
        "mapped_securities": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SecurityEventContext),
        ),  # mappedSecurities
    }

    def __init__(self) -> None:
        """Initialize SecurityEventContextMapping."""
        super().__init__()
        self.filter_chain: Optional[Any] = None
        self.idsm_instance: Optional[IdsmInstance] = None
        self.mapped_securities: list[Any] = []


class SecurityEventContextMappingBuilder:
    """Builder for SecurityEventContextMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMapping = SecurityEventContextMapping()

    def build(self) -> SecurityEventContextMapping:
        """Build and return SecurityEventContextMapping object.

        Returns:
            SecurityEventContextMapping instance
        """
        # TODO: Add validation
        return self._obj
