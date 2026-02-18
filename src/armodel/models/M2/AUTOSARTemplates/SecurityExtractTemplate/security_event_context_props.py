"""SecurityEventContextProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 258)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 33)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_definition import (
    SecurityEventDefinition,
)


class SecurityEventContextProps(Identifiable):
    """AUTOSAR SecurityEventContextProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_data: Optional[Any]
    default: Optional[Any]
    persistent: Optional[Boolean]
    security_event: Optional[SecurityEventDefinition]
    sensor_instance: Optional[PositiveInteger]
    severity: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecurityEventContextProps."""
        super().__init__()
        self.context_data: Optional[Any] = None
        self.default: Optional[Any] = None
        self.persistent: Optional[Boolean] = None
        self.security_event: Optional[SecurityEventDefinition] = None
        self.sensor_instance: Optional[PositiveInteger] = None
        self.severity: Optional[PositiveInteger] = None


class SecurityEventContextPropsBuilder:
    """Builder for SecurityEventContextProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextProps = SecurityEventContextProps()

    def build(self) -> SecurityEventContextProps:
        """Build and return SecurityEventContextProps object.

        Returns:
            SecurityEventContextProps instance
        """
        # TODO: Add validation
        return self._obj
