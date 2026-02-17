"""CanControllerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_controller_attributes import (
    AbstractCanCommunicationControllerAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CanControllerConfiguration(AbstractCanCommunicationControllerAttributes):
    """AUTOSAR CanControllerConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "prop_seg": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # propSeg
        "sync_jump_width": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # syncJumpWidth
        "time_seg1": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeSeg1
        "time_seg2": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeSeg2
    }

    def __init__(self) -> None:
        """Initialize CanControllerConfiguration."""
        super().__init__()
        self.prop_seg: Optional[Integer] = None
        self.sync_jump_width: Optional[Integer] = None
        self.time_seg1: Optional[Integer] = None
        self.time_seg2: Optional[Integer] = None


class CanControllerConfigurationBuilder:
    """Builder for CanControllerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerConfiguration = CanControllerConfiguration()

    def build(self) -> CanControllerConfiguration:
        """Build and return CanControllerConfiguration object.

        Returns:
            CanControllerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
