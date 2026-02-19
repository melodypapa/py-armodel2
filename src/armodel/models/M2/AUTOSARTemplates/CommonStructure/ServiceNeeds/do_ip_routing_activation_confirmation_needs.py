"""DoIpRoutingActivationConfirmationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 807)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class DoIpRoutingActivationConfirmationNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpRoutingActivationConfirmationNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    routing: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize DoIpRoutingActivationConfirmationNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.routing: Optional[NameToken] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpRoutingActivationConfirmationNeeds":
        """Deserialize XML element to DoIpRoutingActivationConfirmationNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpRoutingActivationConfirmationNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpRoutingActivationConfirmationNeeds, cls).deserialize(element)

        # Parse data_length
        child = ARObject._find_child_element(element, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse routing
        child = ARObject._find_child_element(element, "ROUTING")
        if child is not None:
            routing_value = child.text
            obj.routing = routing_value

        return obj



class DoIpRoutingActivationConfirmationNeedsBuilder:
    """Builder for DoIpRoutingActivationConfirmationNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpRoutingActivationConfirmationNeeds = DoIpRoutingActivationConfirmationNeeds()

    def build(self) -> DoIpRoutingActivationConfirmationNeeds:
        """Build and return DoIpRoutingActivationConfirmationNeeds object.

        Returns:
            DoIpRoutingActivationConfirmationNeeds instance
        """
        # TODO: Add validation
        return self._obj
