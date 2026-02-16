"""AbsoluteTolerance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class AbsoluteTolerance(ARObject):
    """AUTOSAR AbsoluteTolerance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("absolute", None, True, False, None),  # absolute
    ]

    def __init__(self) -> None:
        """Initialize AbsoluteTolerance."""
        super().__init__()
        self.absolute: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbsoluteTolerance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbsoluteTolerance":
        """Create AbsoluteTolerance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbsoluteTolerance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbsoluteTolerance since parent returns ARObject
        return cast("AbsoluteTolerance", obj)


class AbsoluteToleranceBuilder:
    """Builder for AbsoluteTolerance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbsoluteTolerance = AbsoluteTolerance()

    def build(self) -> AbsoluteTolerance:
        """Build and return AbsoluteTolerance object.

        Returns:
            AbsoluteTolerance instance
        """
        # TODO: Add validation
        return self._obj
