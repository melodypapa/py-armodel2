"""GenericTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class GenericTp(TransportProtocolConfiguration):
    """AUTOSAR GenericTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_address: Optional[String]
    tp_technology: Optional[String]
    def __init__(self) -> None:
        """Initialize GenericTp."""
        super().__init__()
        self.tp_address: Optional[String] = None
        self.tp_technology: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GenericTp":
        """Deserialize XML element to GenericTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GenericTp object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = child.text
            obj.tp_address = tp_address_value

        # Parse tp_technology
        child = ARObject._find_child_element(element, "TP-TECHNOLOGY")
        if child is not None:
            tp_technology_value = child.text
            obj.tp_technology = tp_technology_value

        return obj



class GenericTpBuilder:
    """Builder for GenericTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GenericTp = GenericTp()

    def build(self) -> GenericTp:
        """Build and return GenericTp object.

        Returns:
            GenericTp instance
        """
        # TODO: Add validation
        return self._obj
