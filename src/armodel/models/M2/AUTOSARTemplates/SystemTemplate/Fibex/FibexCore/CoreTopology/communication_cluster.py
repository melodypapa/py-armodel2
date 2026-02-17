"""CommunicationCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 107)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class CommunicationCluster(ARObject):
    """AUTOSAR CommunicationCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "baudrate": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # baudrate
        "physical_channels": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PhysicalChannel,
        ),  # physicalChannels
        "protocol_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # protocolName
        "protocol_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # protocolVersion
    }

    def __init__(self) -> None:
        """Initialize CommunicationCluster."""
        super().__init__()
        self.baudrate: Optional[PositiveUnlimitedInteger] = None
        self.physical_channels: list[PhysicalChannel] = []
        self.protocol_name: Optional[String] = None
        self.protocol_version: Optional[String] = None


class CommunicationClusterBuilder:
    """Builder for CommunicationCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationCluster = CommunicationCluster()

    def build(self) -> CommunicationCluster:
        """Build and return CommunicationCluster object.

        Returns:
            CommunicationCluster instance
        """
        # TODO: Add validation
        return self._obj
