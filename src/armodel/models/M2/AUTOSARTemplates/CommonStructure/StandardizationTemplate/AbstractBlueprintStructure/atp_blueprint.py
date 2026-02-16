"""AtpBlueprint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)


class AtpBlueprint(Identifiable):
    """AUTOSAR AtpBlueprint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("blueprint_policies", None, False, True, BlueprintPolicy),  # blueprintPolicies
    ]

    def __init__(self) -> None:
        """Initialize AtpBlueprint."""
        super().__init__()
        self.blueprint_policies: list[BlueprintPolicy] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AtpBlueprint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpBlueprint":
        """Create AtpBlueprint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AtpBlueprint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AtpBlueprint since parent returns ARObject
        return cast("AtpBlueprint", obj)


class AtpBlueprintBuilder:
    """Builder for AtpBlueprint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpBlueprint = AtpBlueprint()

    def build(self) -> AtpBlueprint:
        """Build and return AtpBlueprint object.

        Returns:
            AtpBlueprint instance
        """
        # TODO: Add validation
        return self._obj
