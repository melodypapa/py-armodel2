"""PncMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dynamic_pncs", None, False, True, ISignalIPduGroup),  # dynamicPncs
        ("ident", None, False, False, PncMappingIdent),  # ident
        ("physical_channels", None, False, True, PhysicalChannel),  # physicalChannels
        ("pnc_consumeds", None, False, True, ConsumedProvidedServiceInstanceGroup),  # pncConsumeds
        ("pnc_groups", None, False, True, ISignalIPduGroup),  # pncGroups
        ("pnc_identifier", None, True, False, None),  # pncIdentifier
        ("pnc_pdur_groups", None, False, True, PdurIPduGroup),  # pncPdurGroups
        ("pnc_wakeup", None, True, False, None),  # pncWakeup
        ("relevant_fors", None, False, True, EcuInstance),  # relevantFors
        ("short_label", None, True, False, None),  # shortLabel
        ("vfcs", None, False, True, PortGroup),  # vfcs
        ("wakeup_frames", None, False, True, FrameTriggering),  # wakeupFrames
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PncMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PncMapping":
        """Create PncMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PncMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PncMapping since parent returns ARObject
        return cast("PncMapping", obj)


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
