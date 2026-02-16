"""AtpBlueprintMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprintable import (
    AtpBlueprintable,
)


class AtpBlueprintMapping(ARObject):
    """AUTOSAR AtpBlueprintMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("atp_blueprint", None, False, False, AtpBlueprint),  # atpBlueprint
        ("atp_blueprinted", None, False, False, AtpBlueprintable),  # atpBlueprinted
    ]

    def __init__(self) -> None:
        """Initialize AtpBlueprintMapping."""
        super().__init__()
        self.atp_blueprint: AtpBlueprint = None
        self.atp_blueprinted: AtpBlueprintable = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AtpBlueprintMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpBlueprintMapping":
        """Create AtpBlueprintMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AtpBlueprintMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AtpBlueprintMapping since parent returns ARObject
        return cast("AtpBlueprintMapping", obj)


class AtpBlueprintMappingBuilder:
    """Builder for AtpBlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpBlueprintMapping = AtpBlueprintMapping()

    def build(self) -> AtpBlueprintMapping:
        """Build and return AtpBlueprintMapping object.

        Returns:
            AtpBlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
