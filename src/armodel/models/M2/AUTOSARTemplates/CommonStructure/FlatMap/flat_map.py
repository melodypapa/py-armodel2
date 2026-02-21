"""FlatMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 317)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 965)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 445)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)


class FlatMap(ARElement):
    """AUTOSAR FlatMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    instances: list[FlatInstanceDescriptor]
    def __init__(self) -> None:
        """Initialize FlatMap."""
        super().__init__()
        self.instances: list[FlatInstanceDescriptor] = []

    def serialize(self) -> ET.Element:
        """Serialize FlatMap to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlatMap, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize instances (list to container "INSTANCES")
        if self.instances:
            wrapper = ET.Element("INSTANCES")
            for item in self.instances:
                serialized = ARObject._serialize_item(item, "FlatInstanceDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlatMap":
        """Deserialize XML element to FlatMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlatMap object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlatMap, cls).deserialize(element)

        # Parse instances (list from container "INSTANCES")
        obj.instances = []
        container = ARObject._find_child_element(element, "INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instances.append(child_value)

        return obj



class FlatMapBuilder:
    """Builder for FlatMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlatMap = FlatMap()

    def build(self) -> FlatMap:
        """Build and return FlatMap object.

        Returns:
            FlatMap instance
        """
        # TODO: Add validation
        return self._obj
