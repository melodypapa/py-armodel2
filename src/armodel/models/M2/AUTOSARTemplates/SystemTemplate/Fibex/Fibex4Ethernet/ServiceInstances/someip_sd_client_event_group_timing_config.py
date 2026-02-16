"""SomeipSdClientEventGroupTimingConfig AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "request": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RequestResponseDelay,
        ),  # request
        "subscribe": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # subscribe
        "time_to_live": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeToLive
    }

    def __init__(self) -> None:
        """Initialize SomeipSdClientEventGroupTimingConfig."""
        super().__init__()
        self.request: Optional[RequestResponseDelay] = None
        self.subscribe: Optional[PositiveInteger] = None
        self.time_to_live: Optional[PositiveInteger] = None


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
