"""DdsCpProvidedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 472)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)


class DdsCpProvidedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpProvidedServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    local_unicast: Optional[ApplicationEndpoint]
    minor_version: Optional[PositiveInteger]
    provided_ddses: list[DdsCpServiceInstance]
    static_remotes: list[ApplicationEndpoint]
    def __init__(self) -> None:
        """Initialize DdsCpProvidedServiceInstance."""
        super().__init__()
        self.local_unicast: Optional[ApplicationEndpoint] = None
        self.minor_version: Optional[PositiveInteger] = None
        self.provided_ddses: list[DdsCpServiceInstance] = []
        self.static_remotes: list[ApplicationEndpoint] = []
    def serialize(self) -> ET.Element:
        """Serialize DdsCpProvidedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpProvidedServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize local_unicast
        if self.local_unicast is not None:
            serialized = ARObject._serialize_item(self.local_unicast, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-UNICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minor_version
        if self.minor_version is not None:
            serialized = ARObject._serialize_item(self.minor_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize provided_ddses (list to container "PROVIDED-DDSES")
        if self.provided_ddses:
            wrapper = ET.Element("PROVIDED-DDSES")
            for item in self.provided_ddses:
                serialized = ARObject._serialize_item(item, "DdsCpServiceInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize static_remotes (list to container "STATIC-REMOTES")
        if self.static_remotes:
            wrapper = ET.Element("STATIC-REMOTES")
            for item in self.static_remotes:
                serialized = ARObject._serialize_item(item, "ApplicationEndpoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpProvidedServiceInstance":
        """Deserialize XML element to DdsCpProvidedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpProvidedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpProvidedServiceInstance, cls).deserialize(element)

        # Parse local_unicast
        child = ARObject._find_child_element(element, "LOCAL-UNICAST")
        if child is not None:
            local_unicast_value = ARObject._deserialize_by_tag(child, "ApplicationEndpoint")
            obj.local_unicast = local_unicast_value

        # Parse minor_version
        child = ARObject._find_child_element(element, "MINOR-VERSION")
        if child is not None:
            minor_version_value = child.text
            obj.minor_version = minor_version_value

        # Parse provided_ddses (list from container "PROVIDED-DDSES")
        obj.provided_ddses = []
        container = ARObject._find_child_element(element, "PROVIDED-DDSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_ddses.append(child_value)

        # Parse static_remotes (list from container "STATIC-REMOTES")
        obj.static_remotes = []
        container = ARObject._find_child_element(element, "STATIC-REMOTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.static_remotes.append(child_value)

        return obj



class DdsCpProvidedServiceInstanceBuilder:
    """Builder for DdsCpProvidedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpProvidedServiceInstance = DdsCpProvidedServiceInstance()

    def build(self) -> DdsCpProvidedServiceInstance:
        """Build and return DdsCpProvidedServiceInstance object.

        Returns:
            DdsCpProvidedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
