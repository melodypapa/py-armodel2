"""GlobalTimeDomain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 858)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 225)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_gateway import (
    GlobalTimeGateway,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.network_segment_identification import (
    NetworkSegmentIdentification,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class GlobalTimeDomain(FibexElement):
    """AUTOSAR GlobalTimeDomain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    debounce_time: Optional[TimeValue]
    domain_id: Optional[PositiveInteger]
    gateways: list[GlobalTimeGateway]
    global_time: Optional[AbstractGlobalTimeDomainProps]
    global_time_master: Optional[GlobalTimeMaster]
    global_time_sub_refs: list[ARRef]
    network: Optional[NetworkSegmentIdentification]
    offset_time_ref: Optional[ARRef]
    pdu_triggering_ref: Optional[ARRef]
    slaves: list[GlobalTimeSlave]
    sync_loss: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeDomain."""
        super().__init__()
        self.debounce_time: Optional[TimeValue] = None
        self.domain_id: Optional[PositiveInteger] = None
        self.gateways: list[GlobalTimeGateway] = []
        self.global_time: Optional[AbstractGlobalTimeDomainProps] = None
        self.global_time_master: Optional[GlobalTimeMaster] = None
        self.global_time_sub_refs: list[ARRef] = []
        self.network: Optional[NetworkSegmentIdentification] = None
        self.offset_time_ref: Optional[ARRef] = None
        self.pdu_triggering_ref: Optional[ARRef] = None
        self.slaves: list[GlobalTimeSlave] = []
        self.sync_loss: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeDomain to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeDomain, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize debounce_time
        if self.debounce_time is not None:
            serialized = SerializationHelper.serialize_item(self.debounce_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEBOUNCE-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize domain_id
        if self.domain_id is not None:
            serialized = SerializationHelper.serialize_item(self.domain_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DOMAIN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize gateways (list to container "GATEWAYS")
        if self.gateways:
            wrapper = ET.Element("GATEWAYS")
            for item in self.gateways:
                serialized = SerializationHelper.serialize_item(item, "GlobalTimeGateway")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize global_time
        if self.global_time is not None:
            serialized = SerializationHelper.serialize_item(self.global_time, "AbstractGlobalTimeDomainProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_time_master
        if self.global_time_master is not None:
            serialized = SerializationHelper.serialize_item(self.global_time_master, "GlobalTimeMaster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-TIME-MASTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_time_sub_refs (list to container "GLOBAL-TIME-SUB-REFS")
        if self.global_time_sub_refs:
            wrapper = ET.Element("GLOBAL-TIME-SUB-REFS")
            for item in self.global_time_sub_refs:
                serialized = SerializationHelper.serialize_item(item, "GlobalTimeDomain")
                if serialized is not None:
                    child_elem = ET.Element("GLOBAL-TIME-SUB-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize network
        if self.network is not None:
            serialized = SerializationHelper.serialize_item(self.network, "NetworkSegmentIdentification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset_time_ref
        if self.offset_time_ref is not None:
            serialized = SerializationHelper.serialize_item(self.offset_time_ref, "GlobalTimeDomain")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET-TIME-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_triggering_ref
        if self.pdu_triggering_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_triggering_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-TRIGGERING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slaves (list to container "SLAVES")
        if self.slaves:
            wrapper = ET.Element("SLAVES")
            for item in self.slaves:
                serialized = SerializationHelper.serialize_item(item, "GlobalTimeSlave")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sync_loss
        if self.sync_loss is not None:
            serialized = SerializationHelper.serialize_item(self.sync_loss, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-LOSS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeDomain":
        """Deserialize XML element to GlobalTimeDomain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeDomain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeDomain, cls).deserialize(element)

        # Parse debounce_time
        child = SerializationHelper.find_child_element(element, "DEBOUNCE-TIME")
        if child is not None:
            debounce_time_value = child.text
            obj.debounce_time = debounce_time_value

        # Parse domain_id
        child = SerializationHelper.find_child_element(element, "DOMAIN-ID")
        if child is not None:
            domain_id_value = child.text
            obj.domain_id = domain_id_value

        # Parse gateways (list from container "GATEWAYS")
        obj.gateways = []
        container = SerializationHelper.find_child_element(element, "GATEWAYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.gateways.append(child_value)

        # Parse global_time
        child = SerializationHelper.find_child_element(element, "GLOBAL-TIME")
        if child is not None:
            global_time_value = SerializationHelper.deserialize_by_tag(child, "AbstractGlobalTimeDomainProps")
            obj.global_time = global_time_value

        # Parse global_time_master
        child = SerializationHelper.find_child_element(element, "GLOBAL-TIME-MASTER")
        if child is not None:
            global_time_master_value = SerializationHelper.deserialize_by_tag(child, "GlobalTimeMaster")
            obj.global_time_master = global_time_master_value

        # Parse global_time_sub_refs (list from container "GLOBAL-TIME-SUB-REFS")
        obj.global_time_sub_refs = []
        container = SerializationHelper.find_child_element(element, "GLOBAL-TIME-SUB-REFS")
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
                    obj.global_time_sub_refs.append(child_value)

        # Parse network
        child = SerializationHelper.find_child_element(element, "NETWORK")
        if child is not None:
            network_value = SerializationHelper.deserialize_by_tag(child, "NetworkSegmentIdentification")
            obj.network = network_value

        # Parse offset_time_ref
        child = SerializationHelper.find_child_element(element, "OFFSET-TIME-REF")
        if child is not None:
            offset_time_ref_value = ARRef.deserialize(child)
            obj.offset_time_ref = offset_time_ref_value

        # Parse pdu_triggering_ref
        child = SerializationHelper.find_child_element(element, "PDU-TRIGGERING-REF")
        if child is not None:
            pdu_triggering_ref_value = ARRef.deserialize(child)
            obj.pdu_triggering_ref = pdu_triggering_ref_value

        # Parse slaves (list from container "SLAVES")
        obj.slaves = []
        container = SerializationHelper.find_child_element(element, "SLAVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.slaves.append(child_value)

        # Parse sync_loss
        child = SerializationHelper.find_child_element(element, "SYNC-LOSS")
        if child is not None:
            sync_loss_value = child.text
            obj.sync_loss = sync_loss_value

        return obj



class GlobalTimeDomainBuilder:
    """Builder for GlobalTimeDomain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeDomain = GlobalTimeDomain()

    def build(self) -> GlobalTimeDomain:
        """Build and return GlobalTimeDomain object.

        Returns:
            GlobalTimeDomain instance
        """
        # TODO: Add validation
        return self._obj
