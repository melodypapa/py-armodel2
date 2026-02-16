"""BswSynchronousServerCallPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class BswSynchronousServerCallPoint(BswModuleCallPoint):
    """AUTOSAR BswSynchronousServerCallPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("called_entry_entry", None, False, False, BswModuleClientServerEntry),  # calledEntryEntry
        ("called_from", None, False, False, ExclusiveAreaNestingOrder),  # calledFrom
    ]

    def __init__(self) -> None:
        """Initialize BswSynchronousServerCallPoint."""
        super().__init__()
        self.called_entry_entry: Optional[BswModuleClientServerEntry] = None
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswSynchronousServerCallPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswSynchronousServerCallPoint":
        """Create BswSynchronousServerCallPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswSynchronousServerCallPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswSynchronousServerCallPoint since parent returns ARObject
        return cast("BswSynchronousServerCallPoint", obj)


class BswSynchronousServerCallPointBuilder:
    """Builder for BswSynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswSynchronousServerCallPoint = BswSynchronousServerCallPoint()

    def build(self) -> BswSynchronousServerCallPoint:
        """Build and return BswSynchronousServerCallPoint object.

        Returns:
            BswSynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
