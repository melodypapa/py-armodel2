"""CpSoftwareClusterToResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 907)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterToResourceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provider: Optional[CpSoftwareCluster]
    requesters: list[CpSoftwareCluster]
    service: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToResourceMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requesters: list[CpSoftwareCluster] = []
        self.service: Optional[CpSoftwareCluster] = None
    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterToResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterToResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider
        if self.provider is not None:
            serialized = ARObject._serialize_item(self.provider, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requesters (list to container "REQUESTERS")
        if self.requesters:
            wrapper = ET.Element("REQUESTERS")
            for item in self.requesters:
                serialized = ARObject._serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service
        if self.service is not None:
            serialized = ARObject._serialize_item(self.service, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToResourceMapping":
        """Deserialize XML element to CpSoftwareClusterToResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterToResourceMapping, cls).deserialize(element)

        # Parse provider
        child = ARObject._find_child_element(element, "PROVIDER")
        if child is not None:
            provider_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.provider = provider_value

        # Parse requesters (list from container "REQUESTERS")
        obj.requesters = []
        container = ARObject._find_child_element(element, "REQUESTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.requesters.append(child_value)

        # Parse service
        child = ARObject._find_child_element(element, "SERVICE")
        if child is not None:
            service_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.service = service_value

        return obj



class CpSoftwareClusterToResourceMappingBuilder:
    """Builder for CpSoftwareClusterToResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToResourceMapping = CpSoftwareClusterToResourceMapping()

    def build(self) -> CpSoftwareClusterToResourceMapping:
        """Build and return CpSoftwareClusterToResourceMapping object.

        Returns:
            CpSoftwareClusterToResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
