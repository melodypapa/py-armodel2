"""BlueprintPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class BlueprintPolicy(ARObject):
    """AUTOSAR BlueprintPolicy."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("attribute_name", None, True, False, None),  # attributeName
    ]

    def __init__(self) -> None:
        """Initialize BlueprintPolicy."""
        super().__init__()
        self.attribute_name: String = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BlueprintPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintPolicy":
        """Create BlueprintPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BlueprintPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BlueprintPolicy since parent returns ARObject
        return cast("BlueprintPolicy", obj)


class BlueprintPolicyBuilder:
    """Builder for BlueprintPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintPolicy = BlueprintPolicy()

    def build(self) -> BlueprintPolicy:
        """Build and return BlueprintPolicy object.

        Returns:
            BlueprintPolicy instance
        """
        # TODO: Add validation
        return self._obj
