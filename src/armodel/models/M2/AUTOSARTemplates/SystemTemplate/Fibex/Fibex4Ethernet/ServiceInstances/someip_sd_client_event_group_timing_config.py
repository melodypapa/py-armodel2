"""SomeipSdClientEventGroupTimingConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 521)

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
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdClientEventGroupTimingConfig(ARElement):
    """AUTOSAR SomeipSdClientEventGroupTimingConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request: Optional[RequestResponseDelay]
    subscribe: Optional[PositiveInteger]
    time_to_live: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SomeipSdClientEventGroupTimingConfig."""
        super().__init__()
        self.request: Optional[RequestResponseDelay] = None
        self.subscribe: Optional[PositiveInteger] = None
        self.time_to_live: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdClientEventGroupTimingConfig":
        """Deserialize XML element to SomeipSdClientEventGroupTimingConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdClientEventGroupTimingConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdClientEventGroupTimingConfig, cls).deserialize(element)

        # Parse request
        child = ARObject._find_child_element(element, "REQUEST")
        if child is not None:
            request_value = ARObject._deserialize_by_tag(child, "RequestResponseDelay")
            obj.request = request_value

        # Parse subscribe
        child = ARObject._find_child_element(element, "SUBSCRIBE")
        if child is not None:
            subscribe_value = child.text
            obj.subscribe = subscribe_value

        # Parse time_to_live
        child = ARObject._find_child_element(element, "TIME-TO-LIVE")
        if child is not None:
            time_to_live_value = child.text
            obj.time_to_live = time_to_live_value

        return obj



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
