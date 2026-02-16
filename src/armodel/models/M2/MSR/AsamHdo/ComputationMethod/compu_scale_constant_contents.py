"""CompuScaleConstantContents AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)


class CompuScaleConstantContents(CompuScaleContents):
    """AUTOSAR CompuScaleConstantContents."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_const", None, False, False, CompuConst),  # compuConst
    ]

    def __init__(self) -> None:
        """Initialize CompuScaleConstantContents."""
        super().__init__()
        self.compu_const: Optional[CompuConst] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuScaleConstantContents to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScaleConstantContents":
        """Create CompuScaleConstantContents from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuScaleConstantContents instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuScaleConstantContents since parent returns ARObject
        return cast("CompuScaleConstantContents", obj)


class CompuScaleConstantContentsBuilder:
    """Builder for CompuScaleConstantContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScaleConstantContents = CompuScaleConstantContents()

    def build(self) -> CompuScaleConstantContents:
        """Build and return CompuScaleConstantContents object.

        Returns:
            CompuScaleConstantContents instance
        """
        # TODO: Add validation
        return self._obj
