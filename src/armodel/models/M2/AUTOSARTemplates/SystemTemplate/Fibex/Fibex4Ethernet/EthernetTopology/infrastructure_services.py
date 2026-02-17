"""InfrastructureServices AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.do_ip_entity import (
    DoIpEntity,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_synchronization import (
    TimeSynchronization,
)


class InfrastructureServices(ARObject):
    """AUTOSAR InfrastructureServices."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "do_ip_entity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DoIpEntity,
        ),  # doIpEntity
        "time": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeSynchronization,
        ),  # time
    }

    def __init__(self) -> None:
        """Initialize InfrastructureServices."""
        super().__init__()
        self.do_ip_entity: Optional[DoIpEntity] = None
        self.time: Optional[TimeSynchronization] = None


class InfrastructureServicesBuilder:
    """Builder for InfrastructureServices."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InfrastructureServices = InfrastructureServices()

    def build(self) -> InfrastructureServices:
        """Build and return InfrastructureServices object.

        Returns:
            InfrastructureServices instance
        """
        # TODO: Add validation
        return self._obj
