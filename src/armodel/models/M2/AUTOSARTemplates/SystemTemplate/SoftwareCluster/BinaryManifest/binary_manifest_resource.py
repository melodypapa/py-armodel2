"""BinaryManifestResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 915)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from abc import ABC, abstractmethod


class BinaryManifestResource(Identifiable, ABC):
    """AUTOSAR BinaryManifestResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    global_resource: Optional[PositiveInteger]
    resource: Optional[Any]
    resource_guard: Optional[String]
    def __init__(self) -> None:
        """Initialize BinaryManifestResource."""
        super().__init__()
        self.global_resource: Optional[PositiveInteger] = None
        self.resource: Optional[Any] = None
        self.resource_guard: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize global_resource
        if self.global_resource is not None:
            serialized = ARObject._serialize_item(self.global_resource, "PositiveInteger")
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

        # Serialize resource
        if self.resource is not None:
            serialized = ARObject._serialize_item(self.resource, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resource_guard
        if self.resource_guard is not None:
            serialized = ARObject._serialize_item(self.resource_guard, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE-GUARD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestResource":
        """Deserialize XML element to BinaryManifestResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestResource, cls).deserialize(element)

        # Parse global_resource
        child = ARObject._find_child_element(element, "GLOBAL-RESOURCE")
        if child is not None:
            global_resource_value = child.text
            obj.global_resource = global_resource_value

        # Parse resource
        child = ARObject._find_child_element(element, "RESOURCE")
        if child is not None:
            resource_value = child.text
            obj.resource = resource_value

        # Parse resource_guard
        child = ARObject._find_child_element(element, "RESOURCE-GUARD")
        if child is not None:
            resource_guard_value = child.text
            obj.resource_guard = resource_guard_value

        return obj



class BinaryManifestResourceBuilder:
    """Builder for BinaryManifestResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestResource = BinaryManifestResource()

    def build(self) -> BinaryManifestResource:
        """Build and return BinaryManifestResource object.

        Returns:
            BinaryManifestResource instance
        """
        # TODO: Add validation
        return self._obj
