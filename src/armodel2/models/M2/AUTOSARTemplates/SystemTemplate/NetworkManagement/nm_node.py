"""NmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    NmCoordinatorRoleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
        NmEcu,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "CONTROLLER-REF": lambda obj, elem: setattr(obj, "controller_ref", ARRef.deserialize(elem)),
        "NM-COORD-CLUSTER": lambda obj, elem: setattr(obj, "nm_coord_cluster", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "NM-COORDINATOR-ROLE": lambda obj, elem: setattr(obj, "nm_coordinator_role", NmCoordinatorRoleEnum.deserialize(elem)),
        "NM-IF-ECU-REF": lambda obj, elem: setattr(obj, "nm_if_ecu_ref", ARRef.deserialize(elem)),
        "NM-NODE-ID": lambda obj, elem: setattr(obj, "nm_node_id", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NM-PASSIVE": lambda obj, elem: setattr(obj, "nm_passive", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RX-NM-PDU-REFS": lambda obj, elem: [obj.rx_nm_pdu_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "TX-NM-PDU-REFS": lambda obj, elem: [obj.tx_nm_pdu_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTROLLER-REF":
                setattr(obj, "controller_ref", ARRef.deserialize(child))
            elif tag == "NM-COORD-CLUSTER":
                setattr(obj, "nm_coord_cluster", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "NM-COORDINATOR-ROLE":
                setattr(obj, "nm_coordinator_role", NmCoordinatorRoleEnum.deserialize(child))
            elif tag == "NM-IF-ECU-REF":
                setattr(obj, "nm_if_ecu_ref", ARRef.deserialize(child))
            elif tag == "NM-NODE-ID":
                setattr(obj, "nm_node_id", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "NM-PASSIVE":
                setattr(obj, "nm_passive", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RX-NM-PDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rx_nm_pdu_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TX-NM-PDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tx_nm_pdu_refs.append(ARRef.deserialize(item_elem))

        return obj



class NmNodeBuilder(IdentifiableBuilder):
    """Builder for NmNode with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NmNode = NmNode()


    def with_controller(self, value: Optional[Any]) -> "NmNodeBuilder":
        """Set controller attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'controller' is required and cannot be None")
        self._obj.controller = value
        return self

    def with_nm_coord_cluster(self, value: Optional[PositiveInteger]) -> "NmNodeBuilder":
        """Set nm_coord_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_coord_cluster' is required and cannot be None")
        self._obj.nm_coord_cluster = value
        return self

    def with_nm_coordinator_role(self, value: Optional[NmCoordinatorRoleEnum]) -> "NmNodeBuilder":
        """Set nm_coordinator_role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_coordinator_role' is required and cannot be None")
        self._obj.nm_coordinator_role = value
        return self

    def with_nm_if_ecu(self, value: Optional[NmEcu]) -> "NmNodeBuilder":
        """Set nm_if_ecu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_if_ecu' is required and cannot be None")
        self._obj.nm_if_ecu = value
        return self

    def with_nm_node_id(self, value: Optional[Integer]) -> "NmNodeBuilder":
        """Set nm_node_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_node_id' is required and cannot be None")
        self._obj.nm_node_id = value
        return self

    def with_nm_passive(self, value: Optional[Boolean]) -> "NmNodeBuilder":
        """Set nm_passive attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_passive' is required and cannot be None")
        self._obj.nm_passive = value
        return self

    def with_rx_nm_pdus(self, items: list[NmPdu]) -> "NmNodeBuilder":
        """Set rx_nm_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rx_nm_pdus = list(items) if items else []
        return self

    def with_tx_nm_pdus(self, items: list[NmPdu]) -> "NmNodeBuilder":
        """Set tx_nm_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tx_nm_pdus = list(items) if items else []
        return self


    def add_rx_nm_pdu(self, item: NmPdu) -> "NmNodeBuilder":
        """Add a single item to rx_nm_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rx_nm_pdus.append(item)
        return self

    def clear_rx_nm_pdus(self) -> "NmNodeBuilder":
        """Clear all items from rx_nm_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.rx_nm_pdus = []
        return self

    def add_tx_nm_pdu(self, item: NmPdu) -> "NmNodeBuilder":
        """Add a single item to tx_nm_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tx_nm_pdus.append(item)
        return self

    def clear_tx_nm_pdus(self) -> "NmNodeBuilder":
        """Clear all items from tx_nm_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.tx_nm_pdus = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "controller",
        "nmCoordCluster",
        "nmCoordinatorRole",
        "nmIfEcu",
        "nmNodeId",
        "nmPassive",
        "rxNmPdu",
        "txNmPdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> NmNode:
        """Build and return the NmNode instance (abstract)."""
        raise NotImplementedError