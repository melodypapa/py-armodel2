"""SwDataDependency AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_generic_math import (
    CompuGenericMath,
)


class SwDataDependency(ARObject):
    """AUTOSAR SwDataDependency."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_data", None, False, False, CompuGenericMath),  # swData
    ]

    def __init__(self) -> None:
        """Initialize SwDataDependency."""
        super().__init__()
        self.sw_data: Optional[CompuGenericMath] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwDataDependency to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDependency":
        """Create SwDataDependency from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwDataDependency instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwDataDependency since parent returns ARObject
        return cast("SwDataDependency", obj)


class SwDataDependencyBuilder:
    """Builder for SwDataDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwDataDependency = SwDataDependency()

    def build(self) -> SwDataDependency:
        """Build and return SwDataDependency object.

        Returns:
            SwDataDependency instance
        """
        # TODO: Add validation
        return self._obj
