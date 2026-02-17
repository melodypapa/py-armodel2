"""DiagnosticFimFunctionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 264)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticFimFunctionMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticFimFunctionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mapped_bsw": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # mappedBsw
        "mapped_flat_swc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # mappedFlatSwc
        "mapped": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # mapped
        "mapped_swc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # mappedSwc
    }

    def __init__(self) -> None:
        """Initialize DiagnosticFimFunctionMapping."""
        super().__init__()
        self.mapped_bsw: Optional[Any] = None
        self.mapped_flat_swc: Optional[Any] = None
        self.mapped: Optional[Any] = None
        self.mapped_swc: Optional[Any] = None


class DiagnosticFimFunctionMappingBuilder:
    """Builder for DiagnosticFimFunctionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimFunctionMapping = DiagnosticFimFunctionMapping()

    def build(self) -> DiagnosticFimFunctionMapping:
        """Build and return DiagnosticFimFunctionMapping object.

        Returns:
            DiagnosticFimFunctionMapping instance
        """
        # TODO: Add validation
        return self._obj
