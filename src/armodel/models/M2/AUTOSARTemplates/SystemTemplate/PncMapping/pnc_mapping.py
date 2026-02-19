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

    def serialize(self) -> ET.Element:
        """Serialize PncMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PncMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_pnc_refs (list to container "DYNAMIC-PNCS")
        if self.dynamic_pnc_refs:
            wrapper = ET.Element("DYNAMIC-PNCS")
            for item in self.dynamic_pnc_refs:
                serialized = ARObject._serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ident_ref
        if self.ident_ref is not None:
            serialized = ARObject._serialize_item(self.ident_ref, "PncMappingIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_channels (list to container "PHYSICAL-CHANNELS")
        if self.physical_channels:
            wrapper = ET.Element("PHYSICAL-CHANNELS")
            for item in self.physical_channels:
                serialized = ARObject._serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_consumeds (list to container "PNC-CONSUMEDS")
        if self.pnc_consumeds:
            wrapper = ET.Element("PNC-CONSUMEDS")
            for item in self.pnc_consumeds:
                serialized = ARObject._serialize_item(item, "ConsumedProvidedServiceInstanceGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_group_refs (list to container "PNC-GROUPS")
        if self.pnc_group_refs:
            wrapper = ET.Element("PNC-GROUPS")
            for item in self.pnc_group_refs:
                serialized = ARObject._serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_identifier
        if self.pnc_identifier is not None:
            serialized = ARObject._serialize_item(self.pnc_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_pdur_group_refs (list to container "PNC-PDUR-GROUPS")
        if self.pnc_pdur_group_refs:
            wrapper = ET.Element("PNC-PDUR-GROUPS")
            for item in self.pnc_pdur_group_refs:
                serialized = ARObject._serialize_item(item, "PdurIPduGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_wakeup
        if self.pnc_wakeup is not None:
            serialized = ARObject._serialize_item(self.pnc_wakeup, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-WAKEUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize relevant_fors (list to container "RELEVANT-FORS")
        if self.relevant_fors:
            wrapper = ET.Element("RELEVANT-FORS")
            for item in self.relevant_fors:
                serialized = ARObject._serialize_item(item, "EcuInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vfc_refs (list to container "VFCS")
        if self.vfc_refs:
            wrapper = ET.Element("VFCS")
            for item in self.vfc_refs:
                serialized = ARObject._serialize_item(item, "PortGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize wakeup_frame_refs (list to container "WAKEUP-FRAMES")
        if self.wakeup_frame_refs:
            wrapper = ET.Element("WAKEUP-FRAMES")
            for item in self.wakeup_frame_refs:
                serialized = ARObject._serialize_item(item, "FrameTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PncMapping":
        """Deserialize XML element to PncMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PncMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PncMapping, cls).deserialize(element)

        # Parse dynamic_pnc_refs (list from container "DYNAMIC-PNCS")
        obj.dynamic_pnc_refs = []
        container = ARObject._find_child_element(element, "DYNAMIC-PNCS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dynamic_pnc_refs.append(child_value)

        # Parse ident_ref
        child = ARObject._find_child_element(element, "IDENT-REF")
        if child is not None:
            ident_ref_value = ARRef.deserialize(child)
            obj.ident_ref = ident_ref_value

        # Parse physical_channels (list from container "PHYSICAL-CHANNELS")
        obj.physical_channels = []
        container = ARObject._find_child_element(element, "PHYSICAL-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channels.append(child_value)

        # Parse pnc_consumeds (list from container "PNC-CONSUMEDS")
        obj.pnc_consumeds = []
        container = ARObject._find_child_element(element, "PNC-CONSUMEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_consumeds.append(child_value)

        # Parse pnc_group_refs (list from container "PNC-GROUPS")
        obj.pnc_group_refs = []
        container = ARObject._find_child_element(element, "PNC-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_group_refs.append(child_value)

        # Parse pnc_identifier
        child = ARObject._find_child_element(element, "PNC-IDENTIFIER")
        if child is not None:
            pnc_identifier_value = child.text
            obj.pnc_identifier = pnc_identifier_value

        # Parse pnc_pdur_group_refs (list from container "PNC-PDUR-GROUPS")
        obj.pnc_pdur_group_refs = []
        container = ARObject._find_child_element(element, "PNC-PDUR-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_pdur_group_refs.append(child_value)

        # Parse pnc_wakeup
        child = ARObject._find_child_element(element, "PNC-WAKEUP")
        if child is not None:
            pnc_wakeup_value = child.text
            obj.pnc_wakeup = pnc_wakeup_value

        # Parse relevant_fors (list from container "RELEVANT-FORS")
        obj.relevant_fors = []
        container = ARObject._find_child_element(element, "RELEVANT-FORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.relevant_fors.append(child_value)

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse vfc_refs (list from container "VFCS")
        obj.vfc_refs = []
        container = ARObject._find_child_element(element, "VFCS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.vfc_refs.append(child_value)

        # Parse wakeup_frame_refs (list from container "WAKEUP-FRAMES")
        obj.wakeup_frame_refs = []
        container = ARObject._find_child_element(element, "WAKEUP-FRAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.wakeup_frame_refs.append(child_value)

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
