"""TpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 587)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from abc import ABC, abstractmethod


class TpConfig(FibexElement, ABC):
    """AUTOSAR TpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_cluster: Optional[CommunicationCluster]
    def __init__(self) -> None:
        """Initialize TpConfig."""
        super().__init__()
        self.communication_cluster: Optional[CommunicationCluster] = None

    def serialize(self) -> ET.Element:
        """Serialize TpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_cluster
        if self.communication_cluster is not None:
            serialized = ARObject._serialize_item(self.communication_cluster, "CommunicationCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CLUSTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpConfig":
        """Deserialize XML element to TpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TpConfig, cls).deserialize(element)

        # Parse communication_cluster
        child = ARObject._find_child_element(element, "COMMUNICATION-CLUSTER")
        if child is not None:
            communication_cluster_value = ARObject._deserialize_by_tag(child, "CommunicationCluster")
            obj.communication_cluster = communication_cluster_value

        return obj



class TpConfigBuilder:
    """Builder for TpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConfig = TpConfig()

    def build(self) -> TpConfig:
        """Build and return TpConfig object.

        Returns:
            TpConfig instance
        """
        # TODO: Add validation
        return self._obj
