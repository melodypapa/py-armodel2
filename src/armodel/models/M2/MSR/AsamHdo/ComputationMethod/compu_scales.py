"""CompuScales AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import (
    CompuContent,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale import (
    CompuScale,
)


class CompuScales(CompuContent):
    """AUTOSAR CompuScales."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_scales", None, False, True, CompuScale),  # compuScales
    ]

    def __init__(self) -> None:
        """Initialize CompuScales."""
        super().__init__()
        self.compu_scales: list[CompuScale] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuScales to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScales":
        """Create CompuScales from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuScales instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuScales since parent returns ARObject
        return cast("CompuScales", obj)


class CompuScalesBuilder:
    """Builder for CompuScales."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScales = CompuScales()

    def build(self) -> CompuScales:
        """Build and return CompuScales object.

        Returns:
            CompuScales instance
        """
        # TODO: Add validation
        return self._obj
