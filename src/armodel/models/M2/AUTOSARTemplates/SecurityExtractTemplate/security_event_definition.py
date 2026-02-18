"""SecurityEventDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 259)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 17)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecurityEventDefinition(IdsCommonElement):
    """AUTOSAR SecurityEventDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_symbol_name: Optional[Any]
    id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecurityEventDefinition."""
        super().__init__()
        self.event_symbol_name: Optional[Any] = None
        self.id: Optional[PositiveInteger] = None


class SecurityEventDefinitionBuilder:
    """Builder for SecurityEventDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventDefinition = SecurityEventDefinition()

    def build(self) -> SecurityEventDefinition:
        """Build and return SecurityEventDefinition object.

        Returns:
            SecurityEventDefinition instance
        """
        # TODO: Add validation
        return self._obj
