"""PhysicalDimensionMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)


class PhysicalDimensionMapping(ARObject):
    """AUTOSAR PhysicalDimensionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_physical", None, False, False, PhysicalDimension),  # firstPhysical
        ("second_physical", None, False, False, PhysicalDimension),  # secondPhysical
    ]

    def __init__(self) -> None:
        """Initialize PhysicalDimensionMapping."""
        super().__init__()
        self.first_physical: Optional[PhysicalDimension] = None
        self.second_physical: Optional[PhysicalDimension] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PhysicalDimensionMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimensionMapping":
        """Create PhysicalDimensionMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PhysicalDimensionMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PhysicalDimensionMapping since parent returns ARObject
        return cast("PhysicalDimensionMapping", obj)


class PhysicalDimensionMappingBuilder:
    """Builder for PhysicalDimensionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalDimensionMapping = PhysicalDimensionMapping()

    def build(self) -> PhysicalDimensionMapping:
        """Build and return PhysicalDimensionMapping object.

        Returns:
            PhysicalDimensionMapping instance
        """
        # TODO: Add validation
        return self._obj
