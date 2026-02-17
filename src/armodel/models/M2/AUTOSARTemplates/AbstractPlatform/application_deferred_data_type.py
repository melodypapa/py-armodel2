"""ApplicationDeferredDataType AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 37)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AbstractPlatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class ApplicationDeferredDataType(ApplicationDataType):
    """AUTOSAR ApplicationDeferredDataType."""

    def __init__(self) -> None:
        """Initialize ApplicationDeferredDataType."""
        super().__init__()


class ApplicationDeferredDataTypeBuilder:
    """Builder for ApplicationDeferredDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationDeferredDataType = ApplicationDeferredDataType()

    def build(self) -> ApplicationDeferredDataType:
        """Build and return ApplicationDeferredDataType object.

        Returns:
            ApplicationDeferredDataType instance
        """
        # TODO: Add validation
        return self._obj
