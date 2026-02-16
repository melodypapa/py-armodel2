"""FlatMap AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)


class FlatMap(ARElement):
    """AUTOSAR FlatMap."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("instances", None, False, True, FlatInstanceDescriptor),  # instances
    ]

    def __init__(self) -> None:
        """Initialize FlatMap."""
        super().__init__()
        self.instances: list[FlatInstanceDescriptor] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlatMap to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlatMap":
        """Create FlatMap from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlatMap instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlatMap since parent returns ARObject
        return cast("FlatMap", obj)


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
