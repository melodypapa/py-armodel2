"""BlueprintMappingSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint_mapping import (
    AtpBlueprintMapping,
)


class BlueprintMappingSet(ARElement):
    """AUTOSAR BlueprintMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("blueprint_maps", None, False, True, AtpBlueprintMapping),  # blueprintMaps
    ]

    def __init__(self) -> None:
        """Initialize BlueprintMappingSet."""
        super().__init__()
        self.blueprint_maps: list[AtpBlueprintMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BlueprintMappingSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintMappingSet":
        """Create BlueprintMappingSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BlueprintMappingSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BlueprintMappingSet since parent returns ARObject
        return cast("BlueprintMappingSet", obj)


class BlueprintMappingSetBuilder:
    """Builder for BlueprintMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintMappingSet = BlueprintMappingSet()

    def build(self) -> BlueprintMappingSet:
        """Build and return BlueprintMappingSet object.

        Returns:
            BlueprintMappingSet instance
        """
        # TODO: Add validation
        return self._obj
