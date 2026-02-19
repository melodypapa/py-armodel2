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

    controller: Optional[Any]
    nm_coord_cluster: Optional[PositiveInteger]
    nm_coordinator_role: Optional[NmCoordinatorRoleEnum]
    nm_if_ecu: Optional[NmEcu]
    nm_node_id: Optional[Integer]
    nm_passive: Optional[Boolean]
    rx_nm_pdus: list[NmPdu]
    tx_nm_pdus: list[NmPdu]
    def __init__(self) -> None:
        """Initialize NmNode."""
        super().__init__()
        self.controller: Optional[Any] = None
        self.nm_coord_cluster: Optional[PositiveInteger] = None
        self.nm_coordinator_role: Optional[NmCoordinatorRoleEnum] = None
        self.nm_if_ecu: Optional[NmEcu] = None
        self.nm_node_id: Optional[Integer] = None
        self.nm_passive: Optional[Boolean] = None
        self.rx_nm_pdus: list[NmPdu] = []
        self.tx_nm_pdus: list[NmPdu] = []
    def serialize(self) -> ET.Element:
        """Serialize NmNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize controller
        if self.controller is not None:
            serialized = ARObject._serialize_item(self.controller, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTROLLER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_coord_cluster
        if self.nm_coord_cluster is not None:
            serialized = ARObject._serialize_item(self.nm_coord_cluster, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.nm_coordinator_role, "NmCoordinatorRoleEnum")
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

        # Serialize nm_if_ecu
        if self.nm_if_ecu is not None:
            serialized = ARObject._serialize_item(self.nm_if_ecu, "NmEcu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-IF-ECU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_node_id
        if self.nm_node_id is not None:
            serialized = ARObject._serialize_item(self.nm_node_id, "Integer")
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
            serialized = ARObject._serialize_item(self.nm_passive, "Boolean")
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

        # Serialize rx_nm_pdus (list to container "RX-NM-PDUS")
        if self.rx_nm_pdus:
            wrapper = ET.Element("RX-NM-PDUS")
            for item in self.rx_nm_pdus:
                serialized = ARObject._serialize_item(item, "NmPdu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tx_nm_pdus (list to container "TX-NM-PDUS")
        if self.tx_nm_pdus:
            wrapper = ET.Element("TX-NM-PDUS")
            for item in self.tx_nm_pdus:
                serialized = ARObject._serialize_item(item, "NmPdu")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Parse controller
        child = ARObject._find_child_element(element, "CONTROLLER")
        if child is not None:
            controller_value = child.text
            obj.controller = controller_value

        # Parse nm_coord_cluster
        child = ARObject._find_child_element(element, "NM-COORD-CLUSTER")
        if child is not None:
            nm_coord_cluster_value = child.text
            obj.nm_coord_cluster = nm_coord_cluster_value

        # Parse nm_coordinator_role
        child = ARObject._find_child_element(element, "NM-COORDINATOR-ROLE")
        if child is not None:
            nm_coordinator_role_value = NmCoordinatorRoleEnum.deserialize(child)
            obj.nm_coordinator_role = nm_coordinator_role_value

        # Parse nm_if_ecu
        child = ARObject._find_child_element(element, "NM-IF-ECU")
        if child is not None:
            nm_if_ecu_value = ARObject._deserialize_by_tag(child, "NmEcu")
            obj.nm_if_ecu = nm_if_ecu_value

        # Parse nm_node_id
        child = ARObject._find_child_element(element, "NM-NODE-ID")
        if child is not None:
            nm_node_id_value = child.text
            obj.nm_node_id = nm_node_id_value

        # Parse nm_passive
        child = ARObject._find_child_element(element, "NM-PASSIVE")
        if child is not None:
            nm_passive_value = child.text
            obj.nm_passive = nm_passive_value

        # Parse rx_nm_pdus (list from container "RX-NM-PDUS")
        obj.rx_nm_pdus = []
        container = ARObject._find_child_element(element, "RX-NM-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rx_nm_pdus.append(child_value)

        # Parse tx_nm_pdus (list from container "TX-NM-PDUS")
        obj.tx_nm_pdus = []
        container = ARObject._find_child_element(element, "TX-NM-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tx_nm_pdus.append(child_value)

        return obj



class NmNodeBuilder:
    """Builder for NmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmNode = NmNode()

    def build(self) -> NmNode:
        """Build and return NmNode object.

        Returns:
            NmNode instance
        """
        # TODO: Add validation
        return self._obj
