"""DiagnosticEnableConditionGroup AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import (
    DiagnosticConditionGroup,
)


class DiagnosticEnableConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticEnableConditionGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "enable_conditions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DiagnosticEnable),
        ),  # enableConditions
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionGroup."""
        super().__init__()
        self.enable_conditions: list[Any] = []


class DiagnosticEnableConditionGroupBuilder:
    """Builder for DiagnosticEnableConditionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionGroup = DiagnosticEnableConditionGroup()

    def build(self) -> DiagnosticEnableConditionGroup:
        """Build and return DiagnosticEnableConditionGroup object.

        Returns:
            DiagnosticEnableConditionGroup instance
        """
        # TODO: Add validation
        return self._obj
