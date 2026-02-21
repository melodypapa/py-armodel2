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
from armodel.serialization import SerializationHelper
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
    physical_channel_refs: list[ARRef]
    pnc_consumed_refs: list[ARRef]
    pnc_group_refs: list[ARRef]
    pnc_identifier: Optional[PositiveInteger]
    pnc_pdur_group_refs: list[ARRef]
    pnc_wakeup: Optional[Boolean]
    relevant_for_refs: list[ARRef]
    short_label: Optional[Identifier]
    vfc_refs: list[ARRef]
    wakeup_frame_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PncMapping."""
        super().__init__()
        self.dynamic_pnc_refs: list[ARRef] = []
        self.ident_ref: Optional[ARRef] = None
        self.physical_channel_refs: list[ARRef] = []
        self.pnc_consumed_refs: list[ARRef] = []
        self.pnc_group_refs: list[ARRef] = []
        self.pnc_identifier: Optional[PositiveInteger] = None
        self.pnc_pdur_group_refs: list[ARRef] = []
        self.pnc_wakeup: Optional[Boolean] = None
        self.relevant_for_refs: list[ARRef] = []
        self.short_label: Optional[Identifier] = None
        self.vfc_refs: list[ARRef] = []
        self.wakeup_frame_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PncMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PncMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_pnc_refs (list to container "DYNAMIC-PNC-REFS")
        if self.dynamic_pnc_refs:
            wrapper = ET.Element("DYNAMIC-PNC-REFS")
            for item in self.dynamic_pnc_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("DYNAMIC-PNC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ident_ref
        if self.ident_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ident_ref, "PncMappingIdent")
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

        # Serialize physical_channel_refs (list to container "PHYSICAL-CHANNEL-REFS")
        if self.physical_channel_refs:
            wrapper = ET.Element("PHYSICAL-CHANNEL-REFS")
            for item in self.physical_channel_refs:
                serialized = SerializationHelper.serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    child_elem = ET.Element("PHYSICAL-CHANNEL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_consumed_refs (list to container "PNC-CONSUMED-REFS")
        if self.pnc_consumed_refs:
            wrapper = ET.Element("PNC-CONSUMED-REFS")
            for item in self.pnc_consumed_refs:
                serialized = SerializationHelper.serialize_item(item, "ConsumedProvidedServiceInstanceGroup")
                if serialized is not None:
                    child_elem = ET.Element("PNC-CONSUMED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_group_refs (list to container "PNC-GROUP-REFS")
        if self.pnc_group_refs:
            wrapper = ET.Element("PNC-GROUP-REFS")
            for item in self.pnc_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("PNC-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_identifier
        if self.pnc_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_identifier, "PositiveInteger")
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

        # Serialize pnc_pdur_group_refs (list to container "PNC-PDUR-GROUP-REFS")
        if self.pnc_pdur_group_refs:
            wrapper = ET.Element("PNC-PDUR-GROUP-REFS")
            for item in self.pnc_pdur_group_refs:
                serialized = SerializationHelper.serialize_item(item, "PdurIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("PNC-PDUR-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_wakeup
        if self.pnc_wakeup is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_wakeup, "Boolean")
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

        # Serialize relevant_for_refs (list to container "RELEVANT-FOR-REFS")
        if self.relevant_for_refs:
            wrapper = ET.Element("RELEVANT-FOR-REFS")
            for item in self.relevant_for_refs:
                serialized = SerializationHelper.serialize_item(item, "EcuInstance")
                if serialized is not None:
                    child_elem = ET.Element("RELEVANT-FOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
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

        # Serialize vfc_refs (list to container "VFC-REFS")
        if self.vfc_refs:
            wrapper = ET.Element("VFC-REFS")
            for item in self.vfc_refs:
                serialized = SerializationHelper.serialize_item(item, "PortGroup")
                if serialized is not None:
                    child_elem = ET.Element("VFC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize wakeup_frame_refs (list to container "WAKEUP-FRAME-REFS")
        if self.wakeup_frame_refs:
            wrapper = ET.Element("WAKEUP-FRAME-REFS")
            for item in self.wakeup_frame_refs:
                serialized = SerializationHelper.serialize_item(item, "FrameTriggering")
                if serialized is not None:
                    child_elem = ET.Element("WAKEUP-FRAME-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Parse dynamic_pnc_refs (list from container "DYNAMIC-PNC-REFS")
        obj.dynamic_pnc_refs = []
        container = SerializationHelper.find_child_element(element, "DYNAMIC-PNC-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dynamic_pnc_refs.append(child_value)

        # Parse ident_ref
        child = SerializationHelper.find_child_element(element, "IDENT-REF")
        if child is not None:
            ident_ref_value = ARRef.deserialize(child)
            obj.ident_ref = ident_ref_value

        # Parse physical_channel_refs (list from container "PHYSICAL-CHANNEL-REFS")
        obj.physical_channel_refs = []
        container = SerializationHelper.find_child_element(element, "PHYSICAL-CHANNEL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channel_refs.append(child_value)

        # Parse pnc_consumed_refs (list from container "PNC-CONSUMED-REFS")
        obj.pnc_consumed_refs = []
        container = SerializationHelper.find_child_element(element, "PNC-CONSUMED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_consumed_refs.append(child_value)

        # Parse pnc_group_refs (list from container "PNC-GROUP-REFS")
        obj.pnc_group_refs = []
        container = SerializationHelper.find_child_element(element, "PNC-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_group_refs.append(child_value)

        # Parse pnc_identifier
        child = SerializationHelper.find_child_element(element, "PNC-IDENTIFIER")
        if child is not None:
            pnc_identifier_value = child.text
            obj.pnc_identifier = pnc_identifier_value

        # Parse pnc_pdur_group_refs (list from container "PNC-PDUR-GROUP-REFS")
        obj.pnc_pdur_group_refs = []
        container = SerializationHelper.find_child_element(element, "PNC-PDUR-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_pdur_group_refs.append(child_value)

        # Parse pnc_wakeup
        child = SerializationHelper.find_child_element(element, "PNC-WAKEUP")
        if child is not None:
            pnc_wakeup_value = child.text
            obj.pnc_wakeup = pnc_wakeup_value

        # Parse relevant_for_refs (list from container "RELEVANT-FOR-REFS")
        obj.relevant_for_refs = []
        container = SerializationHelper.find_child_element(element, "RELEVANT-FOR-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.relevant_for_refs.append(child_value)

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse vfc_refs (list from container "VFC-REFS")
        obj.vfc_refs = []
        container = SerializationHelper.find_child_element(element, "VFC-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.vfc_refs.append(child_value)

        # Parse wakeup_frame_refs (list from container "WAKEUP-FRAME-REFS")
        obj.wakeup_frame_refs = []
        container = SerializationHelper.find_child_element(element, "WAKEUP-FRAME-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
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
