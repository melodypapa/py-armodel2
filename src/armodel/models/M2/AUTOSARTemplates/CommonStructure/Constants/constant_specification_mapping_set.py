"""ConstantSpecificationMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 445)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)


class ConstantSpecificationMappingSet(ARElement):
    """AUTOSAR ConstantSpecificationMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mappings: list[ConstantSpecification]
    def __init__(self) -> None:
        """Initialize ConstantSpecificationMappingSet."""
        super().__init__()
        self.mappings: list[ConstantSpecification] = []

    def serialize(self) -> ET.Element:
        """Serialize ConstantSpecificationMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConstantSpecificationMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mappings (list to container "MAPPINGS")
        if self.mappings:
            wrapper = ET.Element("MAPPINGS")
            for item in self.mappings:
                serialized = ARObject._serialize_item(item, "ConstantSpecification")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecificationMappingSet":
        """Deserialize XML element to ConstantSpecificationMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstantSpecificationMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstantSpecificationMappingSet, cls).deserialize(element)

        # Parse mappings (list from container "MAPPINGS")
        obj.mappings = []
        container = ARObject._find_child_element(element, "MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mappings.append(child_value)

        return obj



class ConstantSpecificationMappingSetBuilder:
    """Builder for ConstantSpecificationMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantSpecificationMappingSet = ConstantSpecificationMappingSet()

    def build(self) -> ConstantSpecificationMappingSet:
        """Build and return ConstantSpecificationMappingSet object.

        Returns:
            ConstantSpecificationMappingSet instance
        """
        # TODO: Add validation
        return self._obj
