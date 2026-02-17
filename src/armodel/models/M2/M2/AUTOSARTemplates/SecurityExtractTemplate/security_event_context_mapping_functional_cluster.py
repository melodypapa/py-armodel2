"""SecurityEventContextMappingFunctionalCluster AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 39)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SecurityEventContextMappingFunctionalCluster(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingFunctionalCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "affected": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # affected
    }

    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingFunctionalCluster."""
        super().__init__()
        self.affected: String = None


class SecurityEventContextMappingFunctionalClusterBuilder:
    """Builder for SecurityEventContextMappingFunctionalCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingFunctionalCluster = SecurityEventContextMappingFunctionalCluster()

    def build(self) -> SecurityEventContextMappingFunctionalCluster:
        """Build and return SecurityEventContextMappingFunctionalCluster object.

        Returns:
            SecurityEventContextMappingFunctionalCluster instance
        """
        # TODO: Add validation
        return self._obj
