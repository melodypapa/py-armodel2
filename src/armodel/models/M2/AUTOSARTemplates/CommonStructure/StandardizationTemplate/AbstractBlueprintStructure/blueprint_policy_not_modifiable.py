"""BlueprintPolicyNotModifiable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)


class BlueprintPolicyNotModifiable(BlueprintPolicy):
    """AUTOSAR BlueprintPolicyNotModifiable."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize BlueprintPolicyNotModifiable."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BlueprintPolicyNotModifiable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintPolicyNotModifiable":
        """Create BlueprintPolicyNotModifiable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BlueprintPolicyNotModifiable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BlueprintPolicyNotModifiable since parent returns ARObject
        return cast("BlueprintPolicyNotModifiable", obj)


class BlueprintPolicyNotModifiableBuilder:
    """Builder for BlueprintPolicyNotModifiable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintPolicyNotModifiable = BlueprintPolicyNotModifiable()

    def build(self) -> BlueprintPolicyNotModifiable:
        """Build and return BlueprintPolicyNotModifiable object.

        Returns:
            BlueprintPolicyNotModifiable instance
        """
        # TODO: Add validation
        return self._obj
