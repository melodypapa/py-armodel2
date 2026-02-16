"""BswSchedulableEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)


class BswSchedulableEntity(BswModuleEntity):
    """AUTOSAR BswSchedulableEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize BswSchedulableEntity."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswSchedulableEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswSchedulableEntity":
        """Create BswSchedulableEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswSchedulableEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswSchedulableEntity since parent returns ARObject
        return cast("BswSchedulableEntity", obj)


class BswSchedulableEntityBuilder:
    """Builder for BswSchedulableEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswSchedulableEntity = BswSchedulableEntity()

    def build(self) -> BswSchedulableEntity:
        """Build and return BswSchedulableEntity object.

        Returns:
            BswSchedulableEntity instance
        """
        # TODO: Add validation
        return self._obj
