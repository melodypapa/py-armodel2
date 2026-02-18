"""ApplicationError AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 108)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1996)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class ApplicationError(Identifiable):
    """AUTOSAR ApplicationError."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    error_code: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ApplicationError."""
        super().__init__()
        self.error_code: Optional[Integer] = None


class ApplicationErrorBuilder:
    """Builder for ApplicationError."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationError = ApplicationError()

    def build(self) -> ApplicationError:
        """Build and return ApplicationError object.

        Returns:
            ApplicationError instance
        """
        # TODO: Add validation
        return self._obj
