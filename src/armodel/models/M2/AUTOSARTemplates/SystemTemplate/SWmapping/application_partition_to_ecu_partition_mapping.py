"""ApplicationPartitionToEcuPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "applications": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ApplicationPartition,
        ),  # applications
        "ecu_partition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcuPartition,
        ),  # ecuPartition
    }

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
