"""TransportProtocolConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class TransportProtocolConfiguration(ARObject, ABC):
    """AUTOSAR TransportProtocolConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize TransportProtocolConfiguration."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize TransportProtocolConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransportProtocolConfiguration":
        """Deserialize XML element to TransportProtocolConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransportProtocolConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class TransportProtocolConfigurationBuilder:
    """Builder for TransportProtocolConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransportProtocolConfiguration = TransportProtocolConfiguration()

    def build(self) -> TransportProtocolConfiguration:
        """Build and return TransportProtocolConfiguration object.

        Returns:
            TransportProtocolConfiguration instance
        """
        # TODO: Add validation
        return self._obj
