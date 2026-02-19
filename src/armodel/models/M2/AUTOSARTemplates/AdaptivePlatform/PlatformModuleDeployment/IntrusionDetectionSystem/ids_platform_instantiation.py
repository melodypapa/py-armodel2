"""IdsPlatformInstantiation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_IntrusionDetectionSystem.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.AdaptiveModule.platform_module_ethernet_endpoint_configuration import (
    PlatformModuleEthernetEndpointConfiguration,
)
from abc import ABC, abstractmethod


class IdsPlatformInstantiation(Identifiable, ABC):
    """AUTOSAR IdsPlatformInstantiation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    networks: list[PlatformModuleEthernetEndpointConfiguration]
    time_base_resource: Optional[Any]
    def __init__(self) -> None:
        """Initialize IdsPlatformInstantiation."""
        super().__init__()
        self.networks: list[PlatformModuleEthernetEndpointConfiguration] = []
        self.time_base_resource: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsPlatformInstantiation":
        """Deserialize XML element to IdsPlatformInstantiation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsPlatformInstantiation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse networks (list)
        obj.networks = []
        for child in ARObject._find_all_child_elements(element, "NETWORKS"):
            networks_value = ARObject._deserialize_by_tag(child, "PlatformModuleEthernetEndpointConfiguration")
            obj.networks.append(networks_value)

        # Parse time_base_resource
        child = ARObject._find_child_element(element, "TIME-BASE-RESOURCE")
        if child is not None:
            time_base_resource_value = child.text
            obj.time_base_resource = time_base_resource_value

        return obj



class IdsPlatformInstantiationBuilder:
    """Builder for IdsPlatformInstantiation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsPlatformInstantiation = IdsPlatformInstantiation()

    def build(self) -> IdsPlatformInstantiation:
        """Build and return IdsPlatformInstantiation object.

        Returns:
            IdsPlatformInstantiation instance
        """
        # TODO: Add validation
        return self._obj
