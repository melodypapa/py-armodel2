"""ConsumedProvidedServiceInstanceGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 523)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ConsumedProvidedServiceInstanceGroup(FibexElement):
    """AUTOSAR ConsumedProvidedServiceInstanceGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consumed_services: list[Any]
    provided_services: list[Any]
    def __init__(self) -> None:
        """Initialize ConsumedProvidedServiceInstanceGroup."""
        super().__init__()
        self.consumed_services: list[Any] = []
        self.provided_services: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedProvidedServiceInstanceGroup":
        """Deserialize XML element to ConsumedProvidedServiceInstanceGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsumedProvidedServiceInstanceGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsumedProvidedServiceInstanceGroup, cls).deserialize(element)

        # Parse consumed_services (list from container "CONSUMED-SERVICES")
        obj.consumed_services = []
        container = ARObject._find_child_element(element, "CONSUMED-SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.consumed_services.append(child_value)

        # Parse provided_services (list from container "PROVIDED-SERVICES")
        obj.provided_services = []
        container = ARObject._find_child_element(element, "PROVIDED-SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_services.append(child_value)

        return obj



class ConsumedProvidedServiceInstanceGroupBuilder:
    """Builder for ConsumedProvidedServiceInstanceGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsumedProvidedServiceInstanceGroup = ConsumedProvidedServiceInstanceGroup()

    def build(self) -> ConsumedProvidedServiceInstanceGroup:
        """Build and return ConsumedProvidedServiceInstanceGroup object.

        Returns:
            ConsumedProvidedServiceInstanceGroup instance
        """
        # TODO: Add validation
        return self._obj
