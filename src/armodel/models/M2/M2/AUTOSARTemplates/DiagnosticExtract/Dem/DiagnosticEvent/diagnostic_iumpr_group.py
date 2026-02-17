"""DiagnosticIumprGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)


class DiagnosticIumprGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumprGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "iumprs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticIumpr,
        ),  # iumprs
        "iumpr_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class="DiagnosticIumprGroup",
        ),  # iumprGroup
    }

    def __init__(self) -> None:
        """Initialize DiagnosticIumprGroup."""
        super().__init__()
        self.iumprs: list[DiagnosticIumpr] = []
        self.iumpr_group: Optional[DiagnosticIumprGroup] = None


class DiagnosticIumprGroupBuilder:
    """Builder for DiagnosticIumprGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprGroup = DiagnosticIumprGroup()

    def build(self) -> DiagnosticIumprGroup:
        """Build and return DiagnosticIumprGroup object.

        Returns:
            DiagnosticIumprGroup instance
        """
        # TODO: Add validation
        return self._obj
