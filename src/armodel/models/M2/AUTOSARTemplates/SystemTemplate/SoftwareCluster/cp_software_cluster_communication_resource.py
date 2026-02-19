"""CpSoftwareClusterCommunicationResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 902)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterCommunicationResource(CpSoftwareClusterResource):
    """AUTOSAR CpSoftwareClusterCommunicationResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterCommunicationResource."""
        super().__init__()
        self.communication: Optional[CpSoftwareCluster] = None
    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterCommunicationResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterCommunicationResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication
        if self.communication is not None:
            serialized = ARObject._serialize_item(self.communication, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterCommunicationResource":
        """Deserialize XML element to CpSoftwareClusterCommunicationResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterCommunicationResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterCommunicationResource, cls).deserialize(element)

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.communication = communication_value

        return obj



class CpSoftwareClusterCommunicationResourceBuilder:
    """Builder for CpSoftwareClusterCommunicationResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterCommunicationResource = CpSoftwareClusterCommunicationResource()

    def build(self) -> CpSoftwareClusterCommunicationResource:
        """Build and return CpSoftwareClusterCommunicationResource object.

        Returns:
            CpSoftwareClusterCommunicationResource instance
        """
        # TODO: Add validation
        return self._obj
