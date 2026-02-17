"""HwPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 183)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPortMapping(ARObject):
    """AUTOSAR HwPortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "communication_connector": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CommunicationConnector,
        ),  # communicationConnector
        "hw_pin_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwPinGroup,
        ),  # hwPinGroup
    }

    def __init__(self) -> None:
        """Initialize HwPortMapping."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.hw_pin_group: Optional[HwPinGroup] = None


class HwPortMappingBuilder:
    """Builder for HwPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPortMapping = HwPortMapping()

    def build(self) -> HwPortMapping:
        """Build and return HwPortMapping object.

        Returns:
            HwPortMapping instance
        """
        # TODO: Add validation
        return self._obj
