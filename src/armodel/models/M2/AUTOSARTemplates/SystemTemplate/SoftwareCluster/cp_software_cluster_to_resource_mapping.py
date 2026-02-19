"""CpSoftwareClusterToResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 907)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterToResourceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provider: Optional[CpSoftwareCluster]
    requesters: list[CpSoftwareCluster]
    service: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToResourceMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requesters: list[CpSoftwareCluster] = []
        self.service: Optional[CpSoftwareCluster] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToResourceMapping":
        """Deserialize XML element to CpSoftwareClusterToResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToResourceMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse provider
        child = ARObject._find_child_element(element, "PROVIDER")
        if child is not None:
            provider_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.provider = provider_value

        # Parse requesters (list)
        obj.requesters = []
        for child in ARObject._find_all_child_elements(element, "REQUESTERS"):
            requesters_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.requesters.append(requesters_value)

        # Parse service
        child = ARObject._find_child_element(element, "SERVICE")
        if child is not None:
            service_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.service = service_value

        return obj



class CpSoftwareClusterToResourceMappingBuilder:
    """Builder for CpSoftwareClusterToResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToResourceMapping = CpSoftwareClusterToResourceMapping()

    def build(self) -> CpSoftwareClusterToResourceMapping:
        """Build and return CpSoftwareClusterToResourceMapping object.

        Returns:
            CpSoftwareClusterToResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
