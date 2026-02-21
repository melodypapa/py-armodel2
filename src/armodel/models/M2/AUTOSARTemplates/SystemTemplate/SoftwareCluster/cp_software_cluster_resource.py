"""CpSoftwareClusterResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 271)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 901)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.role_based_resource_dependency import (
    RoleBasedResourceDependency,
)
from abc import ABC, abstractmethod


class CpSoftwareClusterResource(Identifiable, ABC):
    """AUTOSAR CpSoftwareClusterResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    dependents: list[RoleBasedResourceDependency]
    global_resource: Optional[PositiveInteger]
    is_mandatory: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResource."""
        super().__init__()
        self.dependents: list[RoleBasedResourceDependency] = []
        self.global_resource: Optional[PositiveInteger] = None
        self.is_mandatory: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dependents (list to container "DEPENDENTS")
        if self.dependents:
            wrapper = ET.Element("DEPENDENTS")
            for item in self.dependents:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedResourceDependency")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize global_resource
        if self.global_resource is not None:
            serialized = SerializationHelper.serialize_item(self.global_resource, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_mandatory
        if self.is_mandatory is not None:
            serialized = SerializationHelper.serialize_item(self.is_mandatory, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-MANDATORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResource":
        """Deserialize XML element to CpSoftwareClusterResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterResource, cls).deserialize(element)

        # Parse dependents (list from container "DEPENDENTS")
        obj.dependents = []
        container = SerializationHelper.find_child_element(element, "DEPENDENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dependents.append(child_value)

        # Parse global_resource
        child = SerializationHelper.find_child_element(element, "GLOBAL-RESOURCE")
        if child is not None:
            global_resource_value = child.text
            obj.global_resource = global_resource_value

        # Parse is_mandatory
        child = SerializationHelper.find_child_element(element, "IS-MANDATORY")
        if child is not None:
            is_mandatory_value = child.text
            obj.is_mandatory = is_mandatory_value

        return obj



class CpSoftwareClusterResourceBuilder:
    """Builder for CpSoftwareClusterResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterResource = CpSoftwareClusterResource()

    def build(self) -> CpSoftwareClusterResource:
        """Build and return CpSoftwareClusterResource object.

        Returns:
            CpSoftwareClusterResource instance
        """
        # TODO: Add validation
        return self._obj
