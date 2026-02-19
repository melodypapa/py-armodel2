"""CpSoftwareClusterServiceResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 904)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class CpSoftwareClusterServiceResource(CpSoftwareClusterResource):
    """AUTOSAR CpSoftwareClusterServiceResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    resource_needses: list[EcucContainerValue]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterServiceResource."""
        super().__init__()
        self.resource_needses: list[EcucContainerValue] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterServiceResource":
        """Deserialize XML element to CpSoftwareClusterServiceResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterServiceResource object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse resource_needses (list)
        obj.resource_needses = []
        for child in ARObject._find_all_child_elements(element, "RESOURCE-NEEDSES"):
            resource_needses_value = ARObject._deserialize_by_tag(child, "EcucContainerValue")
            obj.resource_needses.append(resource_needses_value)

        return obj



class CpSoftwareClusterServiceResourceBuilder:
    """Builder for CpSoftwareClusterServiceResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterServiceResource = CpSoftwareClusterServiceResource()

    def build(self) -> CpSoftwareClusterServiceResource:
        """Build and return CpSoftwareClusterServiceResource object.

        Returns:
            CpSoftwareClusterServiceResource instance
        """
        # TODO: Add validation
        return self._obj
