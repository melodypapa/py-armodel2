"""ApplicationSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 231)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 71)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1998)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 205)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)


class ApplicationSwComponentType(AtomicSwComponentType):
    """AUTOSAR ApplicationSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ApplicationSwComponentType."""
        super().__init__()


class ApplicationSwComponentTypeBuilder:
    """Builder for ApplicationSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationSwComponentType = ApplicationSwComponentType()

    def build(self) -> ApplicationSwComponentType:
        """Build and return ApplicationSwComponentType object.

        Returns:
            ApplicationSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
