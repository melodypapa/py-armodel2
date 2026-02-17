"""GenericTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class GenericTp(TransportProtocolConfiguration):
    """AUTOSAR GenericTp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tp_address": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tpAddress
        "tp_technology": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tpTechnology
    }

    def __init__(self) -> None:
        """Initialize GenericTp."""
        super().__init__()
        self.tp_address: Optional[String] = None
        self.tp_technology: Optional[String] = None


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
