"""RelativeTolerance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class RelativeTolerance(ARObject):
    """AUTOSAR RelativeTolerance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("relative", None, True, False, None),  # relative
    ]

    def __init__(self) -> None:
        """Initialize RelativeTolerance."""
        super().__init__()
        self.relative: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RelativeTolerance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RelativeTolerance":
        """Create RelativeTolerance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RelativeTolerance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RelativeTolerance since parent returns ARObject
        return cast("RelativeTolerance", obj)


class RelativeToleranceBuilder:
    """Builder for RelativeTolerance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RelativeTolerance = RelativeTolerance()

    def build(self) -> RelativeTolerance:
        """Build and return RelativeTolerance object.

        Returns:
            RelativeTolerance instance
        """
        # TODO: Add validation
        return self._obj
