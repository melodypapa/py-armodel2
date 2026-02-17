"""EcuPartition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcuPartition(Identifiable):
    """AUTOSAR EcuPartition."""

    def __init__(self) -> None:
        """Initialize EcuPartition."""
        super().__init__()
        self.exec_in_user: Optional[Boolean] = None


class EcuPartitionBuilder:
    """Builder for EcuPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuPartition = EcuPartition()

    def build(self) -> EcuPartition:
        """Build and return EcuPartition object.

        Returns:
            EcuPartition instance
        """
        # TODO: Add validation
        return self._obj
