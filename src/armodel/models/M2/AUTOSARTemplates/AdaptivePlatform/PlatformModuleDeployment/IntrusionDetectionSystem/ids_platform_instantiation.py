"""IdsPlatformInstantiation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_IntrusionDetectionSystem.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.AdaptiveModule.platform_module_ethernet_endpoint_configuration import (
    PlatformModuleEthernetEndpointConfiguration,
)
from abc import ABC, abstractmethod


class IdsPlatformInstantiation(Identifiable, ABC):
    """AUTOSAR IdsPlatformInstantiation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    network_refs: list[ARRef]
    time_base_resource_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize IdsPlatformInstantiation."""
        super().__init__()
        self.network_refs: list[ARRef] = []
        self.time_base_resource_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize IdsPlatformInstantiation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsPlatformInstantiation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize network_refs (list to container "NETWORK-REFS")
        if self.network_refs:
            wrapper = ET.Element("NETWORK-REFS")
            for item in self.network_refs:
                serialized = ARObject._serialize_item(item, "PlatformModuleEthernetEndpointConfiguration")
                if serialized is not None:
                    child_elem = ET.Element("NETWORK-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize time_base_resource_ref
        if self.time_base_resource_ref is not None:
            serialized = ARObject._serialize_item(self.time_base_resource_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BASE-RESOURCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsPlatformInstantiation":
        """Deserialize XML element to IdsPlatformInstantiation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsPlatformInstantiation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsPlatformInstantiation, cls).deserialize(element)

        # Parse network_refs (list from container "NETWORK-REFS")
        obj.network_refs = []
        container = ARObject._find_child_element(element, "NETWORK-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.network_refs.append(child_value)

        # Parse time_base_resource_ref
        child = ARObject._find_child_element(element, "TIME-BASE-RESOURCE-REF")
        if child is not None:
            time_base_resource_ref_value = ARRef.deserialize(child)
            obj.time_base_resource_ref = time_base_resource_ref_value

        return obj



class IdsPlatformInstantiationBuilder:
    """Builder for IdsPlatformInstantiation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsPlatformInstantiation = IdsPlatformInstantiation()

    def build(self) -> IdsPlatformInstantiation:
        """Build and return IdsPlatformInstantiation object.

        Returns:
            IdsPlatformInstantiation instance
        """
        # TODO: Add validation
        return self._obj
