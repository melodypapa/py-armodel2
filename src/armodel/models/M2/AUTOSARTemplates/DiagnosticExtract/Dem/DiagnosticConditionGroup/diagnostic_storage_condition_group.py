"""DiagnosticStorageConditionGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticConditionGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import (
    DiagnosticConditionGroup,
)


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticStorageConditionGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "storages": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DiagnosticStorage),
        ),  # storages
    }

    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionGroup."""
        super().__init__()
        self.storages: list[Any] = []


class DiagnosticStorageConditionGroupBuilder:
    """Builder for DiagnosticStorageConditionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionGroup = DiagnosticStorageConditionGroup()

    def build(self) -> DiagnosticStorageConditionGroup:
        """Build and return DiagnosticStorageConditionGroup object.

        Returns:
            DiagnosticStorageConditionGroup instance
        """
        # TODO: Add validation
        return self._obj
