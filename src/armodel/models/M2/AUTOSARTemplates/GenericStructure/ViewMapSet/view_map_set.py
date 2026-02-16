"""ViewMapSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet.view_map import (
    ViewMap,
)


class ViewMapSet(ARElement):
    """AUTOSAR ViewMapSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("view_maps", None, False, True, ViewMap),  # viewMaps
    ]

    def __init__(self) -> None:
        """Initialize ViewMapSet."""
        super().__init__()
        self.view_maps: list[ViewMap] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ViewMapSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ViewMapSet":
        """Create ViewMapSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ViewMapSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ViewMapSet since parent returns ARObject
        return cast("ViewMapSet", obj)


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
