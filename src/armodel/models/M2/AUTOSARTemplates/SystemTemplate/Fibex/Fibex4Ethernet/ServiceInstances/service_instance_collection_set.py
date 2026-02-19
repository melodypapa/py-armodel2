"""ServiceInstanceCollectionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)


class ServiceInstanceCollectionSet(FibexElement):
    """AUTOSAR ServiceInstanceCollectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    service_instances: list[AbstractServiceInstance]
    def __init__(self) -> None:
        """Initialize ServiceInstanceCollectionSet."""
        super().__init__()
        self.service_instances: list[AbstractServiceInstance] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceInstanceCollectionSet":
        """Deserialize XML element to ServiceInstanceCollectionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServiceInstanceCollectionSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse service_instances (list)
        obj.service_instances = []
        for child in ARObject._find_all_child_elements(element, "SERVICE-INSTANCES"):
            service_instances_value = ARObject._deserialize_by_tag(child, "AbstractServiceInstance")
            obj.service_instances.append(service_instances_value)

        return obj



class ServiceInstanceCollectionSetBuilder:
    """Builder for ServiceInstanceCollectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceInstanceCollectionSet = ServiceInstanceCollectionSet()

    def build(self) -> ServiceInstanceCollectionSet:
        """Build and return ServiceInstanceCollectionSet object.

        Returns:
            ServiceInstanceCollectionSet instance
        """
        # TODO: Add validation
        return self._obj
