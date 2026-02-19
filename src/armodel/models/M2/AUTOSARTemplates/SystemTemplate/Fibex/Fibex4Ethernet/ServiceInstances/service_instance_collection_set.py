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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ServiceInstanceCollectionSet, cls).deserialize(element)

        # Parse service_instances (list from container "SERVICE-INSTANCES")
        obj.service_instances = []
        container = ARObject._find_child_element(element, "SERVICE-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.service_instances.append(child_value)

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
