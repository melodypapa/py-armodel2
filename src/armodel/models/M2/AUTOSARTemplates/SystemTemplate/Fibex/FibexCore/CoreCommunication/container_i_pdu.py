"""ContainerIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 353)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainerIPduHeaderTypeEnum,
    ContainerIPduTriggerEnum,
    RxAcceptContainedIPduEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class ContainerIPdu(IPdu):
    """AUTOSAR ContainerIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    contained_i_pdu_propses: list[ContainedIPduProps]
    contained_pdu_refs: list[ARRef]
    container: Optional[TimeValue]
    container_trigger_ref: Optional[ContainerIPduTriggerEnum]
    header_type: Optional[ContainerIPduHeaderTypeEnum]
    minimum_rx: Optional[PositiveInteger]
    minimum_tx: Optional[PositiveInteger]
    rx_accept: Optional[RxAcceptContainedIPduEnum]
    threshold_size: Optional[PositiveInteger]
    unused_bit: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ContainerIPdu."""
        super().__init__()
        self.contained_i_pdu_propses: list[ContainedIPduProps] = []
        self.contained_pdu_refs: list[ARRef] = []
        self.container: Optional[TimeValue] = None
        self.container_trigger_ref: Optional[ContainerIPduTriggerEnum] = None
        self.header_type: Optional[ContainerIPduHeaderTypeEnum] = None
        self.minimum_rx: Optional[PositiveInteger] = None
        self.minimum_tx: Optional[PositiveInteger] = None
        self.rx_accept: Optional[RxAcceptContainedIPduEnum] = None
        self.threshold_size: Optional[PositiveInteger] = None
        self.unused_bit: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ContainerIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ContainerIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize contained_i_pdu_propses (list to container "CONTAINED-I-PDU-PROPSES")
        if self.contained_i_pdu_propses:
            wrapper = ET.Element("CONTAINED-I-PDU-PROPSES")
            for item in self.contained_i_pdu_propses:
                serialized = ARObject._serialize_item(item, "ContainedIPduProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize contained_pdu_refs (list to container "CONTAINED-PDU-REFS")
        if self.contained_pdu_refs:
            wrapper = ET.Element("CONTAINED-PDU-REFS")
            for item in self.contained_pdu_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("CONTAINED-PDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize container
        if self.container is not None:
            serialized = ARObject._serialize_item(self.container, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize container_trigger_ref
        if self.container_trigger_ref is not None:
            serialized = ARObject._serialize_item(self.container_trigger_ref, "ContainerIPduTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINER-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize header_type
        if self.header_type is not None:
            serialized = ARObject._serialize_item(self.header_type, "ContainerIPduHeaderTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_rx
        if self.minimum_rx is not None:
            serialized = ARObject._serialize_item(self.minimum_rx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-RX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_tx
        if self.minimum_tx is not None:
            serialized = ARObject._serialize_item(self.minimum_tx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_accept
        if self.rx_accept is not None:
            serialized = ARObject._serialize_item(self.rx_accept, "RxAcceptContainedIPduEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-ACCEPT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize threshold_size
        if self.threshold_size is not None:
            serialized = ARObject._serialize_item(self.threshold_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("THRESHOLD-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unused_bit
        if self.unused_bit is not None:
            serialized = ARObject._serialize_item(self.unused_bit, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNUSED-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ContainerIPdu":
        """Deserialize XML element to ContainerIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ContainerIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ContainerIPdu, cls).deserialize(element)

        # Parse contained_i_pdu_propses (list from container "CONTAINED-I-PDU-PROPSES")
        obj.contained_i_pdu_propses = []
        container = ARObject._find_child_element(element, "CONTAINED-I-PDU-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contained_i_pdu_propses.append(child_value)

        # Parse contained_pdu_refs (list from container "CONTAINED-PDU-REFS")
        obj.contained_pdu_refs = []
        container = ARObject._find_child_element(element, "CONTAINED-PDU-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contained_pdu_refs.append(child_value)

        # Parse container
        child = ARObject._find_child_element(element, "CONTAINER")
        if child is not None:
            container_value = child.text
            obj.container = container_value

        # Parse container_trigger_ref
        child = ARObject._find_child_element(element, "CONTAINER-TRIGGER-REF")
        if child is not None:
            container_trigger_ref_value = ARRef.deserialize(child)
            obj.container_trigger_ref = container_trigger_ref_value

        # Parse header_type
        child = ARObject._find_child_element(element, "HEADER-TYPE")
        if child is not None:
            header_type_value = ContainerIPduHeaderTypeEnum.deserialize(child)
            obj.header_type = header_type_value

        # Parse minimum_rx
        child = ARObject._find_child_element(element, "MINIMUM-RX")
        if child is not None:
            minimum_rx_value = child.text
            obj.minimum_rx = minimum_rx_value

        # Parse minimum_tx
        child = ARObject._find_child_element(element, "MINIMUM-TX")
        if child is not None:
            minimum_tx_value = child.text
            obj.minimum_tx = minimum_tx_value

        # Parse rx_accept
        child = ARObject._find_child_element(element, "RX-ACCEPT")
        if child is not None:
            rx_accept_value = RxAcceptContainedIPduEnum.deserialize(child)
            obj.rx_accept = rx_accept_value

        # Parse threshold_size
        child = ARObject._find_child_element(element, "THRESHOLD-SIZE")
        if child is not None:
            threshold_size_value = child.text
            obj.threshold_size = threshold_size_value

        # Parse unused_bit
        child = ARObject._find_child_element(element, "UNUSED-BIT")
        if child is not None:
            unused_bit_value = child.text
            obj.unused_bit = unused_bit_value

        return obj



class ContainerIPduBuilder:
    """Builder for ContainerIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ContainerIPdu = ContainerIPdu()

    def build(self) -> ContainerIPdu:
        """Build and return ContainerIPdu object.

        Returns:
            ContainerIPdu instance
        """
        # TODO: Add validation
        return self._obj
