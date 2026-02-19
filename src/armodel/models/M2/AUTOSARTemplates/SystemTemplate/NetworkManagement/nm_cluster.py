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

    communication_cluster: Optional[CommunicationCluster]
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
        self.communication_cluster: Optional[CommunicationCluster] = None
        self.nm_channel: Optional[Boolean] = None
        self.nm_node: Optional[Boolean] = None
        self.nm_node_id_enabled: Optional[Boolean] = None
        self.nm_pnc: Optional[Boolean] = None
        self.nm_repeat_msg_ind_enabled: Optional[Boolean] = None
        self.nm: Optional[Boolean] = None
        self.pnc_cluster: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmCluster":
        """Deserialize XML element to NmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication_cluster
        child = ARObject._find_child_element(element, "COMMUNICATION-CLUSTER")
        if child is not None:
            communication_cluster_value = ARObject._deserialize_by_tag(child, "CommunicationCluster")
            obj.communication_cluster = communication_cluster_value

        # Parse nm_channel
        child = ARObject._find_child_element(element, "NM-CHANNEL")
        if child is not None:
            nm_channel_value = child.text
            obj.nm_channel = nm_channel_value

        # Parse nm_node
        child = ARObject._find_child_element(element, "NM-NODE")
        if child is not None:
            nm_node_value = child.text
            obj.nm_node = nm_node_value

        # Parse nm_node_id_enabled
        child = ARObject._find_child_element(element, "NM-NODE-ID-ENABLED")
        if child is not None:
            nm_node_id_enabled_value = child.text
            obj.nm_node_id_enabled = nm_node_id_enabled_value

        # Parse nm_pnc
        child = ARObject._find_child_element(element, "NM-PNC")
        if child is not None:
            nm_pnc_value = child.text
            obj.nm_pnc = nm_pnc_value

        # Parse nm_repeat_msg_ind_enabled
        child = ARObject._find_child_element(element, "NM-REPEAT-MSG-IND-ENABLED")
        if child is not None:
            nm_repeat_msg_ind_enabled_value = child.text
            obj.nm_repeat_msg_ind_enabled = nm_repeat_msg_ind_enabled_value

        # Parse nm
        child = ARObject._find_child_element(element, "NM")
        if child is not None:
            nm_value = child.text
            obj.nm = nm_value

        # Parse pnc_cluster
        child = ARObject._find_child_element(element, "PNC-CLUSTER")
        if child is not None:
            pnc_cluster_value = child.text
            obj.pnc_cluster = pnc_cluster_value

        return obj



class NmClusterBuilder:
    """Builder for NmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmCluster = NmCluster()

    def build(self) -> NmCluster:
        """Build and return NmCluster object.

        Returns:
            NmCluster instance
        """
        # TODO: Add validation
        return self._obj
