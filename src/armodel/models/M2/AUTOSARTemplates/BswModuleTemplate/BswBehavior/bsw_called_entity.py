"""BswCalledEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)


class BswCalledEntity(BswModuleEntity):
    """AUTOSAR BswCalledEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize BswCalledEntity."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswCalledEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswCalledEntity":
        """Create BswCalledEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswCalledEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswCalledEntity since parent returns ARObject
        return cast("BswCalledEntity", obj)


class BswCalledEntityBuilder:
    """Builder for BswCalledEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswCalledEntity = BswCalledEntity()

    def build(self) -> BswCalledEntity:
        """Build and return BswCalledEntity object.

        Returns:
            BswCalledEntity instance
        """
        # TODO: Add validation
        return self._obj
