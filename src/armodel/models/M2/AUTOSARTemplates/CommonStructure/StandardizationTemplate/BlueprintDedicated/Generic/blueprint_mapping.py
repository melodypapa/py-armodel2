"""BlueprintMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprintable import (
    AtpBlueprintable,
)


class BlueprintMapping(ARObject):
    """AUTOSAR BlueprintMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("blueprint", None, False, False, AtpBlueprint),  # blueprint
        ("derived_object", None, False, False, AtpBlueprintable),  # derivedObject
    ]

    def __init__(self) -> None:
        """Initialize BlueprintMapping."""
        super().__init__()
        self.blueprint: AtpBlueprint = None
        self.derived_object: AtpBlueprintable = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BlueprintMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintMapping":
        """Create BlueprintMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BlueprintMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BlueprintMapping since parent returns ARObject
        return cast("BlueprintMapping", obj)


class BlueprintMappingBuilder:
    """Builder for BlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintMapping = BlueprintMapping()

    def build(self) -> BlueprintMapping:
        """Build and return BlueprintMapping object.

        Returns:
            BlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
