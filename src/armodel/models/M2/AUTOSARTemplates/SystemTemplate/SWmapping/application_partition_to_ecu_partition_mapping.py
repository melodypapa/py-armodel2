"""ApplicationPartitionToEcuPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_partition import (
    EcuPartition,
)


class ApplicationPartitionToEcuPartitionMapping(Identifiable):
    """AUTOSAR ApplicationPartitionToEcuPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[ApplicationPartition]
    ecu_partition: Optional[EcuPartition]
    def __init__(self) -> None:
        """Initialize ApplicationPartitionToEcuPartitionMapping."""
        super().__init__()
        self.applications: list[ApplicationPartition] = []
        self.ecu_partition: Optional[EcuPartition] = None


class ApplicationPartitionToEcuPartitionMappingBuilder:
    """Builder for ApplicationPartitionToEcuPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationPartitionToEcuPartitionMapping = ApplicationPartitionToEcuPartitionMapping()

    def build(self) -> ApplicationPartitionToEcuPartitionMapping:
        """Build and return ApplicationPartitionToEcuPartitionMapping object.

        Returns:
            ApplicationPartitionToEcuPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
