"""SomeipSdServerServiceInstanceConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 513)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdServerServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdServerServiceInstanceConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_offer_behavior: Optional[InitialSdDelayConfig]
    offer_cyclic_delay: Optional[TimeValue]
    priority: Optional[PositiveInteger]
    request: Optional[RequestResponseDelay]
    service_offer: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SomeipSdServerServiceInstanceConfig."""
        super().__init__()
        self.initial_offer_behavior: Optional[InitialSdDelayConfig] = None
        self.offer_cyclic_delay: Optional[TimeValue] = None
        self.priority: Optional[PositiveInteger] = None
        self.request: Optional[RequestResponseDelay] = None
        self.service_offer: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdServerServiceInstanceConfig":
        """Deserialize XML element to SomeipSdServerServiceInstanceConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdServerServiceInstanceConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdServerServiceInstanceConfig, cls).deserialize(element)

        # Parse initial_offer_behavior
        child = ARObject._find_child_element(element, "INITIAL-OFFER-BEHAVIOR")
        if child is not None:
            initial_offer_behavior_value = ARObject._deserialize_by_tag(child, "InitialSdDelayConfig")
            obj.initial_offer_behavior = initial_offer_behavior_value

        # Parse offer_cyclic_delay
        child = ARObject._find_child_element(element, "OFFER-CYCLIC-DELAY")
        if child is not None:
            offer_cyclic_delay_value = child.text
            obj.offer_cyclic_delay = offer_cyclic_delay_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse request
        child = ARObject._find_child_element(element, "REQUEST")
        if child is not None:
            request_value = ARObject._deserialize_by_tag(child, "RequestResponseDelay")
            obj.request = request_value

        # Parse service_offer
        child = ARObject._find_child_element(element, "SERVICE-OFFER")
        if child is not None:
            service_offer_value = child.text
            obj.service_offer = service_offer_value

        return obj



class SomeipSdServerServiceInstanceConfigBuilder:
    """Builder for SomeipSdServerServiceInstanceConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdServerServiceInstanceConfig = SomeipSdServerServiceInstanceConfig()

    def build(self) -> SomeipSdServerServiceInstanceConfig:
        """Build and return SomeipSdServerServiceInstanceConfig object.

        Returns:
            SomeipSdServerServiceInstanceConfig instance
        """
        # TODO: Add validation
        return self._obj
