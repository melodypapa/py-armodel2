"""SecurityEventContextMappingApplication AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SecurityEventContextMappingApplication(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingApplication."""

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
        """Initialize SecurityEventContextMappingApplication."""
        super().__init__()
        self.affected: String = None


class SecurityEventContextMappingApplicationBuilder:
    """Builder for SecurityEventContextMappingApplication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingApplication = SecurityEventContextMappingApplication()

    def build(self) -> SecurityEventContextMappingApplication:
        """Build and return SecurityEventContextMappingApplication object.

        Returns:
            SecurityEventContextMappingApplication instance
        """
        # TODO: Add validation
        return self._obj
