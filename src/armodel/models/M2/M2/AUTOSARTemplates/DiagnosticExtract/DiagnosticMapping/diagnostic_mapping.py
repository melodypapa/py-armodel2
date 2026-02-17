"""DiagnosticMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class DiagnosticMapping(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "provider": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # provider
        "requester": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # requester
    }

    def __init__(self) -> None:
        """Initialize DiagnosticMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requester: Optional[CpSoftwareCluster] = None


class DiagnosticMappingBuilder:
    """Builder for DiagnosticMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMapping = DiagnosticMapping()

    def build(self) -> DiagnosticMapping:
        """Build and return DiagnosticMapping object.

        Returns:
            DiagnosticMapping instance
        """
        # TODO: Add validation
        return self._obj
