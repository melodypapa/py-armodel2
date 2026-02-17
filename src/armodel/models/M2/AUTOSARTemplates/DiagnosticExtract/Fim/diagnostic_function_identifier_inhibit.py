"""DiagnosticFunctionIdentifierInhibit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 215)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim import (
    DiagnosticInhibitionMaskEnum,
)


class DiagnosticFunctionIdentifierInhibit(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFunctionIdentifierInhibit."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "function": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # function
        "inhibition_mask": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticInhibitionMaskEnum,
        ),  # inhibitionMask
        "inhibit_sources": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # inhibitSources
    }

    def __init__(self) -> None:
        """Initialize DiagnosticFunctionIdentifierInhibit."""
        super().__init__()
        self.function: Optional[Any] = None
        self.inhibition_mask: Optional[DiagnosticInhibitionMaskEnum] = None
        self.inhibit_sources: list[Any] = []


class DiagnosticFunctionIdentifierInhibitBuilder:
    """Builder for DiagnosticFunctionIdentifierInhibit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionIdentifierInhibit = DiagnosticFunctionIdentifierInhibit()

    def build(self) -> DiagnosticFunctionIdentifierInhibit:
        """Build and return DiagnosticFunctionIdentifierInhibit object.

        Returns:
            DiagnosticFunctionIdentifierInhibit instance
        """
        # TODO: Add validation
        return self._obj
