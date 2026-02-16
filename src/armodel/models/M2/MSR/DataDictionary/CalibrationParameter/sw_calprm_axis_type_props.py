"""SwCalprmAxisTypeProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class SwCalprmAxisTypeProps(ARObject):
    """AUTOSAR SwCalprmAxisTypeProps."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_gradient", None, True, False, None),  # maxGradient
        ("monotony", None, False, False, MonotonyEnum),  # monotony
    ]

    def __init__(self) -> None:
        """Initialize SwCalprmAxisTypeProps."""
        super().__init__()
        self.max_gradient: Optional[Float] = None
        self.monotony: Optional[MonotonyEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwCalprmAxisTypeProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmAxisTypeProps":
        """Create SwCalprmAxisTypeProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwCalprmAxisTypeProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwCalprmAxisTypeProps since parent returns ARObject
        return cast("SwCalprmAxisTypeProps", obj)


class SwCalprmAxisTypePropsBuilder:
    """Builder for SwCalprmAxisTypeProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmAxisTypeProps = SwCalprmAxisTypeProps()

    def build(self) -> SwCalprmAxisTypeProps:
        """Build and return SwCalprmAxisTypeProps object.

        Returns:
            SwCalprmAxisTypeProps instance
        """
        # TODO: Add validation
        return self._obj
