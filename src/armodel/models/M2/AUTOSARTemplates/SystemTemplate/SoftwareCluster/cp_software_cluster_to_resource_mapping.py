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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    provider_ref: Optional[ARRef]
    requester_refs: list[ARRef]
    service_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToResourceMapping."""
        super().__init__()
        self.provider_ref: Optional[ARRef] = None
        self.requester_refs: list[ARRef] = []
        self.service_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterToResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterToResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider_ref
        if self.provider_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provider_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requester_refs (list to container "REQUESTER-REFS")
        if self.requester_refs:
            wrapper = ET.Element("REQUESTER-REFS")
            for item in self.requester_refs:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    child_elem = ET.Element("REQUESTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_ref
        if self.service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.service_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-REF")
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

        # Parse provider_ref
        child = SerializationHelper.find_child_element(element, "PROVIDER-REF")
        if child is not None:
            provider_ref_value = ARRef.deserialize(child)
            obj.provider_ref = provider_ref_value

        # Parse requester_refs (list from container "REQUESTER-REFS")
        obj.requester_refs = []
        container = SerializationHelper.find_child_element(element, "REQUESTER-REFS")
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
                    obj.requester_refs.append(child_value)

        # Parse service_ref
        child = SerializationHelper.find_child_element(element, "SERVICE-REF")
        if child is not None:
            service_ref_value = ARRef.deserialize(child)
            obj.service_ref = service_ref_value

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
