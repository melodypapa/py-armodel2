"""SomeipSdServerServiceInstanceConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("initial_offer_behavior", None, False, False, InitialSdDelayConfig),  # initialOfferBehavior
        ("offer_cyclic_delay", None, True, False, None),  # offerCyclicDelay
        ("priority", None, True, False, None),  # priority
        ("request", None, False, False, RequestResponseDelay),  # request
        ("service_offer", None, True, False, None),  # serviceOffer
    ]

    def __init__(self) -> None:
        """Initialize SomeipSdServerServiceInstanceConfig."""
        super().__init__()
        self.initial_offer_behavior: Optional[InitialSdDelayConfig] = None
        self.offer_cyclic_delay: Optional[TimeValue] = None
        self.priority: Optional[PositiveInteger] = None
        self.request: Optional[RequestResponseDelay] = None
        self.service_offer: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SomeipSdServerServiceInstanceConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdServerServiceInstanceConfig":
        """Create SomeipSdServerServiceInstanceConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SomeipSdServerServiceInstanceConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SomeipSdServerServiceInstanceConfig since parent returns ARObject
        return cast("SomeipSdServerServiceInstanceConfig", obj)


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
