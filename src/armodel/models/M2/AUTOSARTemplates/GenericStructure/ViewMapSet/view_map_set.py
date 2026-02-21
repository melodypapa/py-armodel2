"""ViewMapSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2079)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 401)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ViewMapSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet.view_map import (
    ViewMap,
)


class ViewMapSet(ARElement):
    """AUTOSAR ViewMapSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    view_maps: list[ViewMap]
    def __init__(self) -> None:
        """Initialize ViewMapSet."""
        super().__init__()
        self.view_maps: list[ViewMap] = []

    def serialize(self) -> ET.Element:
        """Serialize ViewMapSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ViewMapSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize view_maps (list to container "VIEW-MAPS")
        if self.view_maps:
            wrapper = ET.Element("VIEW-MAPS")
            for item in self.view_maps:
                serialized = SerializationHelper.serialize_item(item, "ViewMap")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ViewMapSet":
        """Deserialize XML element to ViewMapSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ViewMapSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ViewMapSet, cls).deserialize(element)

        # Parse view_maps (list from container "VIEW-MAPS")
        obj.view_maps = []
        container = SerializationHelper.find_child_element(element, "VIEW-MAPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.view_maps.append(child_value)

        return obj



class ViewMapSetBuilder:
    """Builder for ViewMapSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ViewMapSet = ViewMapSet()

    def build(self) -> ViewMapSet:
        """Build and return ViewMapSet object.

        Returns:
            ViewMapSet instance
        """
        # TODO: Add validation
        return self._obj
