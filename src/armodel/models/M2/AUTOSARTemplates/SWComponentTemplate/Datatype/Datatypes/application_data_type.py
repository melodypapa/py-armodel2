"""ApplicationDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 299)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 232)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1996)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 34)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)


class ApplicationDataType(AutosarDataType):
    """AUTOSAR ApplicationDataType."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize ApplicationDataType."""
        super().__init__()


class ApplicationDataTypeBuilder:
    """Builder for ApplicationDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationDataType = ApplicationDataType()

    def build(self) -> ApplicationDataType:
        """Build and return ApplicationDataType object.

        Returns:
            ApplicationDataType instance
        """
        # TODO: Add validation
        return self._obj
