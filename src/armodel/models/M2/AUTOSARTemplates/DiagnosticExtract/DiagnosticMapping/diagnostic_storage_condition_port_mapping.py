"""DiagnosticStorageConditionPortMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticStorageConditionPortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostic_storage": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticStorage),
        ),  # diagnosticStorage
        "swc_flat_service": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwcService),
        ),  # swcFlatService
        "swc_service": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwcService),
        ),  # swcService
    }

    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionPortMapping."""
        super().__init__()
        self.diagnostic_storage: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None


class DiagnosticStorageConditionPortMappingBuilder:
    """Builder for DiagnosticStorageConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionPortMapping = DiagnosticStorageConditionPortMapping()

    def build(self) -> DiagnosticStorageConditionPortMapping:
        """Build and return DiagnosticStorageConditionPortMapping object.

        Returns:
            DiagnosticStorageConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
