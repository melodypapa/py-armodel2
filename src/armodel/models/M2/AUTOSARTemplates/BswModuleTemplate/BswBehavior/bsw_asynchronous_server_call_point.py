"""BswAsynchronousServerCallPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)


class BswAsynchronousServerCallPoint(BswModuleCallPoint):
    """AUTOSAR BswAsynchronousServerCallPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("called_entry_entry", None, False, False, BswModuleClientServerEntry),  # calledEntryEntry
    ]

    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallPoint."""
        super().__init__()
        self.called_entry_entry: Optional[BswModuleClientServerEntry] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswAsynchronousServerCallPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswAsynchronousServerCallPoint":
        """Create BswAsynchronousServerCallPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswAsynchronousServerCallPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswAsynchronousServerCallPoint since parent returns ARObject
        return cast("BswAsynchronousServerCallPoint", obj)


class BswAsynchronousServerCallPointBuilder:
    """Builder for BswAsynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallPoint = BswAsynchronousServerCallPoint()

    def build(self) -> BswAsynchronousServerCallPoint:
        """Build and return BswAsynchronousServerCallPoint object.

        Returns:
            BswAsynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
