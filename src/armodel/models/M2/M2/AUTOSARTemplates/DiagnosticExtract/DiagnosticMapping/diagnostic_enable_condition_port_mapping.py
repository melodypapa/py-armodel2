"""DiagnosticEnableConditionPortMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticEnableConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticEnableConditionPortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "enable_condition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticEnable),
        ),  # enableCondition
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
        """Initialize DiagnosticEnableConditionPortMapping."""
        super().__init__()
        self.enable_condition: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None


class DiagnosticEnableConditionPortMappingBuilder:
    """Builder for DiagnosticEnableConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionPortMapping = DiagnosticEnableConditionPortMapping()

    def build(self) -> DiagnosticEnableConditionPortMapping:
        """Build and return DiagnosticEnableConditionPortMapping object.

        Returns:
            DiagnosticEnableConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
