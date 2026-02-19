"""DdsCpConsumedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 474)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyVersionString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)


class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpConsumedServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consumed_ddses: list[DdsCpServiceInstance]
    local_unicast: Optional[ApplicationEndpoint]
    minor_version: Optional[AnyVersionString]
    static_remote: Optional[ApplicationEndpoint]
    def __init__(self) -> None:
        """Initialize DdsCpConsumedServiceInstance."""
        super().__init__()
        self.consumed_ddses: list[DdsCpServiceInstance] = []
        self.local_unicast: Optional[ApplicationEndpoint] = None
        self.minor_version: Optional[AnyVersionString] = None
        self.static_remote: Optional[ApplicationEndpoint] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpConsumedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpConsumedServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consumed_ddses (list to container "CONSUMED-DDSES")
        if self.consumed_ddses:
            wrapper = ET.Element("CONSUMED-DDSES")
            for item in self.consumed_ddses:
                serialized = ARObject._serialize_item(item, "DdsCpServiceInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
            serialized = ARObject._serialize_item(self.minor_version, "AnyVersionString")
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

        # Serialize static_remote
        if self.static_remote is not None:
            serialized = ARObject._serialize_item(self.static_remote, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATIC-REMOTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpConsumedServiceInstance":
        """Deserialize XML element to DdsCpConsumedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpConsumedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpConsumedServiceInstance, cls).deserialize(element)

        # Parse consumed_ddses (list from container "CONSUMED-DDSES")
        obj.consumed_ddses = []
        container = ARObject._find_child_element(element, "CONSUMED-DDSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.consumed_ddses.append(child_value)

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

        # Parse static_remote
        child = ARObject._find_child_element(element, "STATIC-REMOTE")
        if child is not None:
            static_remote_value = ARObject._deserialize_by_tag(child, "ApplicationEndpoint")
            obj.static_remote = static_remote_value

        return obj



class DdsCpConsumedServiceInstanceBuilder:
    """Builder for DdsCpConsumedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpConsumedServiceInstance = DdsCpConsumedServiceInstance()

    def build(self) -> DdsCpConsumedServiceInstance:
        """Build and return DdsCpConsumedServiceInstance object.

        Returns:
            DdsCpConsumedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
