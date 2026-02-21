"""ComponentClustering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 203)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
    MappingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    MappingScopeEnum,
)


class ComponentClustering(MappingConstraint):
    """AUTOSAR ComponentClustering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clustereds: list[Any]
    mapping_scope_enum_ref: Optional[MappingScopeEnum]
    def __init__(self) -> None:
        """Initialize ComponentClustering."""
        super().__init__()
        self.clustereds: list[Any] = []
        self.mapping_scope_enum_ref: Optional[MappingScopeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ComponentClustering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ComponentClustering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize clustereds (list to container "CLUSTEREDS")
        if self.clustereds:
            wrapper = ET.Element("CLUSTEREDS")
            for item in self.clustereds:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mapping_scope_enum_ref
        if self.mapping_scope_enum_ref is not None:
            serialized = ARObject._serialize_item(self.mapping_scope_enum_ref, "MappingScopeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPING-SCOPE-ENUM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComponentClustering":
        """Deserialize XML element to ComponentClustering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComponentClustering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ComponentClustering, cls).deserialize(element)

        # Parse clustereds (list from container "CLUSTEREDS")
        obj.clustereds = []
        container = ARObject._find_child_element(element, "CLUSTEREDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.clustereds.append(child_value)

        # Parse mapping_scope_enum_ref
        child = ARObject._find_child_element(element, "MAPPING-SCOPE-ENUM-REF")
        if child is not None:
            mapping_scope_enum_ref_value = ARRef.deserialize(child)
            obj.mapping_scope_enum_ref = mapping_scope_enum_ref_value

        return obj



class ComponentClusteringBuilder:
    """Builder for ComponentClustering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentClustering = ComponentClustering()

    def build(self) -> ComponentClustering:
        """Build and return ComponentClustering object.

        Returns:
            ComponentClustering instance
        """
        # TODO: Add validation
        return self._obj
