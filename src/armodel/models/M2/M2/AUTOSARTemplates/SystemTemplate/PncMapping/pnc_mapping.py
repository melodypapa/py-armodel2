"""PncMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 264)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_PncMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_provided_service_instance_group import (
    ConsumedProvidedServiceInstanceGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu_group import (
    ISignalIPduGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdur_i_pdu_group import (
    PdurIPduGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class PncMapping(Describable):
    """AUTOSAR PncMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dynamic_pncs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ISignalIPduGroup,
        ),  # dynamicPncs
        "ident": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PncMappingIdent,
        ),  # ident
        "physical_channels": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PhysicalChannel,
        ),  # physicalChannels
        "pnc_consumeds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ConsumedProvidedServiceInstanceGroup,
        ),  # pncConsumeds
        "pnc_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ISignalIPduGroup,
        ),  # pncGroups
        "pnc_identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pncIdentifier
        "pnc_pdur_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PdurIPduGroup,
        ),  # pncPdurGroups
        "pnc_wakeup": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pncWakeup
        "relevant_fors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcuInstance,
        ),  # relevantFors
        "short_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # shortLabel
        "vfcs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortGroup,
        ),  # vfcs
        "wakeup_frames": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FrameTriggering,
        ),  # wakeupFrames
    }

    def __init__(self) -> None:
        """Initialize PncMapping."""
        super().__init__()
        self.dynamic_pncs: list[ISignalIPduGroup] = []
        self.ident: Optional[PncMappingIdent] = None
        self.physical_channels: list[PhysicalChannel] = []
        self.pnc_consumeds: list[ConsumedProvidedServiceInstanceGroup] = []
        self.pnc_groups: list[ISignalIPduGroup] = []
        self.pnc_identifier: Optional[PositiveInteger] = None
        self.pnc_pdur_groups: list[PdurIPduGroup] = []
        self.pnc_wakeup: Optional[Boolean] = None
        self.relevant_fors: list[EcuInstance] = []
        self.short_label: Optional[Identifier] = None
        self.vfcs: list[PortGroup] = []
        self.wakeup_frames: list[FrameTriggering] = []


class PncMappingBuilder:
    """Builder for PncMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PncMapping = PncMapping()

    def build(self) -> PncMapping:
        """Build and return PncMapping object.

        Returns:
            PncMapping instance
        """
        # TODO: Add validation
        return self._obj
