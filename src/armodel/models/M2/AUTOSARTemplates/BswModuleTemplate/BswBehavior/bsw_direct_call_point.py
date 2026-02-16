"""BswDirectCallPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class BswDirectCallPoint(BswModuleCallPoint):
    """AUTOSAR BswDirectCallPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("called_entry", None, False, False, BswModuleEntry),  # calledEntry
        ("called_from", None, False, False, ExclusiveAreaNestingOrder),  # calledFrom
    ]

    def __init__(self) -> None:
        """Initialize BswDirectCallPoint."""
        super().__init__()
        self.called_entry: Optional[BswModuleEntry] = None
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswDirectCallPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswDirectCallPoint":
        """Create BswDirectCallPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswDirectCallPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswDirectCallPoint since parent returns ARObject
        return cast("BswDirectCallPoint", obj)


class BswDirectCallPointBuilder:
    """Builder for BswDirectCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDirectCallPoint = BswDirectCallPoint()

    def build(self) -> BswDirectCallPoint:
        """Build and return BswDirectCallPoint object.

        Returns:
            BswDirectCallPoint instance
        """
        # TODO: Add validation
        return self._obj
