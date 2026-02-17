"""SecurityEventContextMappingBswModule AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 38)

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


class SecurityEventContextMappingBswModule(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingBswModule."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "affected_bsw": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # affectedBsw
    }

    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingBswModule."""
        super().__init__()
        self.affected_bsw: Optional[String] = None


class SecurityEventContextMappingBswModuleBuilder:
    """Builder for SecurityEventContextMappingBswModule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingBswModule = SecurityEventContextMappingBswModule()

    def build(self) -> SecurityEventContextMappingBswModule:
        """Build and return SecurityEventContextMappingBswModule object.

        Returns:
            SecurityEventContextMappingBswModule instance
        """
        # TODO: Add validation
        return self._obj
