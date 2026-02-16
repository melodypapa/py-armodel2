"""BswExclusiveAreaPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class BswExclusiveAreaPolicy(ARObject):
    """AUTOSAR BswExclusiveAreaPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("api_principle_enum", None, False, False, ApiPrincipleEnum),  # apiPrincipleEnum
        ("exclusive_area", None, False, False, ExclusiveArea),  # exclusiveArea
    ]

    def __init__(self) -> None:
        """Initialize BswExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle_enum: Optional[ApiPrincipleEnum] = None
        self.exclusive_area: Optional[ExclusiveArea] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswExclusiveAreaPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswExclusiveAreaPolicy":
        """Create BswExclusiveAreaPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswExclusiveAreaPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswExclusiveAreaPolicy since parent returns ARObject
        return cast("BswExclusiveAreaPolicy", obj)


class BswExclusiveAreaPolicyBuilder:
    """Builder for BswExclusiveAreaPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswExclusiveAreaPolicy = BswExclusiveAreaPolicy()

    def build(self) -> BswExclusiveAreaPolicy:
        """Build and return BswExclusiveAreaPolicy object.

        Returns:
            BswExclusiveAreaPolicy instance
        """
        # TODO: Add validation
        return self._obj
