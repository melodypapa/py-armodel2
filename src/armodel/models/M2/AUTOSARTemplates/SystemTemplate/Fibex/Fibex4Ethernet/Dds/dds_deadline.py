"""DdsDeadline AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 532)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsDeadline(ARObject):
    """AUTOSAR DdsDeadline."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    deadline_period: Optional[Float]
    def __init__(self) -> None:
        """Initialize DdsDeadline."""
        super().__init__()
        self.deadline_period: Optional[Float] = None


class DdsDeadlineBuilder:
    """Builder for DdsDeadline."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDeadline = DdsDeadline()

    def build(self) -> DdsDeadline:
        """Build and return DdsDeadline object.

        Returns:
            DdsDeadline instance
        """
        # TODO: Add validation
        return self._obj
