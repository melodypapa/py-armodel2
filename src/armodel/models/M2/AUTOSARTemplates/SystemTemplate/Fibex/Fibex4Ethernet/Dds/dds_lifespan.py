"""DdsLifespan AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 536)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLifespan(ARObject):
    """AUTOSAR DdsLifespan."""

    def __init__(self) -> None:
        """Initialize DdsLifespan."""
        super().__init__()
        self.lifespan_duration: Optional[Float] = None


class DdsLifespanBuilder:
    """Builder for DdsLifespan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLifespan = DdsLifespan()

    def build(self) -> DdsLifespan:
        """Build and return DdsLifespan object.

        Returns:
            DdsLifespan instance
        """
        # TODO: Add validation
        return self._obj
