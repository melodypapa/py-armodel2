"""SomeipSdClientEventGroupTimingConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdClientEventGroupTimingConfig(ARElement):
    """AUTOSAR SomeipSdClientEventGroupTimingConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request", None, False, False, RequestResponseDelay),  # request
        ("subscribe", None, True, False, None),  # subscribe
        ("time_to_live", None, True, False, None),  # timeToLive
    ]

    def __init__(self) -> None:
        """Initialize SomeipSdClientEventGroupTimingConfig."""
        super().__init__()
        self.request: Optional[RequestResponseDelay] = None
        self.subscribe: Optional[PositiveInteger] = None
        self.time_to_live: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SomeipSdClientEventGroupTimingConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdClientEventGroupTimingConfig":
        """Create SomeipSdClientEventGroupTimingConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SomeipSdClientEventGroupTimingConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SomeipSdClientEventGroupTimingConfig since parent returns ARObject
        return cast("SomeipSdClientEventGroupTimingConfig", obj)


class SomeipSdClientEventGroupTimingConfigBuilder:
    """Builder for SomeipSdClientEventGroupTimingConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdClientEventGroupTimingConfig = SomeipSdClientEventGroupTimingConfig()

    def build(self) -> SomeipSdClientEventGroupTimingConfig:
        """Build and return SomeipSdClientEventGroupTimingConfig object.

        Returns:
            SomeipSdClientEventGroupTimingConfig instance
        """
        # TODO: Add validation
        return self._obj
