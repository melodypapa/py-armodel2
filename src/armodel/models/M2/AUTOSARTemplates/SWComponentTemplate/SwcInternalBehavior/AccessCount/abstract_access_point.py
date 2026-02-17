"""AbstractAccessPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 562)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    RteApiReturnValueProvisionEnum,
)


class AbstractAccessPoint(Identifiable):
    """AUTOSAR AbstractAccessPoint."""
    """Abstract base class - do not instantiate directly."""

    return_value: Optional[RteApiReturnValueProvisionEnum]
    def __init__(self) -> None:
        """Initialize AbstractAccessPoint."""
        super().__init__()
        self.return_value: Optional[RteApiReturnValueProvisionEnum] = None


class AbstractAccessPointBuilder:
    """Builder for AbstractAccessPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractAccessPoint = AbstractAccessPoint()

    def build(self) -> AbstractAccessPoint:
        """Build and return AbstractAccessPoint object.

        Returns:
            AbstractAccessPoint instance
        """
        # TODO: Add validation
        return self._obj
