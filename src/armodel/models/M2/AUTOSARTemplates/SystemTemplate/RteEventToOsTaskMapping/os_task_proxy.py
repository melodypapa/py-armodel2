"""OsTaskProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import (
    OsTaskPreemptabilityEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class OsTaskProxy(ARElement):
    """AUTOSAR OsTaskProxy."""

    def __init__(self) -> None:
        """Initialize OsTaskProxy."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.preemptability: Optional[OsTaskPreemptabilityEnum] = None
        self.priority: Optional[PositiveInteger] = None


class OsTaskProxyBuilder:
    """Builder for OsTaskProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OsTaskProxy = OsTaskProxy()

    def build(self) -> OsTaskProxy:
        """Build and return OsTaskProxy object.

        Returns:
            OsTaskProxy instance
        """
        # TODO: Add validation
        return self._obj
