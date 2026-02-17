"""DiagnosticJ1939SwMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 268)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_DiagnosticJ1939Mapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticJ1939SwMapping."""

    node: Optional[DiagnosticJ1939Node]
    sw_component_prototype_composition_instance_ref: Optional[SwComponentPrototype]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SwMapping."""
        super().__init__()
        self.node: Optional[DiagnosticJ1939Node] = None
        self.sw_component_prototype_composition_instance_ref: Optional[SwComponentPrototype] = None


class DiagnosticJ1939SwMappingBuilder:
    """Builder for DiagnosticJ1939SwMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939SwMapping = DiagnosticJ1939SwMapping()

    def build(self) -> DiagnosticJ1939SwMapping:
        """Build and return DiagnosticJ1939SwMapping object.

        Returns:
            DiagnosticJ1939SwMapping instance
        """
        # TODO: Add validation
        return self._obj
