"""SomeipSdServerEventGroupTimingConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdServerEventGroupTimingConfig(ARElement):
    """AUTOSAR SomeipSdServerEventGroupTimingConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request", None, False, False, RequestResponseDelay),  # request
    ]

    def __init__(self) -> None:
        """Initialize SomeipSdServerEventGroupTimingConfig."""
        super().__init__()
        self.request: Optional[RequestResponseDelay] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SomeipSdServerEventGroupTimingConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdServerEventGroupTimingConfig":
        """Create SomeipSdServerEventGroupTimingConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SomeipSdServerEventGroupTimingConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SomeipSdServerEventGroupTimingConfig since parent returns ARObject
        return cast("SomeipSdServerEventGroupTimingConfig", obj)


class SomeipSdServerEventGroupTimingConfigBuilder:
    """Builder for SomeipSdServerEventGroupTimingConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdServerEventGroupTimingConfig = SomeipSdServerEventGroupTimingConfig()

    def build(self) -> SomeipSdServerEventGroupTimingConfig:
        """Build and return SomeipSdServerEventGroupTimingConfig object.

        Returns:
            SomeipSdServerEventGroupTimingConfig instance
        """
        # TODO: Add validation
        return self._obj
