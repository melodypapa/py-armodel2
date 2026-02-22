"""NmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 672)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from abc import ABC, abstractmethod


class NmCluster(Identifiable, ABC):
    """AUTOSAR NmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_cluster_ref: Optional[ARRef]
    nm_channel: Optional[Boolean]
    nm_node: Optional[Boolean]
    nm_node_id_enabled: Optional[Boolean]
    nm_pnc: Optional[Boolean]
    nm_repeat_msg_ind_enabled: Optional[Boolean]
    nm: Optional[Boolean]
    pnc_cluster: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NmCluster."""
        super().__init__()
        self.communication_cluster_ref: Optional[ARRef] = None
        self.nm_channel: Optional[Boolean] = None
        self.nm_node: Optional[Boolean] = None
        self.nm_node_id_enabled: Optional[Boolean] = None
        self.nm_pnc: Optional[Boolean] = None
        self.nm_repeat_msg_ind_enabled: Optional[Boolean] = None
        self.nm: Optional[Boolean] = None
        self.pnc_cluster: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize NmCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_cluster_ref
        if self.communication_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_cluster_ref, "CommunicationCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_channel
        if self.nm_channel is not None:
            serialized = SerializationHelper.serialize_item(self.nm_channel, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_node
        if self.nm_node is not None:
            serialized = SerializationHelper.serialize_item(self.nm_node, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-NODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_node_id_enabled
        if self.nm_node_id_enabled is not None:
            serialized = SerializationHelper.serialize_item(self.nm_node_id_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-NODE-ID-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_pnc
        if self.nm_pnc is not None:
            serialized = SerializationHelper.serialize_item(self.nm_pnc, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-PNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_repeat_msg_ind_enabled
        if self.nm_repeat_msg_ind_enabled is not None:
            serialized = SerializationHelper.serialize_item(self.nm_repeat_msg_ind_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REPEAT-MSG-IND-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm
        if self.nm is not None:
            serialized = SerializationHelper.serialize_item(self.nm, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_cluster
        if self.pnc_cluster is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_cluster, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-CLUSTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmCluster":
        """Deserialize XML element to NmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmCluster, cls).deserialize(element)

        # Parse communication_cluster_ref
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CLUSTER-REF")
        if child is not None:
            communication_cluster_ref_value = ARRef.deserialize(child)
            obj.communication_cluster_ref = communication_cluster_ref_value

        # Parse nm_channel
        child = SerializationHelper.find_child_element(element, "NM-CHANNEL")
        if child is not None:
            nm_channel_value = child.text
            obj.nm_channel = nm_channel_value

        # Parse nm_node
        child = SerializationHelper.find_child_element(element, "NM-NODE")
        if child is not None:
            nm_node_value = child.text
            obj.nm_node = nm_node_value

        # Parse nm_node_id_enabled
        child = SerializationHelper.find_child_element(element, "NM-NODE-ID-ENABLED")
        if child is not None:
            nm_node_id_enabled_value = child.text
            obj.nm_node_id_enabled = nm_node_id_enabled_value

        # Parse nm_pnc
        child = SerializationHelper.find_child_element(element, "NM-PNC")
        if child is not None:
            nm_pnc_value = child.text
            obj.nm_pnc = nm_pnc_value

        # Parse nm_repeat_msg_ind_enabled
        child = SerializationHelper.find_child_element(element, "NM-REPEAT-MSG-IND-ENABLED")
        if child is not None:
            nm_repeat_msg_ind_enabled_value = child.text
            obj.nm_repeat_msg_ind_enabled = nm_repeat_msg_ind_enabled_value

        # Parse nm
        child = SerializationHelper.find_child_element(element, "NM")
        if child is not None:
            nm_value = child.text
            obj.nm = nm_value

        # Parse pnc_cluster
        child = SerializationHelper.find_child_element(element, "PNC-CLUSTER")
        if child is not None:
            pnc_cluster_value = child.text
            obj.pnc_cluster = pnc_cluster_value

        return obj



