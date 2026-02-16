"""BswInterruptEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class BswInterruptEntity(BswModuleEntity):
    """AUTOSAR BswInterruptEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("interrupt_category", None, False, False, BswInterruptCategory),  # interruptCategory
        ("interrupt_source", None, True, False, None),  # interruptSource
    ]

    def __init__(self) -> None:
        """Initialize BswInterruptEntity."""
        super().__init__()
        self.interrupt_category: Optional[BswInterruptCategory] = None
        self.interrupt_source: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswInterruptEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInterruptEntity":
        """Create BswInterruptEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswInterruptEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswInterruptEntity since parent returns ARObject
        return cast("BswInterruptEntity", obj)


class BswInterruptEntityBuilder:
    """Builder for BswInterruptEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInterruptEntity = BswInterruptEntity()

    def build(self) -> BswInterruptEntity:
        """Build and return BswInterruptEntity object.

        Returns:
            BswInterruptEntity instance
        """
        # TODO: Add validation
        return self._obj
