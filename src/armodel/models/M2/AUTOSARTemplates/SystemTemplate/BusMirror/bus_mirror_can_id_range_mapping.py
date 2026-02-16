"""BusMirrorCanIdRangeMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BusMirrorCanIdRangeMapping(ARObject):
    """AUTOSAR BusMirrorCanIdRangeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_base", None, True, False, None),  # destinationBase
        ("source_can_id_code", None, True, False, None),  # sourceCanIdCode
        ("source_can_id", None, True, False, None),  # sourceCanId
    ]

    def __init__(self) -> None:
        """Initialize BusMirrorCanIdRangeMapping."""
        super().__init__()
        self.destination_base: Optional[PositiveInteger] = None
        self.source_can_id_code: Optional[PositiveInteger] = None
        self.source_can_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BusMirrorCanIdRangeMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdRangeMapping":
        """Create BusMirrorCanIdRangeMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BusMirrorCanIdRangeMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BusMirrorCanIdRangeMapping since parent returns ARObject
        return cast("BusMirrorCanIdRangeMapping", obj)


class BusMirrorCanIdRangeMappingBuilder:
    """Builder for BusMirrorCanIdRangeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorCanIdRangeMapping = BusMirrorCanIdRangeMapping()

    def build(self) -> BusMirrorCanIdRangeMapping:
        """Build and return BusMirrorCanIdRangeMapping object.

        Returns:
            BusMirrorCanIdRangeMapping instance
        """
        # TODO: Add validation
        return self._obj
