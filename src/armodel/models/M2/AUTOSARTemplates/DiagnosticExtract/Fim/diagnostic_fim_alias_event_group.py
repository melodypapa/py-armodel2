"""DiagnosticFimAliasEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 263)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import (
    DiagnosticAbstractAliasEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    """AUTOSAR DiagnosticFimAliasEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    grouped_aliases: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventGroup."""
        super().__init__()
        self.grouped_aliases: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEventGroup":
        """Deserialize XML element to DiagnosticFimAliasEventGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimAliasEventGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse grouped_aliases (list)
        obj.grouped_aliases = []
        for child in ARObject._find_all_child_elements(element, "GROUPED-ALIASES"):
            grouped_aliases_value = child.text
            obj.grouped_aliases.append(grouped_aliases_value)

        return obj



class DiagnosticFimAliasEventGroupBuilder:
    """Builder for DiagnosticFimAliasEventGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventGroup = DiagnosticFimAliasEventGroup()

    def build(self) -> DiagnosticFimAliasEventGroup:
        """Build and return DiagnosticFimAliasEventGroup object.

        Returns:
            DiagnosticFimAliasEventGroup instance
        """
        # TODO: Add validation
        return self._obj
