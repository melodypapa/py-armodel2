"""ApplicationCompositeDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 241)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1996)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from abc import ABC, abstractmethod


class ApplicationCompositeDataType(ApplicationDataType, ABC):
    """AUTOSAR ApplicationCompositeDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize ApplicationCompositeDataType."""
        super().__init__()


class ApplicationCompositeDataTypeBuilder:
    """Builder for ApplicationCompositeDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeDataType = ApplicationCompositeDataType()

    def build(self) -> ApplicationCompositeDataType:
        """Build and return ApplicationCompositeDataType object.

        Returns:
            ApplicationCompositeDataType instance
        """
        # TODO: Add validation
        return self._obj
