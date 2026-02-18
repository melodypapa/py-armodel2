"""NetworkEndpointAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 464)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class NetworkEndpointAddress(ARObject, ABC):
    """AUTOSAR NetworkEndpointAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize NetworkEndpointAddress."""
        super().__init__()


class NetworkEndpointAddressBuilder:
    """Builder for NetworkEndpointAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NetworkEndpointAddress = NetworkEndpointAddress()

    def build(self) -> NetworkEndpointAddress:
        """Build and return NetworkEndpointAddress object.

        Returns:
            NetworkEndpointAddress instance
        """
        # TODO: Add validation
        return self._obj
