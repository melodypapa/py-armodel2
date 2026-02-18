"""SomeipServiceVersion AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2059)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SomeipServiceVersion(ARObject):
    """AUTOSAR SomeipServiceVersion."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    major_version: Optional[PositiveInteger]
    minor_version: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SomeipServiceVersion."""
        super().__init__()
        self.major_version: Optional[PositiveInteger] = None
        self.minor_version: Optional[PositiveInteger] = None


class SomeipServiceVersionBuilder:
    """Builder for SomeipServiceVersion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipServiceVersion = SomeipServiceVersion()

    def build(self) -> SomeipServiceVersion:
        """Build and return SomeipServiceVersion object.

        Returns:
            SomeipServiceVersion instance
        """
        # TODO: Add validation
        return self._obj
