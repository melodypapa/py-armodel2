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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationPartitionToEcuPartitionMapping":
        """Deserialize XML element to ApplicationPartitionToEcuPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationPartitionToEcuPartitionMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse applications (list)
        obj.applications = []
        for child in ARObject._find_all_child_elements(element, "APPLICATIONS"):
            applications_value = ARObject._deserialize_by_tag(child, "ApplicationPartition")
            obj.applications.append(applications_value)

        # Parse ecu_partition
        child = ARObject._find_child_element(element, "ECU-PARTITION")
        if child is not None:
            ecu_partition_value = ARObject._deserialize_by_tag(child, "EcuPartition")
            obj.ecu_partition = ecu_partition_value

        return obj



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
