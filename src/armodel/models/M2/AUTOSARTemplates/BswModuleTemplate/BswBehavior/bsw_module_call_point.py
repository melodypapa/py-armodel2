"""BswModuleCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from abc import ABC, abstractmethod


class BswModuleCallPoint(Referrable, ABC):
    """AUTOSAR BswModuleCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    contexts: list[BswDistinguishedPartition]
    def __init__(self) -> None:
        """Initialize BswModuleCallPoint."""
        super().__init__()
        self.contexts: list[BswDistinguishedPartition] = []


class BswModuleCallPointBuilder:
    """Builder for BswModuleCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleCallPoint = BswModuleCallPoint()

    def build(self) -> BswModuleCallPoint:
        """Build and return BswModuleCallPoint object.

        Returns:
            BswModuleCallPoint instance
        """
        # TODO: Add validation
        return self._obj
