"""DdsHistory AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsHistory(ARObject):
    """AUTOSAR DdsHistory."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("history_kind", None, False, False, DdsHistoryKindEnum),  # historyKind
        ("history_order", None, True, False, None),  # historyOrder
    ]

    def __init__(self) -> None:
        """Initialize DdsHistory."""
        super().__init__()
        self.history_kind: Optional[DdsHistoryKindEnum] = None
        self.history_order: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsHistory to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsHistory":
        """Create DdsHistory from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsHistory instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsHistory since parent returns ARObject
        return cast("DdsHistory", obj)


class DdsHistoryBuilder:
    """Builder for DdsHistory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsHistory = DdsHistory()

    def build(self) -> DdsHistory:
        """Build and return DdsHistory object.

        Returns:
            DdsHistory instance
        """
        # TODO: Add validation
        return self._obj
