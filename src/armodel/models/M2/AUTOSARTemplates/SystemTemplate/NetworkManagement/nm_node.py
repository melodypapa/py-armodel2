"""NmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    NmCoordinatorRoleEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
        NmEcu,
    )



from abc import ABC, abstractmethod


class NmNode(Identifiable, ABC):
    """AUTOSAR NmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    controller_ref: Optional[Any]
    nm_coord_cluster: Optional[PositiveInteger]
    nm_coordinator_role: Optional[NmCoordinatorRoleEnum]
    nm_if_ecu_ref: Optional[ARRef]
    nm_node_id: Optional[Integer]
    nm_passive: Optional[Boolean]
    rx_nm_pdu_refs: list[ARRef]
    tx_nm_pdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize NmNode."""
        super().__init__()
        self.controller_ref: Optional[Any] = None
        self.nm_coord_cluster: Optional[PositiveInteger] = None
        self.nm_coordinator_role: Optional[NmCoordinatorRoleEnum] = None
        self.nm_if_ecu_ref: Optional[ARRef] = None
        self.nm_node_id: Optional[Integer] = None
        self.nm_passive: Optional[Boolean] = None
        self.rx_nm_pdu_refs: list[ARRef] = []
        self.tx_nm_pdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize NmNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize controller_ref
        if self.controller_ref is not None:
            serialized = SerializationHelper.serialize_item(self.controller_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTROLLER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_coord_cluster
        if self.nm_coord_cluster is not None:
            serialized = SerializationHelper.serialize_item(self.nm_coord_cluster, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-COORD-CLUSTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_coordinator_role
        if self.nm_coordinator_role is not None:
            serialized = SerializationHelper.serialize_item(self.nm_coordinator_role, "NmCoordinatorRoleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-COORDINATOR-ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_if_ecu_ref
        if self.nm_if_ecu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.nm_if_ecu_ref, "NmEcu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-IF-ECU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_node_id
        if self.nm_node_id is not None:
            serialized = SerializationHelper.serialize_item(self.nm_node_id, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-NODE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_passive
        if self.nm_passive is not None:
            serialized = SerializationHelper.serialize_item(self.nm_passive, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-PASSIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_nm_pdu_refs (list to container "RX-NM-PDU-REFS")
        if self.rx_nm_pdu_refs:
            wrapper = ET.Element("RX-NM-PDU-REFS")
            for item in self.rx_nm_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "NmPdu")
                if serialized is not None:
                    child_elem = ET.Element("RX-NM-PDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tx_nm_pdu_refs (list to container "TX-NM-PDU-REFS")
        if self.tx_nm_pdu_refs:
            wrapper = ET.Element("TX-NM-PDU-REFS")
            for item in self.tx_nm_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "NmPdu")
                if serialized is not None:
                    child_elem = ET.Element("TX-NM-PDU-REF")
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
    def deserialize(cls, element: ET.Element) -> "NmNode":
        """Deserialize XML element to NmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmNode, cls).deserialize(element)

        # Parse controller_ref
        child = SerializationHelper.find_child_element(element, "CONTROLLER-REF")
        if child is not None:
            controller_ref_value = ARRef.deserialize(child)
            obj.controller_ref = controller_ref_value

        # Parse nm_coord_cluster
        child = SerializationHelper.find_child_element(element, "NM-COORD-CLUSTER")
        if child is not None:
            nm_coord_cluster_value = child.text
            obj.nm_coord_cluster = nm_coord_cluster_value

        # Parse nm_coordinator_role
        child = SerializationHelper.find_child_element(element, "NM-COORDINATOR-ROLE")
        if child is not None:
            nm_coordinator_role_value = NmCoordinatorRoleEnum.deserialize(child)
            obj.nm_coordinator_role = nm_coordinator_role_value

        # Parse nm_if_ecu_ref
        child = SerializationHelper.find_child_element(element, "NM-IF-ECU-REF")
        if child is not None:
            nm_if_ecu_ref_value = ARRef.deserialize(child)
            obj.nm_if_ecu_ref = nm_if_ecu_ref_value

        # Parse nm_node_id
        child = SerializationHelper.find_child_element(element, "NM-NODE-ID")
        if child is not None:
            nm_node_id_value = child.text
            obj.nm_node_id = nm_node_id_value

        # Parse nm_passive
        child = SerializationHelper.find_child_element(element, "NM-PASSIVE")
        if child is not None:
            nm_passive_value = child.text
            obj.nm_passive = nm_passive_value

        # Parse rx_nm_pdu_refs (list from container "RX-NM-PDU-REFS")
        obj.rx_nm_pdu_refs = []
        container = SerializationHelper.find_child_element(element, "RX-NM-PDU-REFS")
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
                    obj.rx_nm_pdu_refs.append(child_value)

        # Parse tx_nm_pdu_refs (list from container "TX-NM-PDU-REFS")
        obj.tx_nm_pdu_refs = []
        container = SerializationHelper.find_child_element(element, "TX-NM-PDU-REFS")
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
                    obj.tx_nm_pdu_refs.append(child_value)

        return obj



