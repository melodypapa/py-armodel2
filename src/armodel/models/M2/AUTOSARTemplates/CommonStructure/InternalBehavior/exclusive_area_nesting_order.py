"""ExclusiveAreaNestingOrder AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 84)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 554)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class ExclusiveAreaNestingOrder(Referrable):
    """AUTOSAR ExclusiveAreaNestingOrder."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    exclusive_areas: list[ExclusiveArea]
    def __init__(self) -> None:
        """Initialize ExclusiveAreaNestingOrder."""
        super().__init__()
        self.exclusive_areas: list[ExclusiveArea] = []


class ExclusiveAreaNestingOrderBuilder:
    """Builder for ExclusiveAreaNestingOrder."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExclusiveAreaNestingOrder = ExclusiveAreaNestingOrder()

    def build(self) -> ExclusiveAreaNestingOrder:
        """Build and return ExclusiveAreaNestingOrder object.

        Returns:
            ExclusiveAreaNestingOrder instance
        """
        # TODO: Add validation
        return self._obj
