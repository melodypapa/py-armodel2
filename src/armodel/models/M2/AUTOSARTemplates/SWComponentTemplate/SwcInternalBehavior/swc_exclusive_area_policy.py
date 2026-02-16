"""SwcExclusiveAreaPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class SwcExclusiveAreaPolicy(ARObject):
    """AUTOSAR SwcExclusiveAreaPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("api_principle_enum", None, False, False, ApiPrincipleEnum),  # apiPrincipleEnum
        ("exclusive_area", None, False, False, ExclusiveArea),  # exclusiveArea
    ]

    def __init__(self) -> None:
        """Initialize SwcExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle_enum: Optional[ApiPrincipleEnum] = None
        self.exclusive_area: Optional[ExclusiveArea] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcExclusiveAreaPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcExclusiveAreaPolicy":
        """Create SwcExclusiveAreaPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcExclusiveAreaPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcExclusiveAreaPolicy since parent returns ARObject
        return cast("SwcExclusiveAreaPolicy", obj)


class SwcExclusiveAreaPolicyBuilder:
    """Builder for SwcExclusiveAreaPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcExclusiveAreaPolicy = SwcExclusiveAreaPolicy()

    def build(self) -> SwcExclusiveAreaPolicy:
        """Build and return SwcExclusiveAreaPolicy object.

        Returns:
            SwcExclusiveAreaPolicy instance
        """
        # TODO: Add validation
        return self._obj
