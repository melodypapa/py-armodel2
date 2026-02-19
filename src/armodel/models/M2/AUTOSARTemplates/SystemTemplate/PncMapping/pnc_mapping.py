"""PncMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 264)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_PncMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_pnc_refs: list[ARRef]
    ident_ref: Optional[ARRef]
    physical_channels: list[PhysicalChannel]
    pnc_consumeds: list[ConsumedProvidedServiceInstanceGroup]
    pnc_group_refs: list[ARRef]
    pnc_identifier: Optional[PositiveInteger]
    pnc_pdur_group_refs: list[ARRef]
    pnc_wakeup: Optional[Boolean]
    relevant_fors: list[EcuInstance]
    short_label: Optional[Identifier]
    vfc_refs: list[ARRef]
    wakeup_frame_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PncMapping."""
        super().__init__()
        self.dynamic_pnc_refs: list[ARRef] = []
        self.ident_ref: Optional[ARRef] = None
        self.physical_channels: list[PhysicalChannel] = []
        self.pnc_consumeds: list[ConsumedProvidedServiceInstanceGroup] = []
        self.pnc_group_refs: list[ARRef] = []
        self.pnc_identifier: Optional[PositiveInteger] = None
        self.pnc_pdur_group_refs: list[ARRef] = []
        self.pnc_wakeup: Optional[Boolean] = None
        self.relevant_fors: list[EcuInstance] = []
        self.short_label: Optional[Identifier] = None
        self.vfc_refs: list[ARRef] = []
        self.wakeup_frame_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PncMapping":
        """Deserialize XML element to PncMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PncMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dynamic_pnc_refs (list)
        obj.dynamic_pnc_refs = []
        for child in ARObject._find_all_child_elements(element, "DYNAMIC-PNCS"):
            dynamic_pnc_refs_value = ARObject._deserialize_by_tag(child, "ISignalIPduGroup")
            obj.dynamic_pnc_refs.append(dynamic_pnc_refs_value)

        # Parse ident_ref
        child = ARObject._find_child_element(element, "IDENT")
        if child is not None:
            ident_ref_value = ARObject._deserialize_by_tag(child, "PncMappingIdent")
            obj.ident_ref = ident_ref_value

        # Parse physical_channels (list)
        obj.physical_channels = []
        for child in ARObject._find_all_child_elements(element, "PHYSICAL-CHANNELS"):
            physical_channels_value = ARObject._deserialize_by_tag(child, "PhysicalChannel")
            obj.physical_channels.append(physical_channels_value)

        # Parse pnc_consumeds (list)
        obj.pnc_consumeds = []
        for child in ARObject._find_all_child_elements(element, "PNC-CONSUMEDS"):
            pnc_consumeds_value = ARObject._deserialize_by_tag(child, "ConsumedProvidedServiceInstanceGroup")
            obj.pnc_consumeds.append(pnc_consumeds_value)

        # Parse pnc_group_refs (list)
        obj.pnc_group_refs = []
        for child in ARObject._find_all_child_elements(element, "PNC-GROUPS"):
            pnc_group_refs_value = ARObject._deserialize_by_tag(child, "ISignalIPduGroup")
            obj.pnc_group_refs.append(pnc_group_refs_value)

        # Parse pnc_identifier
        child = ARObject._find_child_element(element, "PNC-IDENTIFIER")
        if child is not None:
            pnc_identifier_value = child.text
            obj.pnc_identifier = pnc_identifier_value

        # Parse pnc_pdur_group_refs (list)
        obj.pnc_pdur_group_refs = []
        for child in ARObject._find_all_child_elements(element, "PNC-PDUR-GROUPS"):
            pnc_pdur_group_refs_value = ARObject._deserialize_by_tag(child, "PdurIPduGroup")
            obj.pnc_pdur_group_refs.append(pnc_pdur_group_refs_value)

        # Parse pnc_wakeup
        child = ARObject._find_child_element(element, "PNC-WAKEUP")
        if child is not None:
            pnc_wakeup_value = child.text
            obj.pnc_wakeup = pnc_wakeup_value

        # Parse relevant_fors (list)
        obj.relevant_fors = []
        for child in ARObject._find_all_child_elements(element, "RELEVANT-FORS"):
            relevant_fors_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.relevant_fors.append(relevant_fors_value)

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        # Parse vfc_refs (list)
        obj.vfc_refs = []
        for child in ARObject._find_all_child_elements(element, "VFCS"):
            vfc_refs_value = ARObject._deserialize_by_tag(child, "PortGroup")
            obj.vfc_refs.append(vfc_refs_value)

        # Parse wakeup_frame_refs (list)
        obj.wakeup_frame_refs = []
        for child in ARObject._find_all_child_elements(element, "WAKEUP-FRAMES"):
            wakeup_frame_refs_value = ARObject._deserialize_by_tag(child, "FrameTriggering")
            obj.wakeup_frame_refs.append(wakeup_frame_refs_value)

        return obj



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
