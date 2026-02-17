"""DiagnosticAuthRole AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticAuthRole(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAuthRole."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bit_position": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # bitPosition
        "is_default": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isDefault
    }

    def __init__(self) -> None:
        """Initialize DiagnosticAuthRole."""
        super().__init__()
        self.bit_position: Optional[PositiveInteger] = None
        self.is_default: Optional[Boolean] = None


class DiagnosticAuthRoleBuilder:
    """Builder for DiagnosticAuthRole."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthRole = DiagnosticAuthRole()

    def build(self) -> DiagnosticAuthRole:
        """Build and return DiagnosticAuthRole object.

        Returns:
            DiagnosticAuthRole instance
        """
        # TODO: Add validation
        return self._obj
